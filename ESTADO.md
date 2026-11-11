# ESTADO · Ebook «La IA hace, vos vendés»

> Archivo principal del proyecto. **Todo chat lo lee al arrancar y lo actualiza al terminar.**
> Rama de trabajo: `claude/dazzling-euler-7bk40o` (no `main`). Siempre `git pull --rebase` antes de `git push`: hay varios chats subiendo a la misma rama.
> Última actualización: 11/11/2026.

## 1 · Qué estamos haciendo

Testear un ebook propio sobre cómo usar la IA en un emprendimiento, después de que el ebook de jabones, velas y sahumerios (Taller Triple) no funcionó: se gastaron USD 22,71 y salió 1 venta.

**Presupuesto del test:** USD 25 en total. Con eso **no se valida si el producto vende**: se mide qué gancho engancha y si la gente llega al checkout. El criterio para leerlo está en `plan-ebook-ia.md` §3.

## 2 · La oferta (decidida)

| Pieza | Nombre | Precio | Archivo |
|---|---|---|---|
| 11/11 | Mail de contacto de la garantía: `tallertriplearg@gmail.com` (el mismo de Taller Triple / velas) | Lo eligieron los dueños; ya lo leen. Se aceptó que muestre otra marca |
| Principal | La IA hace, vos vendés | ARS 7.990 | `pdf/la-ia-hace-vos-vendes.pdf` (69 págs.) |
| Bump 1 | Fotos de producto con el celular + IA | ARS 4.990 | `pdf/bump-fotos-con-celular-e-ia.pdf` |
| Bump 2 | La planilla lista para usar | ARS 3.990 | `bumps/planilla-de-tu-negocio.xlsx` |
| Upsell post-compra | Las 200 instrucciones | ARS 12.990 | `pdf/las-200-instrucciones.pdf` |

Subtítulo: «Cómo usar la IA en tu emprendimiento en 7 días, aunque no sepas nada de tecnología».
Público: emprendedores y negocios chicos que venden por WhatsApp e Instagram. Herramienta: ChatGPT gratis.

## 3 · Decisiones (la más nueva arriba)

