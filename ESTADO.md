# ESTADO · Ebook «La IA hace, vos vendés»

> Archivo principal del proyecto. **Todo chat lo lee al arrancar y lo actualiza al terminar.**
> Rama de trabajo: `claude/dazzling-euler-7bk40o` (no `main`). Siempre `git pull --rebase` antes de `git push`: hay varios chats subiendo a la misma rama.
> Última actualización: 11/11/2026 (chat de producción de creativos: tarea 8b hecha).

## 1 · Qué estamos haciendo

Testear un ebook propio sobre cómo usar la IA en un emprendimiento, después de que el ebook de jabones, velas y sahumerios (Taller Triple) no funcionó: se gastaron USD 22,71 y salió 1 venta.

**Presupuesto del test:** USD 25 en total. Con eso **no se valida si el producto vende**: se mide qué gancho engancha y si la gente llega al checkout. El criterio para leerlo está en `plan-ebook-ia.md` §3.

## 2 · La oferta (decidida)

| Pieza | Nombre | Precio | Archivo |
|---|---|---|---|
| 11/11 | Creativos del lanzamiento: los 5 de `anuncios/ideas.md` (A video «¿Precio?», B carrusel «Así es tu semana» con páginas reales, C imagen «No suena a vos», D persona IA «Sol», E solo texto «El audio»). Los 3 anuncios viejos de `anuncios/` quedan descartados. Todas las piezas en 4:5 y 9:16, hechas con IA (sin personas reales). La producción va en un chat aparte | Análisis del test de Taller Triple: 5 videos parecidos, 63 % del gasto en vertical y retención de 5–6 s (detalle en `anuncios/ideas.md`) |
| 11/11 | Los anuncios del ebook de IA salen de una página nueva de Facebook e Instagram, «La IA hace, vos vendés» (la crean los dueños). Propuesta para la campaña: botón «Comprar», título en todos y sin Audience Network | La de velas desconcierta; en Taller Triple, Audience Network trajo clics que no llegaban a la landing |
| 11/11 | Diseño de la landing y la página del upsell: estilo «chat» (propuesta C de `landing/propuestas/`), publicado. Mismos textos, FAQ completa | A los dueños no les gustaba el diseño anterior (se veía como «landing hecha con IA»); eligieron entre 3 propuestas |
| 11/11 | La planilla se entrega con un link de Google Sheets terminado en `/copy`, compartido como Lector (Impultienda solo acepta PDF como archivo) | No hay otra forma de entregar un .xlsx |
| 11/11 | El mail de entrega no se edita en Impultienda (no hay campo): la garantía va en la landing y en un bloque de texto debajo del botón de pagar del checkout. El email de contacto de la tienda (pie del mail) no se tocó | Limitación de Impultienda; el cambio del email de contacto no se aprobó |
| 11/11 | Los 3 bonos inventados no se pueden desactivar desde el conector (en tiendas clásicas no se puede): los borran los dueños en el panel | Limitación de Impultienda |
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
| 11/11 | Los 5 creativos (versión 2) aprobados por los dueños como **listos para testear**: los vieron y escucharon con sonido (voz, acento y música) y no encontraron errores | Revisión de los dueños; Claude no puede escuchar el audio |
| 11/11 | Versión 2 de los creativos: A y D animados con código (subtítulos karaoke, movimiento todo el tiempo), con música y efectos generados por código; D con estética propia (Sol de fondo, ciruela y rosa); B con gancho de dolor y resultados «Así queda»; C con respuesta genérica realista; E en amarillo | Lo pidieron los dueños después de la autocrítica (A y D se parecían y eran diapositivas). La música es propia porque la red de este entorno bloquea los bancos de música CC0 |
| 11/11 | Los 5 creativos producidos: A y D en video con voz de ElevenLabs (A, mujer rioplatense; D, varón, para que no parezca que habla Sol), B carrusel de 6 tarjetas con páginas reales del PDF, C antes/después con el ejemplo de Caro, E solo texto. Todo en 4:5 y 9:16. Sin música | Lo pedido en `anuncios/ideas.md`; las voces las eligieron los dueños entre 7 muestras. No había música CC0 a mano |
| 11/11 | En el lanzamiento van solo los 5; los 2 ganchos alternativos de A quedan hechos en `anuncios/img/reserva/` para renovar | Regla 70/30 y «un gancho nuevo, el cuerpo igual» del kit |
| 11/11 | Los videos no dicen el precio del libro ni fechas; el precio ($7.990) va solo en el texto del anuncio | Regla 07-creativos del kit: el video sirve aunque cambie el precio |
| 11/11 | 5 anuncios para el lanzamiento: los 3 de `anuncios/` mejorados (tapa real, fotos, 9:16) + 1 video con voz (ElevenLabs, sin precio en el video) + 1 solo texto. Todo en un conjunto, una CBO | Bilbao (vía el kit, oct. 2026): 5–10 anuncios con formatos distintos; con USD 25, más anuncios no llegan a gastar |
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
- ~~3 anuncios con imágenes y textos~~ (descartados el 11/11; los reemplazan los 5 de `anuncios/ideas.md`; las imágenes viejas se borraron)
- **Tarea 8b (11/11): los 5 creativos producidos.** Piezas en `anuncios/img/` (`ia1-precio` video, `ia2-semana-1…6` carrusel, `ia3-nosuena`, `ia4-sol` video, `ia5-audio`; cada una en 4:5 y 9:16), textos y estructura de campaña en `anuncios/anuncios.md`, guiones en `anuncios/guiones.md`, 2 ganchos de reserva de A en `anuncios/img/reserva/`. Videos: 18,6 s y 21,3 s, −14 LUFS, menos de 5 MB, texto entre los 290 y los 1.290 px. **Versión 2 (11/11): animados con código, con música y efectos propios** (`anuncios/src/video2/`, `./scripts/armar_videos2.sh`). Voces guardadas en ElevenLabs y en `anuncios/audio/` (rearmar no gasta). Revisados con capturas, también a tamaño de celular
- Análisis de errores del test de Taller Triple y 14 ideas de anuncios, con los 5 elegidos y por qué se descartó el resto: `anuncios/ideas.md` (11/11, chat de creativos, fase 1)
- Lista de prompts de imágenes: `imagenes/prompts.md`
- Las 20 imágenes con IA (IMG-01…15, 20…22, 30, 31), aprobadas por Toto el 10/11: `imagenes/IMG-XX.png`
- Cómo se regeneran PDF, landing y prompts: `scripts/README-imagenes.md`
- **Tarea 4 (10/11):** PDF y landing rearmados con las 20 imágenes. Sin ningún recuadro IMG-xx ni FOTO-xx en los 3 PDF ni en los 4 HTML. Revisados con capturas (páginas con imágenes, tapas, landing en compu y celular, post-compra): sin imágenes cortadas, deformadas ni tapando texto. Se arregló: la última página del ebook y del bump quedaba con una sola frase suelta, y el subtítulo de la tapa del bump estaba pegado a la línea de abajo. Los mockups de la landing salen ahora de páginas buscadas por texto (las páginas se habían corrido). `[MAIL]` sigue sin completar (lo pasan el 11/11)
- **Peso de los PDF (10/11):** `la-ia-hace-vos-vendes.pdf` 3,3 MB (69 págs.) · `bump-fotos-con-celular-e-ia.pdf` 0,7 MB (14 págs.) · `las-200-instrucciones.pdf` 1,0 MB (68 págs.). Todos lejos de los 15 MB
- Tienda nueva en Impultienda creada (parte de la tarea 6): `la-ia-hace.impultienda.ar`, 4 productos cargados con sus ids. Detalle y pendientes en `tienda.md`
- Mercado Pago conectado en la tienda nueva (11/11, verificado con el conector: «Lista para cobrar»). **Ojo:** desde ahora la tienda puede cobrar, pero sigue con la landing de plantilla (16.990, tachado y testimonios inventados) y sin entregables: hacer la tarea 6 antes de mandar a nadie a la tienda
- **Tarea 6 (11/11), con el «sí» de los dueños:** los 3 PDF cargados como entregables (libro, bump de fotos, 200 instrucciones). Fotos y tapas en Recursos (direcciones en `imagenes/urls.json`). **Landing propia publicada** (`landing/landing.html`). **Precio del libro: 7.990 sin tachado** (antes 16.990 con 84.950). **Página propia de la oferta post-compra guardada y prendida** (`landing/postcompra.html`). No se pudo mirar la tienda en vivo desde acá (la red la bloquea): la tienen que abrir los dueños
- Garantía de 7 días sin preguntas con el mail `tallertriplearg@gmail.com`: publicada en la landing y, desde el 11/11, como bloque de texto debajo del botón de pagar del checkout
- Planilla cargada como entregable (11/11, con el «sí» de los dueños): link de Google Sheets con `/copy` (cada comprador se hace su copia; el original está compartido como Lector). Con eso la tarea 6 queda hecha; lo que sigue es la 6c de los dueños
- **Landing y página del upsell rediseñadas (11/11, estilo «chat», con el «sí» de los dueños):** publicadas en Impultienda; las versiones anteriores quedaron guardadas para restaurar. Se arman con `python3 scripts/armar_landing.py`; capturas en `landing/preview/captura-*.png`. Las 3 propuestas de diseño quedan en `landing/propuestas/`. Los dueños miraron la tienda publicada el 11/11: se ve bien
- Bonos inventados y downsell borrados por los dueños en el panel (11/11, verificado con el conector): quedan 4 productos (principal, 2 bumps, upsell) y el funnel con una sola oferta (si rechaza, va al agradecimiento). Diagnóstico: sin errores ni advertencias; próximo paso, la compra de prueba
- Diagnóstico de Impultienda (11/11, antes del borrado): «Puede cobrar» y «Listo para anunciar» en sí. Única advertencia: 4 de 7 ebooks sin entregable (la planilla, ya cargada después, y los 3 bonos inventados)
- Tienda nueva: funnel post-compra creado (upsell 12.990, sin descuento; el downsell quedó en 0 % hasta que los dueños lo borren en el panel), checkout sin barra de compradores ni reloj de bumps, píxel «velas» cargado y verificado. Detalle e ids en `tienda.md`
- Revisión de la landing de plantilla (10/11): lo falso que tenía (testimonios, cuenta regresiva, cupos, tachado) quedó afuera al publicar el HTML propio el 11/11. Los 3 bonos inventados se borraron el 11/11

