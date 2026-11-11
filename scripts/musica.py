"""Música y efectos de sonido generados por código (propios: sin licencias de terceros).
Uso:
  python3 scripts/musica.py musica <estilo> <segundos> <salida.wav>    estilo: pop | lofi
  python3 scripts/musica.py sfx <carpeta>                                -> pop.wav, whoosh.wav, tick.wav, tap.wav, ding.wav
"""
import sys, wave, pathlib
import numpy as np

SR = 48000
rng = np.random.default_rng(7)

def guardar(path, x):
    x = np.asarray(x, dtype=np.float64)
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    x = x / max(1e-9, np.abs(x).max()) * 0.89
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype('<i2').tobytes())

def env(n, a=0.005, d=0.2, s=0.0, sus=0.0, r=0.05):
    t = np.arange(n) / SR
    e = np.zeros(n)
    ai = int(a * SR); di = int(d * SR)
    e[:ai] = np.linspace(0, 1, ai, endpoint=False) if ai else 1
    seg = e[ai:ai + di]
    e[ai:ai + di] = 1 - (1 - s) * (np.arange(len(seg)) / max(1, di))
    e[ai + di:] = s
    if r:
        ri = int(r * SR)
        e[-ri:] *= np.linspace(1, 0, ri)
    return e

def nota(m):
    return 440 * 2 ** ((m - 69) / 12)

def kick(n=0.35):
    N = int(n * SR); t = np.arange(N) / SR
    f = 50 + 110 * np.exp(-t * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 9)

def clap(n=0.25):
    N = int(n * SR); t = np.arange(N) / SR
    x = rng.standard_normal(N)
    # paso banda casero: diferencia de dos promedios móviles
    k1 = np.convolve(x, np.ones(4) / 4, 'same'); k2 = np.convolve(x, np.ones(18) / 18, 'same')
    return (k1 - k2) * np.exp(-t * 18) * 1.4

def hat(n=0.06, abierto=False):
    N = int((0.18 if abierto else n) * SR); t = np.arange(N) / SR
    x = rng.standard_normal(N); x = x - np.convolve(x, np.ones(3) / 3, 'same')
    return x * np.exp(-t * (14 if abierto else 70)) * 0.5

def keys(freqs, dur, brillo=1.0):
    N = int(dur * SR); t = np.arange(N) / SR
    y = np.zeros(N)
    for f in freqs:
        y += (np.sin(2 * np.pi * f * t) + 0.35 * brillo * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t * 3)
              + 0.12 * np.sin(2 * np.pi * 3 * f * t) * np.exp(-t * 5))
    return y * env(N, 0.01, dur * 0.9, 0.35, 0, 0.08) / len(freqs)

def bajo(f, dur):
    N = int(dur * SR); t = np.arange(N) / SR
    y = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t)
    return np.tanh(1.6 * y) * env(N, 0.005, dur * 0.8, 0.6, 0, 0.04)

def poner(buf, x, t):
    i = int(t * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(x))
    buf[i:j] += x[:j - i]

