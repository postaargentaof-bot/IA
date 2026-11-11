# Guiones de los videos · «La IA hace, vos vendés» (11/11/2026)

> Chat de producción de creativos (tarea 8b). Reglas aplicadas (`reglas/07-creativos.md` del kit): gancho en 3 s, sin silencios (pausas recortadas a 0,30 s), cambio de plano cada 0,6–3,9 s, todo el texto entre los 290 y los 1.290 px de altura en 9:16, audio a −14 LUFS, archivos de menos de 30 MB, **sin el precio del libro ni fechas** en el video, voz a ~195 palabras por minuto.
>
> Voces (ElevenLabs, modelo v3, diseñadas el 11/11 y guardadas en la cuenta):
> - **A:** «IA vos vendes - mujer rioplatense» (`u3vPaY3NL56eQODsyxev`, la muestra 2 de la prueba).
> - **D:** «IA vos vendes - varon rioplatense» (`xe2v2RJBS57Ng34Bek9n`, la muestra 3).
>
> D va con voz de varón a propósito: con una voz de mujer se podría creer que habla Sol, y eso la convierte en testimonio.
>
> **Sin música:** no había una pista CC0 a mano y la regla de música de fondo es vieja (20/6/2026). Si se quiere, se suma después con una pista CC0 que se diga de dónde sale.
>
> Cómo se rearman: `python3 scripts/armar_videos_html.py` → `node scripts/render_anuncios.js anuncios/src/video-a.html <carpeta>` → `python3 scripts/armar_videos.py anuncios/src/video-a.json <carpeta> anuncios/audio/ia1-precio-voz.mp3 anuncios/img/ia1-precio` (igual con `video-d` y `anuncios/audio/ia4-sol-voz.mp3`; los de reserva usan los cuadros de `video-a` con `video-ia1b-precios-primero.json` / `video-ia1c-2340.json` y sus voces en `anuncios/audio/`). Los tiempos de cada plano están en `anuncios/src/video-*.json`. Las voces ya están grabadas: rearmar no gasta créditos.

---

## A · «¿Precio?» · `ia1-precio-9x16.mp4` / `ia1-precio-4x5.mp4` (≈18,7 s)

Negocio del ejemplo: Caro · Malva Indumentaria (ropa, Lanús). El $18.500 del buzo es el precio **del ejemplo** (sale de la landing), no el del libro.

| Seg. | Paso | Voz | En pantalla (texto grande) | Plano |
|---|---|---|---|---|
| 0,0 | 1 · Gancho | «¿Precio? ¿Precio? ¿Precio?» | ¿Precio? → ¿Precio? ¿Precio? → ¿Precio? ¿Precio? ¿Precio? | Chat que se llena de «¿precio?» (3 → 5 → 8 burbujas) |
| 2,2 | 2 · Re-gancho | «Si vendés por WhatsApp, lo contestás todo el día.» | Lo contestás todo el día | Lista de chats, todos con «¿precio?» sin leer |
| 4,1 | 3 · Solución | «Esto lo resolvés en una hora.» | Esto lo resolvés en una hora. | Tarjeta verde |
| 5,5 | 4 · Cómo funciona | «La IA te escribe tus quince respuestas, con tus precios y tu forma de hablar.» | La IA escribe tus 15 respuestas → Con tus precios y tu forma de hablar | Chat con la IA: la instrucción del Día 1 y la lista con atajos |
| 9,7 | 5 · Prueba (se ve) | «Te escriben ¿precio?, ponés barra precios y sale la respuesta lista.» | Te escriben «¿precio?» → Ponés /precios… → …y sale la respuesta lista | Chat: llega el mensaje, se escribe /precios, sale la respuesta |
| 13,5 | 6 · Qué es | «Es el Día uno de La IA hace, vos vendés, con ChatGPT gratis.» | DÍA 1 · WhatsApp sin perder la tarde · Una tarea por día, con ChatGPT gratis | Tapa real |
| 17,3 | 7 · CTA | «Tocá Comprar.» | La IA hace, vos vendés · Tocá Comprar | Tapa + botón |

