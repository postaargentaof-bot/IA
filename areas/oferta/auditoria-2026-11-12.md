# Auditoría completa antes de pautar · 12/11/2026

> Hecha por Claude con los datos reales de Impultienda y de Meta, leídos el 12/11/2026. Los números de Meta y de ventas se vuelven a leer frescos antes de cada decisión: no se copian como permanentes.
>
> **Oferta auditada:** «La IA hace, vos vendés» (tienda `la-ia-hace.impultienda.ar`).
> **También se miró:** «Taller Triple», porque comparte la cuenta de Meta y el píxel, y es la única fuente de datos reales de pauta.

> **Actualización (12/11, más tarde):** esta auditoría se hizo sin ver la rama del otro chat. Los dueños ya habían decidido 4 de los puntos, y esas decisiones mandan (`ESTADO.md`):
> - para el test se usa el píxel «velas»; el píxel propio va si se escala;
> - el mail de contacto es el de Taller Triple;
> - no hay downsell en el funnel;
> - el test tiene USD 25 en total: mide el gancho y la llegada al checkout, no si la oferta es rentable.
>
> Además, los 5 creativos ya están hechos (`anuncios/`) y la página de Facebook ya existe.

## 0. Veredicto en una línea

**El producto, el nombre y la landing están bien. Lo que puede hacer que no funcione no es el contenido: es la plata.** Al precio de hoy, cada venta deja muy poco margen para pagar el anuncio. Además hay 3 cosas que frenan la salida: la cuenta de Meta en período de gracia, el píxel compartido y la compra de prueba, que todavía no se hizo.

## 1. Semáforo

| # | Qué | Estado | Riesgo si no se arregla | Quién |
|---|---|---|---|---|
| 1 | Cuenta de Meta «Velas arg» **en período de gracia** (un pago falló) | 🔴 | Meta corta los anuncios en cualquier momento | Vos: Facturación de Meta, pagar o cambiar la tarjeta |
| 2 | **Un solo píxel («velas») para dos productos** distintos | 🔴 | Meta mezcla compradores de velas con emprendedores y optimiza mal. Las compras de una tienda ensucian la otra | Vos: crear un conjunto de datos nuevo; Claude: cargarlo en la tienda |
| 3 | **Compra de prueba en «La IA hace»: no se hizo** (0 ventas) | 🔴 | No sabés si llega el mail, si se entregan los bumps y si la Compra llega a Meta | Vos, con Claude mirando |
| 4 | **Precio base de ARS 7.990** contra el costo real por visita | 🟠 | Ver punto 3: hace falta una conversión muy alta para no perder | Decisión tuya |
| 5 | Upsell sin downsell | 🟠 | Se pierden ventas que el 50% recupera (Taller Triple ya lo tiene) | Claude, con tu OK |
| 6 | Mail de contacto de la landing = el de Taller Triple | 🟠 | Desconfianza («¿quién es Taller Triple?») y reclamos mal dirigidos | Vos: crear un mail para la marca; Claude: cambiarlo en la landing |
| 7 | Sin dominio propio ni verificación de dominio en Meta | 🟡 | El subdominio es compartido con otros vendedores de la plataforma; si Meta castiga el dominio, te arrastra. Sin verificación tampoco controlás la prioridad de eventos | Vos: comprar el dominio; Claude: conectarlo |
| 8 | Recuperación de carritos: manual, sin Brevo | 🟡 | Con Mercado Pago, cada carrito que abandona es plata que no se recupera si nadie le escribe | Vos: conectar Brevo, o revisar carritos a diario |
| 9 | Barra «X personas comprando» en el checkout | ✅ arreglado hoy | Era un contador falso: choca con «nada falso» | Claude la ocultó en las dos tiendas |
| 10 | Timer del bump | ✅ ya estaba apagado | — | — |
| 11 | Bloques del checkout | ✅ limpio | Solo un texto de garantía real | — |
| 12 | Landing: testimonios, contadores, urgencias | ✅ limpia | Sin nada falso. Los 4 negocios de ejemplo dicen que son ejemplos | — |
| 13 | Entregables (libro, 2 bumps, upsell) | ✅ cargados | — | Se confirma con la compra de prueba |
| 14 | Pasarela | ✅ Mercado Pago operativo | — | — |

## 2. Nombre del producto

**Se queda «La IA hace, vos vendés».** Es corto, rioplatense, dice el beneficio y funciona como gancho: el remate de la landing y de los anuncios es el mismo nombre.

- **El riesgo que tiene:** «vos vendés» se puede leer como una promesa de ventas. Eso ya está cubierto en la landing («No te prometemos ventas…») y no hay que romperlo en los anuncios: **nunca** «vendé más», «facturá X» ni «ganá plata con IA». Esas frases son de las que Meta marca como «hacerse rico rápido».
- **No se toca** lo que ya está en la tapa, el PDF, los mails y la landing: cambiar el nombre ahora cuesta todo eso y no suma.

## 3. La plata: precio base, bumps y upsell

