# Tareas

> El tablero, con una fila por tarea.
> - **Estado:** por hacer, en curso o hecho.
> - **Quién:** {{NOMBRE}} o Claude.
> - **Chat:** el nombre corto del chat que la trabaja.
>
> Cada chat edita solo la fila de su tarea. Lo hecho baja a «Hecho» con una línea de nota. Una vez por mes, lo hecho pasa a `archivo/tareas-AAAA-MM.md`.

## En curso

| Tarea | Área | Quién | Para cuándo | Chat | Nota |
|---|---|---|---|---|---|

## Por hacer

| Tarea | Área | Quién | Para cuándo | Chat | Nota |
|---|---|---|---|---|---|
| Pagar la cuenta de Meta «Velas arg» (está en período de gracia) | campanas | {{NOMBRE}} | Hoy | — | Sin esto no se lanza nada |
| En el panel: downsell de «Las 200 instrucciones» al 50% (rama «rechazado» del upsell) y «La planilla» como primer bump (Diseño de ebooks → ⋮ → Mover antes) | oferta | {{NOMBRE}} | Hoy | — | El conector no puede hacer estas dos. Después, Claude verifica |
| Crear un mail de la marca y cambiarlo en la landing (hoy aparece el de Taller Triple) | landing | {{NOMBRE}} + Claude | Antes de pautar | — | Aparece 3 veces en el HTML |
| Píxel nuevo para «La IA hace» y cargarlo en la tienda con su token | campanas | {{NOMBRE}} + Claude | Antes de pautar | — | Hoy hay un solo píxel («velas») para las dos tiendas |
| Compra de prueba real con los 2 bumps y el upsell, y confirmar la Compra en Resumen | landing | {{NOMBRE}} | Antes de pautar | — | Después se reembolsa desde Mercado Pago |
| Producir la tanda 1 (5 piezas) | creativos | {{NOMBRE}} + Claude | Antes de pautar | — | `areas/creativos/tandas/tanda-1/guiones.md`. Presupuesto de generación antes |
| Armar la CBO en borrador y lanzarla con el sí | campanas | Claude + {{NOMBRE}} | Después de lo anterior | — | `reglas/08`: 1 conjunto, 5 anuncios, 2–3 tickets por día |
| Dominio propio, verificación en Meta y Brevo para los carritos | landing | {{NOMBRE}} | Semana 1 | — | Riesgo 🟡, no frena la salida |
| Entrevista de arranque | general | Claude | Día 1 | — | `/arranque` |
| Bajar el cerebro de Bilbao y subirlo al repo | sistema | {{NOMBRE}} | Día 1 | — | `EMPEZA-ACA.md`, paso 3 |
| Armar Meta: Business Manager, página, Instagram, cuenta publicitaria, píxel, 2FA y tarjeta en dólares | campanas | {{NOMBRE}} | Semana 1 | — | Checklist en `reglas/06-meta.md` |
| Primera caza de ofertas | ofertas | Claude | Semana 1 | — | Skill `buscar-ofertas` (viene con el cerebro de Bilbao) y `reglas/03-oferta.md` |

## Hecho

| Tarea | Área | Quién | Hecho el | Nota |
|---|---|---|---|---|
| Auditoría completa antes de pautar | oferta | Claude | 12/11/2026 | `areas/oferta/auditoria-2026-11-12.md` |
| Precios nuevos: front 9.990, planilla 4.990, fotos 5.990 y upsell 16.990 | oferta | Claude | 12/11/2026 | La landing toma el precio sola (`{{price}}`). La oferta post-compra ya muestra 16.990 |
| Ocultar la barra «personas comprando» en los checkouts de las dos tiendas | landing | Claude | 12/11/2026 | Era un contador falso. Los timers de los bumps ya estaban apagados |
| Guiones de la tanda 1 | creativos | Claude | 12/11/2026 | `areas/creativos/tandas/tanda-1/guiones.md` |