Texto completo de la voz (330 caracteres, 59 palabras):
> ¿Precio? ¿Precio? ¿Precio? Si vendés por WhatsApp, lo contestás todo el día. Esto lo resolvés en una hora. La IA te escribe tus quince respuestas, con tus precios y tu forma de hablar. Te escriben ¿precio?, ponés barra precios y sale la respuesta lista. Es el Día uno de La IA hace, vos vendés, con ChatGPT gratis. Tocá Comprar.

---

## D · «Sol» · `ia4-sol-9x16.mp4` / `ia4-sol-4x5.mp4` (≈21,4 s)

Persona IA (retrato IMG-04). Todo sale del libro: la ficha de Sol (Día 0), su `/precios` y su mensaje de ausencia (Día 1). **Etiqueta fija «Ejemplo del libro · no es una clienta»** en todos los planos donde aparece Sol. Narrador en tercera persona; Sol no habla ni da testimonio (la frase del libro «Es lo que yo escribo 30 veces por semana» **no** se usa).

| Seg. | Paso | Voz | En pantalla | Plano |
|---|---|---|---|---|
| 0,0 | 1 · Gancho | «Así arma Sol sus respuestas de turnos.» | Así arma Sol sus respuestas de turnos | Retrato de Sol |
| 2,0 | 2 · Re-gancho | «Sol es un ejemplo armado del libro: hace uñas y pestañas.» | Sol · uñas y pestañas · Rosario · Un negocio armado para el libro | Retrato más cerca |
| 4,5 | (dolor) | (sigue la frase) | — | Chat lleno de preguntas de turnos |
| 6,2 | 3 · Solución | «Primero cargó su ficha: precios, seña y horarios.» | Primero cargó su ficha → Precios, seña y horarios (resaltados) | La ficha de Sol (Día 0) |
| 9,4 | 4 · Cómo funciona | «La IA le escribió las respuestas con su tono.» | Con su tono | Chat: «precio del semi?» → su `/precios` del libro |
| 11,9 | 5 · Prueba (se ve) | «Y a la noche, el mensaje de ausencia le pide a la clienta qué se quiere hacer y qué días puede.» | A la noche… → Ya le pide los datos del turno | Chat de noche: llega el mensaje y sale el de ausencia del libro, con lo importante resaltado |
| 16,9 | 6 · Qué es | «Es el Día uno de La IA hace, vos vendés.» | DÍA 1 · Respuestas y mensaje de ausencia · El ejemplo de Sol está en el libro | Tapa real |
| 20,0 | 7 · CTA | «Tocá Comprar.» | Tocá Comprar | Tapa + botón |

Texto completo de la voz (≈340 caracteres, 68 palabras):
> Así arma Sol sus respuestas de turnos. Sol es un ejemplo armado del libro: hace uñas y pestañas. Primero cargó su ficha: precios, seña y horarios. La IA le escribió las respuestas con su tono. Y a la noche, el mensaje de ausencia le pide a la clienta qué se quiere hacer y qué días puede. Es el Día uno de La IA hace, vos vendés. Tocá Comprar.

---

## Ganchos de reserva de A (en `anuncios/img/reserva/`, NO van en el lanzamiento)

Archivos: `reserva/ia1b-precios-primero-9x16.mp4` / `-4x5.mp4` (≈17,4 s) y `reserva/ia1c-2340-9x16.mp4` / `-4x5.mp4` (≈18,4 s).

Para renovar A si funciona (`07-creativos.md`: un gancho nuevo del mismo ángulo, el cuerpo igual). Cambian solo los primeros segundos; desde «La IA te escribe tus quince respuestas…» es el mismo audio y los mismos planos de A.

### A2 · «/precios primero» (idea #2 de `ideas.md`)
| Voz | En pantalla | Plano |
|---|---|---|
| «Escribís barra precios y la respuesta sale sola. Así se arma, en una hora.» | Escribís /precios… → …y la respuesta sale sola → Así se arma, en una hora. | Chat con /precios → respuesta enviada → tarjeta verde |

### A3 · «23:40» (idea #5 de `ideas.md`)
| Voz | En pantalla | Plano |
|---|---|---|
| «Son las once y media de la noche y te siguen preguntando el precio. Esto lo resolvés en una hora.» | 23:40 → Y te siguen preguntando el precio → Esto lo resolvés en una hora. | Chat oscuro que se llena de «¿precio?» → tarjeta verde |
