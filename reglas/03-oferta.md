# 03 · Oferta: cómo se elige y cómo se testea

_Última actualización: {{FECHA}}. Lo de Bilbao lleva la fecha del video. Verificá cada cita con el agente `bilbao` cuando instales su cerebro._

## Los 8 filtros

Una oferta se modela solo si pasa los 8:

1. **Vende:** tiene de 30 a 50 anuncios activos a la misma oferta. Que el número oscile (100, 80, 120) es normal [Bilbao, 30/8/2026].
2. **Está andando:** lleva más de 3 días al aire, lo que descarta a los que están testeando, y mejor si lleva 1 o 2 semanas con volumen sostenido [Bilbao, 30/8/2026]. «Una persona no va a dejar más de 3 días corriendo un anuncio [que pierde]».
3. **Sin marca personal** ni un experto detrás.
4. **Clonable tal cual:** landing y checkout, con el pago antes (no por WhatsApp).
5. **Sin responsabilidad profesional**, como salud o temas legales.
6. **Riesgo bajo o medio con Meta.**
7. **Se adapta a tu país** y se puede cobrar en tu moneda.
8. **Contenido propio:** nada pirata.

**Errores al elegir:**

- elegir por afinidad con el nicho;
- elegir solo por la cantidad de anuncios;
- elegir algo tan fácil de modelar que ya está saturado.

**Dónde buscar:** Bilbao hoy corre 4 ofertas, todas en **salud, relaciones y dinero**: «big niche, big market» [Bilbao, 18/10/2026]. Se espía Brasil y EE. UU. y se modela para tu país.

**La Biblioteca de anuncios se mira sin iniciar sesión** (con un navegador o un perfil sin Facebook), nunca con la cuenta que maneja tus anuncios.

## El embudo de ofertas

| # | Etapa | Qué se hace | Quién | Pasa a la siguiente si |
|---|---|---|---|---|
| 1 | **Caza** | Skill `buscar-ofertas` en un nicho | Claude, en un chat «caza · <nicho>» | Hay al menos una página que pasa los filtros 1 y 2 |
| 2 | **Filtro** | Los 8 filtros, y el backend a la vista (bump o upsells en el embudo de la fuente) | Claude | Pasa los 8 |
| 3 | **Hueco en tu país** | Se busca con 3 sinónimos en la Biblioteca de tu país: ¿quién la hace y cómo? | Claude | Nadie la hace bien, o la hacen con menos nivel |
| 4 | **Elección** | Una tabla corta con las mejores de la semana | **{{NOMBRE}}** elige una | — |
| 5 | **Radiografía y hoja** | El embudo hasta el precio, los ángulos probados y una hoja de oferta de 1 página | Claude + `revisor` | El revisor no marca nada que frene |
| 6 | **MVP** | Tienda, landing, checkout con bump, el producto y de 5 a 10 creativos | Claude arma; {{NOMBRE}} hace voces y renders | La compra de prueba anda |
| 7 | **Test** | Ver abajo | {{NOMBRE}} da el sí y se publica | — |
| 8 | **Veredicto** | Escalar, ajustar o descartar | {{NOMBRE}}, con la lectura | — |

Cada caza queda en `areas/ofertas/cazas/AAAA-MM-DD-<nicho>.md`, con una fila en el tablero (`areas/ofertas/README.md`).

## Cómo se testea una oferta nueva

| | Regla | Fuente |
|---|---|---|
| Estructura | Una **CBO**: un conjunto con 5–10 anuncios | «una campaña CBO… un adset… entre cinco a 10 creativos… tanto para testear ofertas» [Bilbao, 24/10/2026] |
| Presupuesto | **2–3 tickets por día**. Con un front de USD 10, son USD 20–30 por día | «vos la podés arrancar tranquilamente en dos, tres tickets» [Bilbao, 11/10/2026] |
| Espera | **3 días sin tocar** | «mínimamente dejarla 3 días correr» [Bilbao, 11/10/2026] |
| Corte | No se apaga anuncio por anuncio. Si no hay ROAS positivo, se suman 5 anuncios más. Con **20–25 anuncios en 5–7 días** sin ROAS positivo, se abandona la oferta | [Bilbao, 13/9/2026] · «hay un costo de oportunidad muy grande de quedarte con una oferta en ROAS 0,90» [Bilbao, 24/10/2026] |
| Tope de pérdida | **USD {{TOPE}} por oferta.** Axel usa USD 200 | Bilbao habló de «no perder más de 100, 150, 200»: ⚠️ viejo (21/6/2026) |
| Backend | El bump va desde el día 1 y el upsell, una vez que la oferta valida. Para escalar, el ticket promedio ÷ front tiene que dar **1,5 o más**, y **2 o más** en mercados grandes | [Bilbao, 17/8/2026] y [Bilbao, 18/10/2026] |
| Producto | **MVP real:** corto, pero entrega todo lo que promete la landing. Si valida, se hace el producto completo y se les manda también a los que ya compraron | [nuestro]. Bilbao valida antes de hacer el producto completo |

| A los 5–7 días | Qué pasa |
|---|---|
| Por encima del equilibrio (`02-ecuacion.md`) | Se escala con `08-testing-y-escalado.md`. En mercados chicos una oferta dura «una, dos semanas» antes de que la clonen: si pega, se va rápido a otros países [Bilbao, 18/10/2026] |
| Cerca del equilibrio | Se ajusta donde cae el embudo: landing, checkout o creativos |
| 20–25 anuncios sin ROAS positivo | Se descarta, se archiva y entra la próxima |
