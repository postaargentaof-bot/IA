#!/bin/bash
# Arma los 8 videos (A, D y las 2 reservas de A, en 9:16 y 4:5) con el motor de anuncios/src/video2/.
# No gasta créditos: usa las voces ya grabadas de anuncios/audio/.
set -e
cd "$(dirname "$0")/.."
T=$(mktemp -d)
arm () { # vid fmt voz estilo salida
  node scripts/render_video.js $1 $2 $T/$1-$2.mp4
  python3 scripts/mezclar_audio.py $T/$1-$2.mp4 anuncios/audio/$3 $4 $5
}
for f in v h; do s=$([ $f = v ] && echo 9x16 || echo 4x5)
  arm a  $f ia1-precio-voz.mp3           pop  anuncios/img/ia1-precio-$s.mp4
  arm d  $f ia4-sol-voz.mp3              lofi anuncios/img/ia4-sol-$s.mp4
  arm r2 $f ia1b-precios-primero-voz.mp3 pop  anuncios/img/reserva/ia1b-precios-primero-$s.mp4
  arm r3 $f ia1c-2340-voz.mp3            pop  anuncios/img/reserva/ia1c-2340-$s.mp4
done
