# Tienda en Impultienda · «La IA hace, vos vendés» (10/11/2026)

- **Tienda nueva (clásica, ARS):** https://la-ia-hace.impultienda.ar · id `e36e2cbd-c356-48a0-85cb-259a02de2282`
- Panel: https://impultienda.ar/dashboard/la-ia-hace/inicio

## Productos (revisado el 10/11)

| Producto | Rol | Precio hoy | id | Estado |
|---|---|---|---|---|
| La IA hace, vos vendés | principal | **16.990 con 84.950 tachado (los dos los puso Impultienda). Va a 7.990 sin tachado al publicar el HTML propio (decidido 10/11)** | `4abc74e9-f00f-4f67-9dee-9116c50c3342` | Sin entregable |
| Fotos de producto con el celular + IA | bump | 4.990, sin tachado | `b9fdc983-7333-42a8-af33-e337a1a72000` | Sin entregable |
| La planilla lista para usar | bump | 3.990, sin tachado | `1ae61a84-4d03-4c6f-914c-9715aa6e46ab` | Sin entregable |
| Las 200 instrucciones | upsell solo post-compra | 12.990, sin tachado | `a34739b2-a354-4260-9ed5-5af5b188889f` | Sin entregable. En el funnel post-compra (abajo) |
| Respuestas listas para WhatsApp | bono (inventado) | — | `2ed41ee7-80b2-4ea1-b7c7-0668677204ae` | Borrar en el panel |
| Calendario de publicaciones de 30 días | bono (inventado) | — | `15dbebb7-d05e-4651-a3bd-5eb94b9b1079` | Borrar en el panel |
| Plantillas de presupuestos y precios | bono (inventado) | — | `1312a1bd-d4a2-47e3-8975-4dae1305e527` | Borrar en el panel |

**11/11: Mercado Pago conectado** (verificado: «Lista para cobrar»). La tienda ya puede cobrar, pero ningún producto tiene entregable y la landing sigue siendo la plantilla: no mandar a nadie hasta terminar la tarea 6.

### El precio tachado del principal

Con la landing de plantilla, Impultienda no deja sacar el tachado (el conector rechaza «sin tachado»: «quedaría 0 tachado»).
Además el checkout muestra el tachado del principal y, en el total, le suma el «valor» de los bonos. No existe pausar la tienda
ni modo mantenimiento (solo «Eliminar tienda», que la archiva). Opciones (**elegida el 10/11: la 1**):

1. **Esperar y cambiar el precio cuando se publique el HTML propio** (`landing/landing.html`). Con HTML propio la regla del
   tachado obligatorio no aplica; ahí se pone 7.990 sin tachado. Mientras tanto nadie puede comprar (no hay pasarela).
2. **Publicar ya el HTML propio**, con los recuadros de imágenes vacíos, y en seguida 7.990 sin tachado.
3. **7.990 ya, con un tachado cargado pero oculto con CSS** en la landing. No sirve del todo: el checkout lo sigue mostrando.
4. **Archivar la tienda** hasta que esté lista. Exagerado: libera el subdominio y hay que restaurarla a mano.

## Lo falso o que no está en nuestra oferta en la landing publicada (no arreglado todavía)

Leído con el conector (textos de la plantilla). La página en vivo no se pudo abrir desde esta sesión (la red la bloquea):
lo marcado con (*) es lo que la plantilla muestra de entrada según la documentación de Impultienda; hay que confirmarlo mirando la tienda.

**Testimonios y prueba social**
- Sección «Prueba social» titulada «opiniones reales de compradores», con 3 testimonios inventados: «Lucía Fernández», «Martín Rodríguez» y «Camila Sosa». No hay compradores todavía.
- (*) Estrellas con texto de ventas debajo del título del hero.
- (*) «Notificación de venta» flotante (avisos de compras que no existen).

