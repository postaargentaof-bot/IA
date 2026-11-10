# ESTADO · Ebook «La IA hace, vos vendés»

> Archivo principal del proyecto. **Todo chat lo lee al arrancar y lo actualiza al terminar.**
> Rama de trabajo: `claude/dazzling-euler-7bk40o` (no `main`). Siempre `git pull --rebase` antes de `git push`: hay varios chats subiendo a la misma rama.
> Última actualización: 10/11/2026.

## 1 · Qué estamos haciendo

Testear un ebook propio sobre cómo usar la IA en un emprendimiento, después de que el ebook de jabones, velas y sahumerios (Taller Triple) no funcionó: se gastaron USD 22,71 y salió 1 venta.

**Presupuesto del test:** USD 25 en total. Con eso **no se valida si el producto vende**: se mide qué gancho engancha y si la gente llega al checkout. El criterio para leerlo está en `plan-ebook-ia.md` §3.

## 2 · La oferta (decidida)

| Pieza | Nombre | Precio | Archivo |
|---|---|---|---|
| Principal | La IA hace, vos vendés | ARS 7.990 | `pdf/la-ia-hace-vos-vendes.pdf` (71 págs.) |
| Bump 1 | Fotos de producto con el celular + IA | ARS 4.990 | `pdf/bump-fotos-con-celular-e-ia.pdf` |
| Bump 2 | La planilla lista para usar | ARS 3.990 | `bumps/planilla-de-tu-negocio.xlsx` |
| Upsell post-compra | Las 200 instrucciones | ARS 12.990 | `pdf/las-200-instrucciones.pdf` |

Subtítulo: «Cómo usar la IA en tu emprendimiento en 7 días, aunque no sepas nada de tecnología».
Público: emprendedores y negocios chicos que venden por WhatsApp e Instagram. Herramienta: ChatGPT gratis.

## 3 · Decisiones (la más nueva arriba)

| Fecha | Decisión | Por qué |
|---|---|---|
| 10/11 | Diseño de PDF y landing con lugares para imágenes de IA (IMG-01…31); se generan después | Que quede lindo sin frenar el resto |
| 10/11 | Sin versión para el celular (PDF A5, que se lee bien en el celular) | No estaba hecha |
| 10/11 | Pago con Mercado Pago; sin preguntas de devolución ni de contacto en la landing | Decisión de los dueños |
| 10/11 | 2 bumps (fotos + planilla), no 3 | Un checkout largo en el celular cuesta ventas |
| 10/11 | Upsell = 200 instrucciones para cualquier rubro + instrucción maestra; nada «por rubro» | Si alguien no ve su rubro, no compra |
| 10/11 | El ebook lo escribimos nosotros, no la IA de Impultienda | Más fiel al índice y no gasta cupo |
| 10/11 | Ejemplos con 4 negocios armados: Caro (ropa, Lanús), Mati (pastelería, Morón), Sol (uñas, Rosario), Fede (entrenador, Córdoba) | Cubren producto, comida, turnos y clases |
| 10/11 | Precio de test ARS 7.990 | Con poco tráfico, más chances de ver ventas |
| 10/11 | Taller Triple cerrado; campaña «TT · Ventas · CBO» pausada | Lo decidieron los dueños |

## 4 · Hecho ✅

- Ebook completo: `ebook/` (texto) → `pdf/la-ia-hace-vos-vendes.pdf`
- Bump de fotos: `bumps/fotos-con-celular-e-ia.md` → PDF
- Bump planilla: `bumps/planilla-de-tu-negocio.xlsx` (1.024 fórmulas, sin errores; probada con el ejemplo de Mati)
- Upsell: `upsell/` → PDF. Instrucción maestra probada con la ficha de Sol: `upsell/prueba-instruccion-maestra-sol.md`
- Textos de la landing y el checkout: `landing/textos.md` (los escribió el chat «landing»)
- Landing con diseño (HTML propio para Impultienda): `landing/landing.html` + upsell post-compra `landing/postcompra.html`. Vista previa: `landing/preview/`
- 3 anuncios con imágenes y textos: `anuncios/anuncios.md` + `anuncios/img/`
- Lista de prompts de imágenes: `imagenes/prompts.md`
- Cómo se regeneran PDF, landing y prompts: `scripts/README-imagenes.md`
- Tienda nueva en Impultienda creada (parte de la tarea 6): `la-ia-hace.impultienda.ar`, 4 productos cargados con sus ids. Detalle y pendientes en `tienda.md`
- Revisión de la landing publicada de la tienda nueva: lista de lo falso o que no es de la oferta (testimonios, garantía, cuenta regresiva, cupos, bonos inventados, precio) en `tienda.md`. No se arregló todavía