### Cómo está hoy

| Pieza | Producto | Precio | Dónde sale |
|---|---|---|---|
| Front | La IA hace, vos vendés | ARS 7.990 | Landing → checkout |
| Bump 1 | Fotos de producto con el celular + IA | ARS 4.990 | Checkout (casilla) |
| Bump 2 | La planilla lista para usar | ARS 3.990 | Checkout (casilla) |
| Upsell | Las 200 instrucciones | ARS 12.990 | Después de pagar, 1 clic |
| Downsell | — | — | No hay |

### El problema, con los números de Taller Triple

Taller Triple es lo único con pauta real en esta cuenta: USD 22,75, 45 clics y unas 35 visitas a la landing. Da **~USD 0,65 por visita**. Es poca muestra, con CPM altos (USD 9–15) porque fue un solo día de aprendizaje. Para la cuenta uso dos escenarios:

- **Pesimista:** USD 0,65 por visita, como Taller Triple.
- **Bueno:** USD 0,30 por visita, que se logra con creativos que enganchen. El V2 de Taller Triple tuvo un CPC de USD 0,25.

**Supuestos (cambialos por los tuyos):**

- **Dólar de la pauta:** ARS 1.500 por cada USD que cargás. Medí el tuyo en la próxima carga.
- **Comisiones:** 10% entre Mercado Pago y la plataforma.
- **Toma de los bumps:** 25% y 20%.
- **Upsell:** 8%, y downsell, 6% de los que rechazan.

| | Hoy | Propuesta |
|---|---|---|
| Front | 7.990 | **9.990** |
| Bump 1 | Fotos 4.990 | **La planilla 4.990** (pasa a primer lugar) |
| Bump 2 | La planilla 3.990 | **Fotos 5.990** |
| Upsell | 200 instrucciones 12.990 | **200 instrucciones 16.990** |
| Downsell (si rechaza el upsell) | — | **200 instrucciones al 50%: 8.495** |
| **Ticket promedio esperado** | ~ARS 11.075 | ~ARS 14.260 |
| Ticket promedio neto en USD = **lo máximo que podés pagar por venta** | **~USD 6,6** | **~USD 8,6** |
| Conversión de la landing que necesitás para empatar, a USD 0,30 por visita | 4,5% | 3,5% |
| Ídem, a USD 0,65 por visita | 9,8% | 7,6% |

**Cómo leer la tabla:** una landing fría de low ticket en Argentina convierte, en general, entre 1% y 4%. A ARS 7.990 necesitás un 4,5% **con buenos creativos**, y eso es empatar, no ganar. A 9.990 el piso baja a 3,5%. **El precio de hoy es el riesgo más grande de que no funcione.**

**Por qué 9.990 y no más:**

- queda abajo de los 10 mil, que en la cabeza del comprador es otra categoría;
- sigue siendo low ticket, en línea con lo que enseña Bilbao (front de USD 10–15);
- Taller Triple ya cobra 14.990 y vendió.

**Por qué la planilla primero:** la landing ya la nombra (es «la planilla del Día 4, ya armada»). Es el complemento más directo del libro, el que menos hay que explicar y el que más se toma. Al ser el primer bump, va al precio más fácil.

**Por qué no tocar la estructura:** ya tenés 2 bumps desde el día 1 y un upsell más caro que el front. Es lo que pide el método. Solo falta el downsell.

**Riesgo del cambio de precio:** casi nulo en la landing, porque usa el marcador `{{price}}` en los 4 botones y en la barra fija, y el precio se actualiza solo. Hay que mirar:

- el texto de los anuncios (los videos no nombran precios: `reglas/07`);
- que no quede «7.990» escrito a mano en ningún lado (hoy no hay ninguno).

> **Si preferís no subir el front:** dejalo en 7.990 y aplicá igual el resto (bumps, upsell y downsell). El ticket promedio sube a ~ARS 12.260 (~USD 7,4 neto). Es mejor que hoy, pero sigue dependiendo de que los creativos bajen el costo por visita.

## 4. La landing

**Está muy bien.** Es honesta, concreta, muestra el contenido día por día, tiene una sección de «No es para vos si…» y una de «Sin letra chica», y el FAQ mata las objeciones reales. No tiene nada falso, y la estética de chat de WhatsApp le habla directo a quien vende por WhatsApp.

| Qué | Cambio | Por qué | Prioridad |
|---|---|---|---|
| Mail de contacto (aparece 3 veces) | Un mail de la marca, no el de Taller Triple | Confianza, y para que los reclamos lleguen ordenados | 🟠 antes de pautar |
| Meta descripción (SEO) | «usa ChatGPT» → «usá ChatGPT» | Es la que se ve al compartir el link | 🟡 |
| Prueba social de la plantilla | Hoy no se ve (la landing es HTML propio), pero la plantilla guarda 3 testimonios inventados («Lucía Fernández»…) | Si algún día se vuelve a la plantilla, salen al aire. Se borran o se reemplazan por reales | 🟡 |
| Prueba social real | Pedirles una opinión a los primeros compradores (por mail, a los 7 días) y sumar capturas reales | Es la palanca de conversión que falta. Solo con permiso del comprador | Después de las primeras ventas |
| Hero | Se queda. Opcional: probar más adelante un H1 con la promesa («Que la IA te conteste WhatsApp y te escriba los posteos, aunque no sepas nada de tecnología») | Bilbao pone la promesa en el titular. Hoy la promesa está en el subtítulo y funciona; se prueba con datos, no antes | Más adelante |