**Contadores, cupos y urgencias**
- (*) Barra de anuncio con el texto de «oferta limitada» 🔥 y cuenta regresiva.
- (*) Bloque «Oferta termina en» con reloj en el hero y en la barra fija de abajo (los apaga el mismo interruptor «Mostrar cuenta regresiva»).
- (*) Bloque de cupos en el hero: si no tiene número muestra «7 cupos». No se apaga desde el panel: hace falta CSS.
- (*) Etiqueta roja de urgencia arriba del precio del hero.
- Checkout: sin bloques de cuenta regresiva ni de cupos (revisado). Falta mirar en Diseño de checkout la «Barra de compradores» y la «Barra superior».
- Downsell pre-compra: no configurado (bien).

**Precios y bonos que no existen**
- Precio 16.990 con 84.950 tachado y la línea de «ahorro» calculada con eso.
- 3 bonos que no son de nuestra oferta, con su «valor» tachado y el cartel de «gratis» (sección de bonos y lista del hero). Su valor también sube el tachado del total en el checkout.
- Los 2 bumps y el upsell ya tienen nuestros nombres y precios.

**Promesas que no hacemos**
- «Garantía de 7 días»: «Si comprás y no te sirve, devolvemos tu dinero dentro de los 7 días». No decidimos ninguna devolución. Mirar también «Mostrar garantía» en Diseño de checkout.
- Título del hero: «Pasá de “no llego” a vender todos los días con ayuda de la IA». Promete ventas; nosotros no prometemos ventas.
- Botón del hero «Quiero que la IA labure por mí»: la IA no labura sola, vos revisás todo.
- FAQ: «lo adaptás a tu caso en minutos»: el libro es una hora por día.

**Otros**
- Pie: «© 2026 Nombre. Todos los derechos reservados.» (nombre sin completar).

Casi todo esto desaparece al publicar el HTML propio (`landing/landing.html`), salvo lo del checkout (garantía, barras, tachado y bonos), que depende de los productos y de Diseño de checkout.

## Revisión del 10/11 (tarde): lo que NO depende de las imágenes

### Hecho en el repo
- `landing/landing.html` (y `landing/preview/`): garantía de 7 días sin preguntas en «Lo que tenés que saber», en la FAQ
  («¿Y si no me sirve?») y en la nota del botón final. El mail es **tallertriplearg@gmail.com** (11/11), en `MAIL` de
  `scripts/armar_landing.py` y se vuelve a armar (`python3 scripts/armar_landing.py`). No se publicó.
- `landing/postcompra.html`: el texto está bien (sin descuentos ni urgencias, botones `data-pp-accept` / `data-pp-decline`,
  precio con `{price}`). **No se sube todavía:** tiene el recuadro de IMG-31 y la tapa como `RECURSO:tapa-200.png`, que hay
  que subir a Recursos. Mientras tanto la oferta usa la plantilla de Impultienda con el nombre y la descripción del producto.

### Leído (sin escribir)
- **Mercado Pago:** no conectado; es la única pasarela compatible con la tienda en ARS. Se conecta con el botón de Mercado
  Pago (inicio de sesión de Mercado Pago, sin pegar credenciales) en https://impultienda.ar/dashboard/la-ia-hace/configuracion?tab=pagos
- **Píxel:** la tienda no tiene. La cuenta «Velas arg» (1611303950747523) tiene un solo píxel: «velas» `1439230865058805`
  (activo, último evento 9/11), que ya está cargado con su token de conversiones en Taller Triple. Se puede copiar a esta
  tienda con su token sin tocar nada en Meta. Las compras de las dos tiendas caerían en el mismo píxel (Taller Triple está cerrada).
- **Checkout:** sin bloques arriba ni abajo. El conector no lee el resto del diseño, así que lo que sigue se aplica a ciegas
  y la respuesta devuelve el valor anterior. Los textos de los sellos (incluida la garantía) son fijos: el sello dice la
  garantía con sus días, y la frase «sin preguntas» con el mail solo se puede agregar como bloque de texto.
- **Funnel post-compra:** no existe. El conector lo crea con 15 % al upsell y un downsell con 40 %; el descuento se puede
  poner en 0 %, pero el downsell **no se borra desde el conector**: se borra en el panel (tacho de su tarjeta).

