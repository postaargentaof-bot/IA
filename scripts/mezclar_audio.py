"""Le pone el audio a un video mudo hecho con render_video.js: voz + música propia (scripts/musica.py)
que baja sola cuando habla la voz + efectos (pop, whoosh, tick, tap, ding), y deja todo a -14 LUFS.
Uso: python3 scripts/mezclar_audio.py <video-mudo.mp4> <voz.mp3|wav> <pop|lofi> <salida.mp4>
(los efectos y su tiempo salen de <video-mudo.mp4>.sfx.json)"""
import sys, json, subprocess, tempfile, wave, os, pathlib
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import musica as M
SR = 48000
mudo, voz, estilo, out = sys.argv[1:5]
info = json.load(open(mudo + '.sfx.json'))
dur = info['dur']
tmp = tempfile.mkdtemp()
def leer(p):
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', p, '-ac', '2', '-ar', str(SR), '-f', 's16le', f'{tmp}/x.raw'], check=True)
    return np.fromfile(f'{tmp}/x.raw', '<i2').reshape(-1, 2).astype(np.float64) / 32768
N = int(dur * SR)
v = leer(voz)[:N]; V = np.zeros((N, 2)); V[:len(v)] = v
m = M.musica(estilo, dur)[:N]; MU = np.zeros((N, 2)); MU[:len(m)] = m
M.sfx(f'{tmp}/sfx')
S = np.zeros((N, 2))
cache = {}
for t, nombre, vol in info['sfx']:
    if nombre not in cache: cache[nombre] = leer(f'{tmp}/sfx/{nombre}.wav')
    x = cache[nombre] * vol; i = int(max(0, t) * SR); j = min(N, i + len(x))
    if i < N: S[i:j] += x[:j - i]
# ducking: la música baja ~8 dB cuando hay voz (envolvente de 60 ms, suavizada)
rms = np.sqrt(np.convolve((V ** 2).mean(1), np.ones(2880) / 2880, 'same'))
act = np.clip(rms / 0.04, 0, 1)
act = np.convolve(act, np.ones(9600) / 9600, 'same')
g = 10 ** ((-8 * act) / 20)
def nivel(x): return np.sqrt((x ** 2).mean()) + 1e-9
mus = MU / nivel(MU) * nivel(V) * 10 ** (-17 / 20) * g[:, None]
sf = S / max(1e-9, np.abs(S).max()) * np.abs(V).max() * 0.35
mix = V + mus + sf
mix = mix / np.abs(mix).max() * 0.7
with wave.open(f'{tmp}/mix.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype('<i2').tobytes())
# volumen final: -14 LUFS medido
mm = subprocess.run(['ffmpeg', '-hide_banner', '-i', f'{tmp}/mix.wav', '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
I = float([l for l in mm.splitlines() if l.strip().startswith('I:')][-1].split()[1])
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mudo, '-i', f'{tmp}/mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                '-af', f'volume={-14 - I:.2f}dB,alimiter=limit=0.95:level=false', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], check=True)
mm = subprocess.run(['ffmpeg', '-hide_banner', '-i', out, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
I2 = [l.strip() for l in mm.splitlines() if l.strip().startswith(('I:', 'Peak:'))][-2:]
print(out, ' '.join(I2), round(os.path.getsize(out) / 1e6, 1), 'MB')