| Fecha | Decisión | Por qué |
|---|---|---|
| 10/11 | En los PDF las imágenes van como copias JPEG livianas (1400 px, calidad 80); las PNG originales quedan en `imagenes/` sin tocar | Con las PNG (~2,2 MB cada una) el ebook pasaba los 15 MB; así pesa 3,3 MB |
| 10/11 | En `landing/landing.html` y `postcompra.html` (versión Impultienda) las fotos ya van como `<img>` con `src="RECURSO:IMG-xx.jpg"`, igual que las tapas (`RECURSO:tapa-ebook.png`). Los archivos a subir a Recursos están en `landing/assets/`. Al subirlos se cargan las direcciones en `imagenes/urls.json` y se vuelve a armar | Las imágenes existen: no tiene sentido dejar recuadros; falta solo la dirección pública |
| 10/11 | La vista previa (`landing/preview/`) usa rutas relativas (`../assets/`) | Antes eran rutas `file://` de la compu donde se armó y no se veían en otra |
| 10/11 | Sin fotos reales del antes y después (FOTO-*): la sección se sacó del bump de fotos. La tarea 3 ya no existe | Ya estaba decidido (commit 5d3ab8c); ESTADO lo seguía listando |
| 10/11 | En la tienda nueva se usa el píxel «velas» (`1439230865058805`) de la cuenta «Velas arg», copiado desde Taller Triple | Es el único píxel de la cuenta y ya tiene token; Taller Triple está cerrada |
| 10/11 | Checkout sin barra de compradores ni reloj en los bumps; barra superior «Pago seguro con Mercado Pago» | Nada de urgencias ni números simulados |
| 10/11 | Garantía de 7 días, sin preguntas: se pide por mail y la devolución se hace a mano desde Mercado Pago. Va en la landing propia, el checkout y el mail de entrega | Lo decidieron los dueños; vuelve a haber un contacto (mail) en la landing |
| 10/11 | Funnel post-compra sin descuentos: upsell a 12.990 y sin downsell | Más simple y el precio cobrado es el de la landing |
| 10/11 | El precio del principal pasa a 7.990 sin tachado recién al publicar el HTML propio de la landing (opción 1 de `tienda.md`); hasta entonces queda 16.990 con 84.950 tachado | La plantilla obliga a tener tachado y no se inventa uno; mientras tanto nadie puede comprar (no hay pasarela) |
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
- Las 20 imágenes con IA (IMG-01…15, 20…22, 30, 31), aprobadas por Toto el 10/11: `imagenes/IMG-XX.png`
- Cómo se regeneran PDF, landing y prompts: `scripts/README-imagenes.md`
- **Tarea 4 (10/11):** PDF y landing rearmados con las 20 imágenes. Sin ningún recuadro IMG-xx ni FOTO-xx en los 3 PDF ni en los 4 HTML. Revisados con capturas (páginas con imágenes, tapas, landing en compu y celular, post-compra): sin imágenes cortadas, deformadas ni tapando texto. Se arregló: la última página del ebook y del bump quedaba con una sola frase suelta, y el subtítulo de la tapa del bump estaba pegado a la línea de abajo. Los mockups de la landing salen ahora de páginas buscadas por texto (las páginas se habían corrido). `[MAIL]` sigue sin completar (lo pasan el 11/11)
- **Peso de los PDF (10/11):** `la-ia-hace-vos-vendes.pdf` 3,3 MB (69 págs.) · `bump-fotos-con-celular-e-ia.pdf` 0,7 MB (14 págs.) · `las-200-instrucciones.pdf` 1,0 MB (68 págs.). Todos lejos de los 15 MB
- Tienda nueva en Impultienda creada (parte de la tarea 6): `la-ia-hace.impultienda.ar`, 4 productos cargados con sus ids. Detalle y pendientes en `tienda.md`
- Mercado Pago conectado en la tienda nueva (11/11, verificado con el conector: «Lista para cobrar»). **Ojo:** desde ahora la tienda puede cobrar, pero sigue con la landing de plantilla (16.990, tachado y testimonios inventados) y sin entregables: hacer la tarea 6 antes de mandar a nadie a la tienda
- **Tarea 6 en curso (11/11):** los 3 PDF cargados como entregables en Impultienda (libro, bump de fotos, 200 instrucciones). 15 fotos + tapas y páginas subidas a Recursos; direcciones en `imagenes/urls.json`, y `landing/landing.html` / `postcompra.html` rearmados con ellas. Vista previa del HTML propio aceptada por Impultienda (sin proveedores bloqueados). **Esperando el «sí» de los dueños** para: publicar la landing, precio 7.990 sin tachado, desactivar los 3 bonos inventados y publicar la página post-compra. **Falta el link de Drive de la planilla** (Impultienda solo acepta PDF como archivo)
- Garantía de 7 días sin preguntas en `landing/landing.html`, con el mail `tallertriplearg@gmail.com` (11/11); no publicada
- Tienda nueva: funnel post-compra creado (upsell 12.990, sin descuento; el downsell quedó en 0 % hasta que los dueños lo borren en el panel), checkout sin barra de compradores ni reloj de bumps, píxel «velas» cargado y verificado. Detalle e ids en `tienda.md`
- Revisión de la landing publicada de la tienda nueva: lista de lo falso o que no es de la oferta (testimonios, garantía, cuenta regresiva, cupos, bonos inventados, precio) en `tienda.md`. No se arregló todavía

## 5 · Falta ⏳ (en orden)

| # | Tarea | Quién | Bloquea a | Notas |
|---|---|---|---|---|
| 1 | Pagar los ~USD 7 pendientes en Meta (cuenta «Velas arg» en período de gracia desde el 9/11) | Dueños | 9 | Meta Business Suite → Facturación y pagos → Pagar ahora. Si falla: habilitar la tarjeta para el exterior o cargar otra. **Lo pagan el 11/11** (ARS ~11.200) |
| 5 | Probar la planilla en Google Sheets (colores y listas) y la instrucción maestra en ChatGPT gratis | Dueños | — | Antes de vender |
| 6 | Terminar la tienda nueva: precio del principal a 7.990 y sacar el tachado inventado (84.950) (**decidido: se hace al publicar el HTML propio, en el mismo paso**), HTML propio de landing y upsell, entregables, funnel post-compra, imágenes en Recursos | Claude, con aprobación | 7 | Tienda y productos ya creados (`tienda.md`). Sumar la garantía con el mail `tallertriplearg@gmail.com` como bloque de texto en el checkout y en el mail de entrega. PDF y HTML listos (tarea 4 hecha): subir a Recursos los archivos de `landing/assets/` (15 fotos IMG-xx.jpg + tapas y páginas .png), cargar sus direcciones en `imagenes/urls.json` y volver a armar con `python3 scripts/armar_landing.py`. Borrar a mano en el panel los 3 bonos que inventó la IA de Impultienda. Revisar que no queden testimonios, contadores ni cupos |
| 6c | Borrar en el panel el downsell del funnel post-compra (está en 0 %), los 3 bonos inventados, y revisar en Diseño de checkout los sellos y que «Días de garantía» diga 7 | Dueños | 6 | Links en `tienda.md` |
| 7 | Compra de prueba + evento Compra visible en el Administrador de eventos | Dueños + Claude | 9 | El píxel ya está cargado y verificado (10/11). Mercado Pago ya está (11/11); espera los entregables (tarea 6) |
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