### Aplicado en Impultienda con el «sí» de los dueños (10/11)
1. **Funnel post-compra «Las 200 instrucciones»** (`e60d55c4-4d41-4c1d-855f-de97ba191121`), ACTIVO, «Disparar siempre».
   - Upsell (oferta `624d1055-8a29-47ce-9471-45c5a43d9b97`): 0 % → ARS 12.990.
   - Downsell (oferta `07de2e4b-2ccf-4c09-a124-3f2a0003704f`): 0 % → ARS 12.990. **Lo borran los dueños en el panel**
     (tacho de su tarjeta): https://impultienda.ar/dashboard/la-ia-hace/marketing/post-compra/e60d55c4-4d41-4c1d-855f-de97ba191121?tab=upsells
   - Página: la plantilla de Impultienda con el nombre y la descripción del producto, hasta subir `landing/postcompra.html`.
2. **Checkout:** barra de compradores oculta; timer del bloque de bumps en 0 (oculto; antes: automático); barra superior con
   «Pago seguro con Mercado Pago» (antes: la de siempre). Sellos: se pidió «Clásico» y quedó en «automático» (no se pudo
   confirmar que sea el mismo): **revisar en Diseño de checkout** que no aparezca el sello «Contenido aprobado · Oficialmente».
3. **Píxel «velas» `1439230865058805`** copiado desde Taller Triple con su token. Impultienda verificó que carga en la tienda
   publicada y que Meta acepta el token. En Meta no se tocó nada.

## Pendiente

- Precio del principal: en el mismo paso en que se publique el HTML propio, pasar a 7.990 sin tachado (con el «sí» de los dueños).
- Borrar en el panel (Diseño de ebooks) los 3 bonos inventados. El conector no borra ebooks.
- Sacar todo lo de la lista de arriba (o publicar el HTML propio) y revisar Diseño de checkout: garantía, barra de compradores y barra superior.
- Landing: publicar `landing/landing.html` (HTML propio). Ya tiene las imágenes (10/11), con `src="RECURSO:<archivo>"`: subir a Recursos los archivos de `landing/assets/`, cargar las direcciones en `imagenes/urls.json` y volver a armar.
- Entregables: los PDF de `pdf/` ya están completos con las imágenes (10/11); falta subirlos.
- Funnel post-compra: decidido sin descuento y sin downsell (10/11). Ver «Propuesto» arriba.
- Mercado Pago (lo conectan los dueños, link arriba), píxel (propuesto arriba), compra de prueba.
- Mail de la garantía: `tallertriplearg@gmail.com` (ya en la landing, 11/11). Falta sumar un bloque de texto con la garantía al checkout y revisar el mail de entrega.
- Revisar en el panel (Diseño de checkout) que «Días de garantía» diga 7.

## 11/11 · Tarea 6 aplicada (con el «sí» de los dueños)

- Entregables: PDF cargados y confirmados en «La IA hace, vos vendés» (3,1 MB), «Fotos de producto con el celular + IA» (0,7 MB) y «Las 200 instrucciones» (0,9 MB).
- **Falta la planilla**: Impultienda solo acepta PDF como archivo; necesita un link público de Drive (lo pasan los dueños).
- Recursos: 15 fotos (IMG-xx.jpg) + tapa-ebook, tapa-200 y 3 páginas del libro. Direcciones en `imagenes/urls.json`.
- Landing: HTML propio publicado (era la plantilla; Impultienda dice que no guardó versión anterior porque no había HTML propio, la plantilla sigue en el panel).
- Precio del principal: 7.990 sin tachado (antes 16.990 / 84.950).
- Post-compra: HTML propio guardado en la oferta `624d1055-…` y modo HTML prendido.
- **No se pudo:** desactivar los 3 bonos inventados (el conector no lo permite en tiendas clásicas). Siguen pendientes de borrar en el panel, junto con el downsell `07de2e4b-…`.
- Falta: bloque de texto de la garantía en el checkout, revisar el mail de entrega, compra de prueba.

## 11/11 · Cierre de la tarea 6 (segunda sesión)

