---
name: arranque
description: Entrevista de arranque del Cortex. Completa CLAUDE.md, estado, tareas y la ecuación con los datos del dueño. Usar con "/arranque", "arranquemos", "haceme la entrevista" o cuando ESTADO.md dice SIN ARRANCAR.
---

# /arranque

## 1. La entrevista

Saludá en dos líneas y explicá para qué sirve: con esto, el sistema pasa a ser suyo. Después mandá **todas las preguntas en un solo mensaje**, numeradas y en bloques. Aclará que puede contestar como le salga (con audio transcrito, todas juntas o «no sé») y que lo que falte se completa después.

**Vos**

1. ¿Cómo te llamás y cómo querés que te hable (rioplatense, neutro, más técnico o más simple)?
2. ¿En qué país vas a vender y en qué moneda vas a cobrar?
3. ¿Cuántas horas por semana le podés dedicar, de verdad?
4. Del 0 al 5, ¿cuánto sabés de Meta Ads, de vender online, de diseño y de edición de video?

**Plata**

5. ¿Cuánto podés poner en pauta el primer mes sin que te duela? ¿Y cuánto estás dispuesto a perder como máximo en una oferta antes de descartarla? (Axel usa USD 200.)
6. ¿Con qué vas a pagar Meta? ¿Tenés una tarjeta en dólares?
7. ¿Qué costos fijos tenés ya (Claude, herramientas)?

**Negocio**

8. ¿Ya tenés un nombre o una marca? (Si no, lo elegimos con la oferta.)
9. ¿Qué nichos conocés o te interesan? No es para elegir por afinidad, que es un error común: es para saber por dónde arrancar a cazar.
10. ¿Tenés algún producto o arrancamos de cero?

**Herramientas**

11. ¿Qué cuentas tenés ya? Business Manager, página, Instagram, cuenta publicitaria, plataforma de venta, ElevenLabs, CapCut o Canva.
12. ¿Vas a trabajar desde la PC (VS Code) o desde el navegador y el celular?

**Lo legal**

13. ¿Estás inscripto para facturar (en la Argentina, el monotributo)? ¿Tenés contador?

**La meta**

14. ¿Qué querés lograr en 90 días? Con un número: ventas por día, ganancia por mes o lo que sea.

## 2. Con las respuestas

1. **Reemplazá estos marcadores en todo el repo:**

   | Marcador | Con qué |
   |---|---|
   | `{{NOMBRE}}` | Su nombre |
   | `{{NEGOCIO}}` | La marca o, si no hay, «Mi negocio» |
   | `{{PAÍS}}` | El país donde vende |
   | `{{OFERTA}}` | La oferta o, si no hay, «ninguna todavía» |
   | `{{TONO}}` | El tono que pidió |
   | `{{PLATAFORMA}}` | Su plataforma o, si no hay, «a elegir» |
   | `{{TOPE}}` | El tope de pérdida por oferta |
   | `{{FECHA}}` | La fecha de hoy |

   Buscalos con `grep -rn "{{NOMBRE}}\|{{NEGOCIO}}\|{{PAÍS}}\|{{OFERTA}}\|{{TONO}}\|{{PLATAFORMA}}\|{{TOPE}}\|{{FECHA}}" .`.

   **No toques** `{{campaign.name}}`, `{{adset.name}}`, `{{ad.name}}` ni `{{ad.id}}`: son parámetros de Meta.
2. **Reescribí `ESTADO.md`:**
   - sacá «SIN ARRANCAR»;
   - en una línea, dónde está y qué sigue;
   - completá los números que haya.
3. **Completá en `reglas/02-ecuacion.md`** lo que se sepa. Lo que no, como «se mide con la primera semana de ventas».
4. **`tareas.md`:** armá las tareas de los primeros 30 días (la ruta de `EMPEZA-ACA.md`), ajustadas a sus horas y a lo que ya tiene, cada una con quién y para cuándo.
5. **`decisiones.md`:** completá la primera entrada y sumá lo que haya decidido en la entrevista (tope de pérdida, plataforma, país).
6. **Si el nicho es sensible** (religión, salud, dinero, relaciones), sumá sus reglas propias al final de `reglas/09-reglas-de-juego.md` y a «Reglas que no se rompen» de `CLAUDE.md`.
7. **Mirá si el cerebro de Bilbao está instalado** (`conocimiento/bilbao/WIKI/`). Si no está, dejalo como primera tarea suya.

## 3. Sé honesto

Antes de cerrar, decile en una tabla corta qué ves:

- **¿Alcanza la plata?** Un test necesita 2–3 tickets por día durante 5–7 días. Con un ticket de USD 10, son entre USD 100 y 210 por oferta, más las herramientas. Si no alcanza, decilo y proponé cómo arrancar igual (un solo test a la vez, el producto antes que la pauta).
- **¿Alcanzan las horas?** Con menos de 10 por semana, una cosa a la vez.
- **¿La meta de 90 días es realista** con esa plata y esas horas? Si no, decí qué número sí.

## 4. Cerrá

1. Hacé commit (`arranque: entrevista de {{NOMBRE}}`) y push a `main`.
2. Terminá con el próximo paso concreto: casi siempre, armar las cuentas de Meta o arrancar la primera caza («caza · <nicho>»), con su primer mensaje listo.