## 5 · Falta ⏳ (en orden)

| # | Tarea | Quién | Bloquea a | Notas |
|---|---|---|---|---|
| 1 | Pagar los ~USD 7 pendientes en Meta (cuenta «Velas arg» en período de gracia desde el 9/11) | Dueños | 9 | Meta Business Suite → Facturación y pagos → Pagar ahora. Si falla: habilitar la tarjeta para el exterior o cargar otra. **Lo pagan el 11/11** (ARS ~11.200) |
| 5 | Probar la planilla en Google Sheets (colores y listas) y la instrucción maestra en ChatGPT gratis | Dueños | — | Antes de vender |
| 6c | En Diseño de checkout: revisar los sellos, que «Días de garantía» diga 7 y cómo se ve el bloque de la garantía. Mirar la tienda en compu y celular y el checkout con los 2 bumps | Dueños | 7 | Los bonos y el downsell ya se borraron (11/11) |
| 7 | Compra de prueba + evento Compra visible en el Administrador de eventos | Dueños + Claude | 9 | El píxel ya está cargado y verificado (10/11). Mercado Pago ya está (11/11); sin bloqueos en el Diagnóstico desde el 11/11; antes, la revisión de la 6c. La tienda en vivo no se puede abrir desde las sesiones de Claude (Cloudflare frena el navegador automático): la miran los dueños |
| 8 | Leer todo (ebook, bumps, upsell, landing) y marcar cambios | Dueños | — | Se puede hacer en paralelo |
| 8c | Instagram de la página nueva: crear la cuenta profesional y conectarla a la página. Opcional: sumar la página al portfolio «Ecom Manu» y a «Velas arg» | Dueños | — | La página de Facebook ya existe (12/11, `1492900110562845`) y se puede usar en anuncios. Sin Instagram, los anuncios de IG salen con el nombre de la página de Facebook. Datos en `pagina-meta/datos.md` |
| 9 | Crear la campaña en Meta y prenderla | Claude, con el «sí» de los dueños | 10 | Estructura, textos y qué archivo va en cada ubicación en `anuncios/anuncios.md`. Creativos aprobados el 11/11, también con sonido. Marcar que las imágenes y las voces son hechas con IA |
| 10 | Leer el test con el criterio de `plan-ebook-ia.md` y decidir | Chat principal | — | Las ventas se cuentan en Impultienda, no en Meta |

## 6 · Datos útiles

- **Vencimientos (revisado 12/11):** Impultienda plan Max en prueba gratis hasta el **21/12/2026** (después cobra; comisión 2 % por venta). ElevenLabs: el chat «Creativos tanda 1» (Taller Triple) dejó anotado cancelarlo antes del **6/12** si no se usa más.
- Meta 12/11: «Velas arg» sigue en período de gracia (deuda sin pagar). Página nueva «La IA hace, vos vendés» `1492900110562845` (con permiso para anunciar; todavía sin Instagram).

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