- **Checkout:** bloque de texto debajo del botón de pagar (con el «sí» de los dueños): «Garantía de 7 días, sin preguntas: si no te sirve, escribinos a tallertriplearg@gmail.com dentro de los 7 días desde la compra y te devolvemos la plata.» Antes no había bloques.
- **Mail de entrega:** no se puede editar en Impultienda (no hay campo para el asunto ni para el cuerpo). Al pie muestra el email de contacto de la tienda; se ofreció cambiarlo a `tallertriplearg@gmail.com` y no se aprobó.
- **Verificado con el conector:** landing con HTML propio (23.055 caracteres, igual a `landing/landing.html`); principal 7.990 sin tachado; oferta post-compra `624d1055-…` con HTML propio y modo HTML prendido; PDF cargados en el libro, el bump de fotos y Las 200 instrucciones.
- **Diagnóstico:** puede cobrar y listo para anunciar. Advertencia: 4 de 7 ebooks sin entregable (planilla + 3 bonos inventados).
- **Planilla:** link de Google Sheets que pasaron los dueños: `https://docs.google.com/spreadsheets/d/1GT_vbcGeA4MZggf-DmbHiSuA2XI8920jEMPbOEASzY4/` — **cargado el 11/11** (con el «sí») como `…/copy`: cada comprador se hace su propia copia. Compartido como Lector.
- **Tienda en vivo:** no se pudo abrir desde la sesión. Se sumaron `la-ia-hace.impultienda.ar` y `challenges.cloudflare.com` a la red del entorno, pero Cloudflare frena al navegador automático («Un momento…»). Se miró el mismo HTML con las imágenes reales de Recursos, en compu y celular: ninguna imagen rota, nada se sale de la pantalla, sin testimonios, relojes, cupos ni tachado. El checkout con los 2 bumps lo tienen que mirar los dueños.

### Recursos (direcciones públicas)

Base: `https://aekpgsbqjzqntlbucbts.supabase.co/storage/v1/object/public/store-resources/e36e2cbd-c356-48a0-85cb-259a02de2282/`. La lista completa archivo → dirección está en `imagenes/urls.json` (15 fotos IMG-xx.jpg, tapa-ebook.png, tapa-200.png, pagina-ficha.png, pagina-whatsapp.png, pagina-numeros.png).

### Qué falta para la compra de prueba

1. ~~Cargar la planilla~~ (hecho 11/11). En la compra de prueba, abrir el link de la planilla sin sesión de Google para confirmar que copia bien.
2. ~~Borrar los 3 bonos inventados y el downsell~~ (hecho por los dueños el 11/11; verificado: 4 productos, funnel con una sola oferta, Diagnóstico sin errores ni advertencias). En Diseño de checkout, revisar los sellos, «Días de garantía» = 7 y el bloque de la garantía.
3. Dueños: abrir la tienda en compu y celular y el checkout con los 2 bumps; «Enviar mail de prueba» en Emails al comprador para ver qué PDF baja cada producto.

## 11/11 · Landing y upsell rediseñados (estilo «chat»)

- Los dueños eligieron la propuesta C de `landing/propuestas/` (A cuaderno, B revista, C chat).
- Publicado con su «sí»: `landing/landing.html` como landing (23 → 25 KB) y `landing/postcompra.html` en la oferta `624d1055-…` (11 → 13 KB, modo HTML prendido). Vistas previas sin proveedores bloqueados ni avisos. **Las versiones anteriores quedaron guardadas** (landing: `impultienda_restaurar_html`; upsell: `restaurar_version_anterior`).
- Mismos textos, FAQ completa, garantía con el mail, imágenes de Recursos. El ejemplo del teléfono (Caro, buzo a $18.500) está rotulado «Ejemplo».
- Los dueños miraron la tienda publicada (11/11): se ve bien. Lo que sigue es la compra de prueba.

## Precio de prueba (12/11)
- Principal pasado a **ARS 1.000** para la compra de prueba (pedido de los dueños). Antes estaba en **9.990** (no 7.990: alguien lo cambió en el panel y no quedó anotado). Volver al precio decidido después de la prueba.
