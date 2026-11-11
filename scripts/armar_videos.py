"""Monta los videos con ffmpeg a partir de los cuadros (PNG) y la voz final (WAV).
Uso: python3 scripts/armar_videos.py <video.json> <carpeta-cuadros> <voz.wav> <salida-sin-extension>
video.json: {"cuadros": [["a01", 0.0], ["a02", 0.72], ...]}  (inicio de cada plano en segundos de la voz)
Hace un mp4 en 9:16 y otro en 4:5: zoom suave en cada plano, corte seco, voz a -14 LUFS, H.264 + AAC.
"""
import json, subprocess, sys, os, tempfile
spec, frames, voz, out = sys.argv[1:5]
cuadros = json.load(open(spec))['cuadros']
dur_voz = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', voz]))
fin = dur_voz + 0.5
FPS = 30
for suf, (W, H) in {'9x16': (1080, 1920), '4x5': (1080, 1350)}.items():
    tmp = tempfile.mkdtemp()
    lista = []
    for i, (n, t0) in enumerate(cuadros):
        t1 = cuadros[i + 1][1] if i + 1 < len(cuadros) else fin
        nf = max(1, round((t1 - t0) * FPS))
        clip = f'{tmp}/{i:02d}.mp4'
        # zoom de 1,00 a 1,02 centrado en la caja de texto (no saca texto de la zona segura)
        cy = 790 if suf == '9x16' else H / 2
        z = f"zoompan=z='1+0.02*on/{nf}':x='iw/2-(iw/zoom/2)':y='{cy}*2-({cy}*2)/zoom':d={nf}:s={W}x{H}:fps={FPS}"
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{frames}/{n}-{suf}.png',
                        '-vf', f'scale={W*2}:{H*2},{z},format=yuv420p', '-frames:v', str(nf),
                        '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', clip], check=True)
        lista.append(f"file '{clip}'")
    open(f'{tmp}/l.txt', 'w').write('\n'.join(lista))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/l.txt', '-i', voz,
                    '-filter_complex', f'[1:a]apad,atrim=0:{fin:.3f},loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]',
                    '-map', '0:v', '-map', '[a]', '-c:v', 'libx264', '-preset', 'slow', '-crf', '21', '-pix_fmt', 'yuv420p',
                    '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', '-shortest', f'{out}-{suf}.mp4'], check=True)
    # segunda pasada: corrige el volumen para que quede en -14 LUFS exactos (±0,3)
    m = subprocess.run(['ffmpeg', '-hide_banner', '-i', f'{out}-{suf}.mp4', '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    I = float([l for l in m.splitlines() if l.strip().startswith('I:')][-1].split()[1])
    if abs(I + 14) > 0.3:
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{out}-{suf}.mp4', '-map', '0', '-c:v', 'copy',
                        '-af', f'volume={-14 - I:.2f}dB', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart',
                        f'{tmp}/v.mp4'], check=True)
        os.replace(f'{tmp}/v.mp4', f'{out}-{suf}.mp4')
    print(out + '-' + suf + '.mp4', round(os.path.getsize(f'{out}-{suf}.mp4') / 1e6, 1), 'MB')