**Lo que NO hay que tocar:** la garantía de 7 días, la aclaración de que los negocios son ejemplos, «No te prometemos ventas» y «La IA se equivoca». Son las que te protegen de reclamos y de Meta.

## 5. Creativos

Los guiones de la tanda 1 están en `areas/creativos/tandas/tanda-1/guiones.md`: 5 piezas de 4 formatos distintos, con el texto del anuncio y el título.

**Lo que dicen los datos de Taller Triple** (misma cuenta, muestra chica):

- **Ganó el creativo que mostraba todo lo que trae** («V2 · Todo lo que trae»: CTR 5,6% y CPC USD 0,25).
- Los ganchos de emoción («Algo tuyo desde casa») salieron más caros (CPC USD 0,77).
- Para «La IA hace», el equivalente es mostrar **el resultado concreto en pantalla**: la respuesta de WhatsApp escrita, el posteo armado, la planilla calculando.

**Reglas que no se rompen en estos anuncios (políticas de Meta):**

- Nada de «ganá plata con IA», «ingresos extra», «vendé el doble» ni cifras de ventas.
- No afirmar nada de quien mira, como «¿No te alcanza la plata?» o «¿Estás desbordada?». Va «Si vendés por WhatsApp…».
- No usar logos de ChatGPT ni de OpenAI como si fuera algo oficial. Se puede nombrar ChatGPT como herramienta.
- Los videos no nombran el precio.

## 6. Meta: cuenta, píxel y campaña

| | Hoy | Qué hacer |
|---|---|---|
| Cuenta «Velas arg» (USD) | **En período de gracia** y con 1 campaña pausada de Taller Triple | Pagar lo pendiente o cambiar la tarjeta **hoy**. Sin esto no se lanza nada |
| Cuenta sin nombre (ARS) | Activa, **sin método de pago**, sin campañas | Opción: usarla para «La IA hace» y pagar en pesos. Compará el costo real de cada dólar en las dos (`reglas/02`). Es tu decisión |
| Píxel | Uno solo, «velas» | Crear un conjunto de datos **nuevo** para «La IA hace» y cargarlo en esa tienda, con su token de la API de conversiones. Cada producto, su píxel |
| Campaña | No existe | La de `reglas/08`: una CBO de Ventas con 1 conjunto y 5 anuncios, a 2–3 tickets por día. A 9.990 son **~USD 13–20 por día**. **3 días sin tocar** |
| URL de los anuncios | — | Con los parámetros UTM de `areas/campanas/README.md`. Sin ellos, las ventas llegan «sin origen». En Taller Triple, 24 de 26 visitas al checkout llegaron así: eran pruebas, pero en serio no sirve |

**Tope de pérdida:** lo definís vos. Axel usa USD 200 por oferta. Con USD 13–20 por día son 10–15 días, y alcanza para los 20–25 anuncios del corte de Bilbao.

## 7. Taller Triple (para que no se pierda)

**No está descartado:** se pausó con USD 22,75 gastados, en 1 día y con 5 anuncios. El método pide 3 días sin tocar y 20–25 anuncios antes de abandonar una oferta.

En ese día hubo **1 venta real con bump** (ARS 24.890) y un creativo muy bueno (V2, con CPC de USD 0,25). Si se retoma, va con su propio píxel y después de pagar la cuenta. **No se corren los dos tests juntos en la misma CBO.**

## 8. Checklist de salida (en orden)

1. [ ] Pagar la cuenta de Meta o cambiar la tarjeta, y que salga del período de gracia.
2. [ ] Decidir los precios (punto 3). Claude los aplica en la plataforma y suma el downsell.
3. [ ] Crear un mail de la marca. Claude lo cambia en la landing.
4. [ ] Crear el píxel nuevo y el token. Claude los carga en la tienda.
5. [ ] **Compra de prueba real, con los 2 bumps y aceptando el upsell.** Revisar:
   - que lleguen los 4 archivos por mail;
   - que la Compra aparezca en **Resumen** del Administrador de eventos (no en «Probar eventos»).

   Después se reembolsa desde Mercado Pago.
6. [ ] Grabar o renderizar los 5 creativos de la tanda 1, con presupuesto aprobado antes de gastar créditos.
7. [ ] Armar la CBO en borrador. Claude la revisa, **vos das el sí** y se publica.
8. [ ] 3 días sin tocar. Primera lectura con `/lectura`.
9. [ ] Opcional, la semana 1: dominio propio, verificación en Meta y Brevo para los carritos.