## 5 · Falta ⏳ (en orden)

| # | Tarea | Quién | Bloquea a | Notas |
|---|---|---|---|---|
| 1 | Pagar los ~USD 7 pendientes en Meta (cuenta «Velas arg» en período de gracia desde el 9/11) | Dueños | 9 | Meta Business Suite → Facturación y pagos → Pagar ahora. Si falla: habilitar la tarjeta para el exterior o cargar otra |
| 2 | Generar las 20 imágenes con IA y guardarlas en `imagenes/IMG-XX.png` | Dueños | 4 | Prompts en `imagenes/prompts.md` |
| 4 | Volver a armar los PDF y la landing con las imágenes | Claude | 6 | `scripts/README-imagenes.md` |
| 5 | Probar la planilla en Google Sheets (colores y listas) y la instrucción maestra en ChatGPT gratis | Dueños | — | Antes de vender |
| 6 | Terminar la tienda nueva: precio del principal a 7.990 y sacar el tachado inventado (84.950) (**la plantilla obliga a tener tachado: opciones en `tienda.md`, esperando a los dueños**), HTML propio de landing y upsell, entregables, funnel post-compra, imágenes en Recursos | Claude, con aprobación | 7 | Tienda y productos ya creados (`tienda.md`). Entregables y HTML final esperan a la 4. Borrar a mano en el panel los 3 bonos que inventó la IA de Impultienda. Revisar que no queden testimonios, contadores ni cupos |
| 6b | Decidir el funnel post-compra: Impultienda pone 15 % de descuento al upsell y suma un downsell con 40 % | Dueños | 6 | Ver `tienda.md` |
| 7 | Píxel de Meta en la tienda nueva + compra de prueba + evento Compra visible en el Administrador de eventos | Dueños + Claude | 9 | |
| 8 | Leer todo (ebook, bumps, upsell, landing) y marcar cambios | Dueños | — | Se puede hacer en paralelo |
| 9 | Crear la campaña en Meta y prenderla | Claude, con el «sí» de los dueños | 10 | Estructura en `anuncios/anuncios.md` |
| 10 | Leer el test con el criterio de `plan-ebook-ia.md` y decidir | Chat principal | — | Las ventas se cuentan en Impultienda, no en Meta |

## 6 · Datos útiles

- Impultienda: tienda nueva «La IA hace» (`e36e2cbd-c356-48a0-85cb-259a02de2282`, `la-ia-hace.impultienda.ar`). Tienda vieja «Taller Triple» (`2839f946-6210-4e03-a620-44aa105606b1`), plan Max, ARS, Mercado Pago — no usar para esto.
- Meta: cuenta publicitaria «Velas arg» (`1611303950747523`), en USD.
- La carpeta del kit (`kit-ebooks-cortex.zip`, `EMPEZA-ACA.md`) está sin instalar; se puede instalar más adelante.

## 7 · Reglas de juego

1. **Meta:** Claude lee siempre y cambia algo solo con el «sí» de los dueños en ese momento.
2. **Impultienda:** cada escritura pide aprobación.
3. **Gasto antes de generar:** antes de gastar créditos o cupo (imágenes, generación de ebooks), se pasa la cuenta y se espera el OK.
4. **Nada falso:** ni testimonios, ni contadores, ni urgencias inventadas. Las personas de las imágenes ilustran ejemplos, no son clientes.
5. **Un chat, una tarea.** Cada chat toca solo su área, deja el resultado en el repo y actualiza este archivo.
6. **Las ventas se cuentan en Impultienda.**
