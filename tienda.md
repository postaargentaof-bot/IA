# Tienda en Impultienda · «La IA hace, vos vendés» (10/11/2026)

- **Tienda nueva (clásica, ARS):** https://la-ia-hace.impultienda.ar · id `e36e2cbd-c356-48a0-85cb-259a02de2282`
- Panel: https://impultienda.ar/dashboard/la-ia-hace/inicio

## Productos (revisado el 10/11)

| Producto | Rol | Precio hoy | id | Estado |
|---|---|---|---|---|
| La IA hace, vos vendés | principal | **16.990 con 84.950 tachado (los dos los puso Impultienda). Va a 7.990 sin tachado: esperando decisión, ver abajo** | `4abc74e9-f00f-4f67-9dee-9116c50c3342` | Sin entregable |
| Fotos de producto con el celular + IA | bump | 4.990, sin tachado | `b9fdc983-7333-42a8-af33-e337a1a72000` | Sin entregable |
| La planilla lista para usar | bump | 3.990, sin tachado | `1ae61a84-4d03-4c6f-914c-9715aa6e46ab` | Sin entregable |
| Las 200 instrucciones | upsell solo post-compra | 12.990, sin tachado | `a34739b2-a354-4260-9ed5-5af5b188889f` | Sin entregable, funnel sin crear |
| Respuestas listas para WhatsApp | bono (inventado) | — | `2ed41ee7-80b2-4ea1-b7c7-0668677204ae` | Borrar en el panel |
| Calendario de publicaciones de 30 días | bono (inventado) | — | `15dbebb7-d05e-4651-a3bd-5eb94b9b1079` | Borrar en el panel |
| Plantillas de presupuestos y precios | bono (inventado) | — | `1312a1bd-d4a2-47e3-8975-4dae1305e527` | Borrar en el panel |

Hoy la tienda **no puede cobrar** (no hay Mercado Pago conectado) y ningún producto tiene entregable: nadie puede comprar.

### El precio tachado del principal

Con la landing de plantilla, Impultienda no deja sacar el tachado (el conector rechaza «sin tachado»: «quedaría 0 tachado»).
Además el checkout muestra el tachado del principal y, en el total, le suma el «valor» de los bonos. No existe pausar la tienda
ni modo mantenimiento (solo «Eliminar tienda», que la archiva). Opciones:

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

## Pendiente

- Decidir cómo se corrige el precio del principal (opciones arriba) y aplicarlo con el «sí» de los dueños.
- Borrar en el panel (Diseño de ebooks) los 3 bonos inventados. El conector no borra ebooks.
- Sacar todo lo de la lista de arriba (o publicar el HTML propio) y revisar Diseño de checkout: garantía, barra de compradores y barra superior.
- Landing: publicar `landing/landing.html` (HTML propio). Todavía tiene los recuadros de las imágenes IMG-xx.
- Entregables: los PDF de `pdf/` tienen los recuadros de las imágenes sin completar; se suben cuando estén las imágenes.
- Funnel post-compra: el modo de Impultienda aplica 15 % de descuento al upsell y suma un downsell con 40 %. A decidir.
- Mercado Pago, píxel de Meta, compra de prueba.