def musica(estilo, segundos):
    N = int((segundos + 1) * SR)
    L = np.zeros(N); R = np.zeros(N)
    if estilo == 'pop':
        bpm = 112
        # I–V–vi–IV en Do mayor, voicings abiertos
        prog = [[60, 64, 67, 72], [59, 62, 67, 74], [57, 60, 64, 69], [57, 60, 65, 72]]
        bajos = [36, 43, 45, 41]
    else:
        bpm = 88
        # ii–V–I–vi con séptimas, más tibio
        prog = [[62, 65, 69, 72], [55, 59, 62, 65], [60, 64, 67, 71], [57, 60, 64, 67]]
        bajos = [38, 43, 36, 45]
    beat = 60 / bpm
    compas = 4 * beat
    t = 0.0; c = 0
    while t < segundos + 1:
        acorde = [nota(m) for m in prog[c % 4]]
        k = keys(acorde, compas, 1.0 if estilo == 'pop' else 0.5)
        if estilo == 'pop':
            # acordes en corcheas sincopadas
            for b in [0, 1.5, 2, 3.5]:
                seg = keys(acorde, beat * 0.9, 1.0) * 0.55
                poner(L, seg * 0.9, t + b * beat); poner(R, seg, t + b * beat + 0.012)
        else:
            poner(L, k * 0.7, t); poner(R, k * 0.7, t + 0.015)
        fb = nota(bajos[c % 4])
        for b in ([0, 1.5, 2, 3] if estilo == 'pop' else [0, 2.5]):
            sb = bajo(fb, beat * (0.9 if estilo == 'pop' else 1.4)) * 0.55
            poner(L, sb, t + b * beat); poner(R, sb, t + b * beat)
        for b in range(4):
            if estilo == 'pop' or b in (0, 2):
                poner(L, kick() * 0.9, t + b * beat); poner(R, kick() * 0.9, t + b * beat)
            if b in (1, 3):
                cl = clap() * (0.55 if estilo == 'pop' else 0.35)
                poner(L, cl, t + b * beat); poner(R, cl, t + b * beat + 0.004)
            for hh in (0, 0.5):
                h = hat(abierto=(estilo == 'pop' and hh == 0.5 and b == 3)) * (0.35 if estilo == 'pop' else 0.22)
                sw = 0.06 if (estilo == 'lofi' and hh == 0.5) else 0
                poner(L, h * 0.8, t + (b + hh + sw) * beat); poner(R, h, t + (b + hh + sw) * beat)
        t += compas; c += 1
    x = np.stack([L, R], 1)[:int(segundos * SR)]
    if estilo == 'lofi':
        # tibio: un poco de saturación y ruido de vinilo
        x = np.tanh(x * 1.2) + rng.standard_normal(x.shape) * 0.004
    n = len(x); fi = int(0.4 * SR); fo = int(1.2 * SR)
    x[:fi] *= np.linspace(0, 1, fi)[:, None]; x[-fo:] *= np.linspace(1, 0, fo)[:, None]
    return x

def sfx(carpeta):
    c = pathlib.Path(carpeta); c.mkdir(parents=True, exist_ok=True)
    # pop de burbuja
    N = int(0.12 * SR); t = np.arange(N) / SR
    f = 900 * np.exp(-t * 18) + 420
    guardar(c / 'pop.wav', np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 38) * 0.8)
    # whoosh de corte
    N = int(0.45 * SR); t = np.arange(N) / SR
    x = rng.standard_normal(N)
    y = np.zeros(N); a = 0.0
    for i in range(N):
        k = 0.02 + 0.5 * np.sin(np.pi * t[i] / 0.45) ** 2
        a += k * (x[i] - a); y[i] = a
    guardar(c / 'whoosh.wav', y * np.sin(np.pi * t / 0.45) ** 1.5)
    # tick de tecla
    N = int(0.03 * SR); t = np.arange(N) / SR
    guardar(c / 'tick.wav', rng.standard_normal(N) * np.exp(-t * 300) * 0.6)
    # tap (botón)
    N = int(0.09 * SR); t = np.arange(N) / SR
    guardar(c / 'tap.wav', np.sin(2 * np.pi * 1600 * t) * np.exp(-t * 60) + rng.standard_normal(N) * np.exp(-t * 400) * 0.3)
    # ding (respuesta enviada)
    N = int(0.6 * SR); t = np.arange(N) / SR
    guardar(c / 'ding.wav', (np.sin(2 * np.pi * 1318.5 * t) + 0.5 * np.sin(2 * np.pi * 1975.5 * t)) * np.exp(-t * 7))

if __name__ == '__main__':
    if sys.argv[1] == 'musica':
        guardar(sys.argv[4], musica(sys.argv[2], float(sys.argv[3])))
    else:
        sfx(sys.argv[2])
