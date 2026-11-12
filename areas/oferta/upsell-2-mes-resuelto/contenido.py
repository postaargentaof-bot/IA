# Contenido de «El mes resuelto» (upsell 2 de «La IA hace, vos vendés»).
# Se edita acá y se vuelve a generar el PDF con generar.py.
# Lo que va entre [corchetes] lo completa el comprador (o la IA con su ficha).

TITULO = "El mes resuelto"
SUBTITULO = "30 días de Instagram y WhatsApp, listos para completar con los datos de tu negocio"

INSTRUCCION_MAESTRA = """Te paso la ficha de mi negocio y una plantilla de un posteo.
Completá los huecos que están entre [corchetes] con los datos de mi ficha y escribilo con mi forma de hablar.
Reglas:
1. No inventes precios, plazos, datos ni opiniones de clientes. Si falta un dato, preguntame antes de escribir.
2. Que suene a una persona, no a una publicidad.
3. Dame 2 versiones: una corta y una un poco más larga.

MI FICHA:
[pegá acá tu ficha del Día 0]

LA PLANTILLA:
[pegá acá la plantilla del día]"""

REGLAS = [
    ("Nada inventado.", "Ni opiniones de clientes, ni «últimas unidades», ni precios viejos. Si un posteo necesita un dato que no tenés, cambiá el posteo, no el dato."),
    ("Urgencia, solo si es verdad.", "Si decís «pedidos hasta el jueves», el viernes no tomás. Si decís «promo hasta el domingo», el lunes vuelve el precio de siempre."),
    ("Fotos de clientes, solo con permiso.", "Antes de subir una foto o una captura de un cliente, le preguntás. Las capturas de chat van sin nombre ni número."),
    ("Nada de antes y después del cuerpo.", "En estética y en entrenamiento, no muestres el cuerpo de alguien sin su permiso por escrito, y nunca prometas resultados. Mostrá el proceso, el material, el trabajo."),
    ("Los datos de tus clientes no van a la IA.", "Ni nombres, ni teléfonos, ni direcciones. La IA trabaja con tu ficha, que es lo mismo que ya tenés publicado."),
    ("Listas de difusión, con salida.", "Los mensajes de difusión de WhatsApp solo les llegan a los contactos que tienen tu número agendado. Mandá pocos, que valgan la pena, y siempre con la opción de salir de la lista."),
    ("La IA escribe el borrador; vos lo revisás.", "Precios, fechas, horarios y nombres los confirmás vos antes de publicar."),
    ("Mejor hecho que perfecto.", "Si un día no podés, no pasa nada: seguís al día siguiente. Lo que funciona es la constancia, no la perfección."),
]

SEMANAS = [
    ("Semana 1", "Que te conozcan", "La gente le compra a alguien, no a una cuenta. Esta semana mostrás quién está detrás, qué hacés y cómo se te compra."),
    ("Semana 2", "Que lo quieran", "Esta semana el protagonista es tu producto: los detalles, cómo se usa, para quién es."),
    ("Semana 3", "Que te crean", "Antes de pagar, la gente quiere estar segura. Esta semana mostrás cómo trabajás y respondés las dudas antes de que te las pregunten."),
    ("Semana 4", "Que compren", "Ya te conocen, ya lo vieron y ya te creen. Esta semana les hacés fácil comprar: combos, fechas reales y un pedido claro."),
    ("Días 29 y 30", "Cerrar y repetir", "Se cierra el mes, se mira qué funcionó y se arma el mes que viene sin empezar de cero."),
]

# Cada día: (número, semana_idx, formato, título, para_qué, posteo, idea_visual, historia, whatsapp)
DIAS = [
    (1, 0, "Foto o carrusel", "Presentate",
     "Que quien llega a tu cuenta sepa en 5 segundos quién sos y qué vendés.",
     """Si recién llegás, hola 👋 Soy [tu nombre] y hago [qué vendés] en [tu zona].
Empecé [hace cuánto] porque [el motivo real, en una frase].
Hoy hago [tus productos o servicios] para [a quién].
📦 [Envíos a / Retiro en / Turnos en] [dónde].
💬 Precios y pedidos, por WhatsApp: [link o «link en la bio»].""",
     "Una foto tuya trabajando, o de tus manos con el producto. Si no querés mostrar la cara, las manos alcanzan.",
     "Sticker de preguntas: «¿Qué te gustaría ver por acá este mes?»",
     "Estado: «Arranco el mes con todo: esta semana te muestro cómo trabajo. Cualquier consulta, te respondo por acá 😊»"),
    (2, 0, "Reel", "Un día de trabajo",
     "Mostrar lo que hay detrás: el trabajo que tus clientes nunca ven.",
     """Así arranca un [día de la semana] en [nombre del negocio]:
☕ [primer paso del día]
✂️ [segundo paso]
📦 [tercer paso]
Lo que más me gusta de esta parte es [algo real].
¿Querés que te muestre cómo se hace [producto] de principio a fin? Te leo en comentarios.""",
     "5 o 6 clips cortos (2 a 3 segundos cada uno) de tu día: abrir, preparar, hacer, empaquetar. Música de la app de Instagram.",
     "Compartí el reel con una encuesta: «¿Te muestro más del proceso?» Sí / ¡Obvio!",
     "Estado: un clip del reel con el texto «Así arranco el día 👀»."),
    (3, 0, "Carrusel", "Qué vendés y cómo comprarte",
     "Que nadie tenga que preguntar lo básico. Es la publicación que vas a fijar arriba de tu perfil.",
     """Todo lo que hago, en una sola publicación 👇 (guardala para tenerla a mano)
Placa 1: «[Nombre del negocio]: todo en un lugar»
Placas 2 a 4: un producto o servicio por placa, con foto, nombre y [precio o «desde $»].
Placa 5: «Cómo pedir: 1) Me escribís por WhatsApp. 2) Te paso [talles / sabores / turnos]. 3) [Seña o pago] con [medios de pago]. 4) [Entrega / retiro / turno] en [plazo real].»
Texto: «Esta es la guía rápida de [negocio]. Si te queda alguna duda, escribime: [link].»""",
     "Fondo liso y del mismo color en las 5 placas. Una foto clara por placa.",
     "Compartí la publicación y fijala en tus historias destacadas como «Cómo comprar».",
     "Actualizá el catálogo de WhatsApp Business con las mismas fotos y precios. Lo vas a usar todo el mes."),
    (4, 0, "Foto", "Tu producto estrella",
     "Ponerle cara al producto que más vendés o que más te gusta hacer.",
     """Si tuviera que elegir uno, es este: [producto].
Por qué: [razón 1] y [razón 2].
Sale $[precio] y [cómo se pide / cuánto tarda].
¿Lo querés en [variante: color, sabor, diseño]? Escribime y te paso las opciones.""",
     "Foto de cerca, con luz de ventana, sobre un fondo liso. (Si tenés la guía de fotos, aplicá el Día 1 de esa guía.)",
     "Foto de detalle + sticker de encuesta con dos variantes: «¿Cuál elegís?»",
     "Estado: la foto con el precio y «Consultas por acá»."),
    (5, 0, "Carrusel o historia", "Las preguntas que más te hacen",
     "Contestar en público lo que te preguntan en privado. Te ahorra mensajes y da confianza.",
     """Las 3 preguntas que más me hacen 👇
1. ¿[Pregunta frecuente 1]? [Respuesta corta].
2. ¿[Pregunta frecuente 2]? [Respuesta corta].
3. ¿[Pregunta frecuente 3]? [Respuesta corta].
¿Te quedó otra duda? Mandámela y la sumo a la próxima.""",
     "Una placa por pregunta, con letra grande. Usá las respuestas que armaste en el Día 1 del libro.",
     "Caja de preguntas: «Preguntame lo que quieras de [producto]». Respondé 2 o 3 en historias.",
     "Guardá estas 3 respuestas como respuestas rápidas de WhatsApp Business, si todavía no lo hiciste."),
    (6, 0, "Reel", "De la materia prima al producto",
     "Mostrar la transformación: de los materiales al producto terminado. Engancha porque tiene principio y final.",
     """De esto 👉 [materia prima: tela, harina, esmaltes, plan de rutina] a esto 👉 [producto terminado].
Lleva [tiempo real] y el paso que más cuidado me pide es [paso].
¿Querés uno? Pedidos por WhatsApp: [link].""",
     "Primer plano de los materiales, 3 o 4 clips del proceso y el producto terminado al final. En estética y entrenamiento: el material, la mesa armada o la rutina escrita, no el cuerpo de nadie.",
     "Compartí el reel con el sticker «¿Adivinás cuánto tarda?» y respondé al otro día.",
     "Estado: el clip final, con «Recién terminado ✨»."),
    (7, 0, "Historias y difusión", "Repaso de la semana",
     "Cerrar la semana y mandar tu primer mensaje de difusión del mes.",
     """Historias: «Esta semana te mostré cómo trabajo, qué hago y cómo se pide. ¿Qué fue lo que más te gustó?» (encuesta con 2 opciones).
Para vos: anotá cuál de los 6 posteos te trajo más mensajes. Lo vas a usar el día 30.""",
     "3 historias seguidas con capturas de los posteos de la semana.",
     "La encuesta de arriba.",
     """Difusión: «¡Hola! Te cuento qué hay esta semana en [negocio]: [novedad o producto]. Si querés algo, respondé este mensaje y te paso la info.
(Si preferís no recibir estos mensajes, avisame y te saco de la lista 🙂)»"""),

    (8, 1, "Carrusel", "Los detalles que no se ven",
     "Mostrar lo que hace distinto a tu producto: el material, el ingrediente, la técnica.",
     """Lo que no se ve en la foto de [producto] 👇
Placa 2: [detalle 1: material, ingrediente o técnica] — por qué lo elijo.
Placa 3: [detalle 2] — qué cambia para vos.
Placa 4: [detalle 3] — lo que casi nadie hace.
Placa 5: «Por eso [producto] [beneficio real]. Pedidos: [link].»""",
     "Fotos muy de cerca de cada detalle. Si tenés lupa o macro en el celular, este es el día.",
     "Una historia por detalle, con la pregunta «¿Sabías esto?»",
     "Estado: la foto más de cerca, con «El detalle que hace la diferencia»."),
    (9, 1, "Reel", "Cómo se usa, se combina o se cuida",
     "Ayudar a imaginar el producto en la vida de quien mira.",
     """3 formas de [usar / combinar / conservar] tu [producto]:
1. [forma 1]
2. [forma 2]
3. [forma 3]
¿Cuál es la tuya? Contame en comentarios.""",
     "Un clip por forma, con el número grande en pantalla.",
     "Sticker de preguntas: «¿Cómo lo usarías vos?»",
     "Estado: la forma que más te gusta, con «Tip del día»."),
    (10, 1, "Foto", "El producto en la vida real",
     "Salir del fondo liso y mostrarlo usado: puesto, servido, aplicado, en acción.",
     """[Producto], en la vida real.
[Una frase sobre el momento: «Así quedó en la mesa de cumple de…», «Así se ve con…»].
Si querés el tuyo, [cómo se pide y en cuánto llega].""",
     "Una foto tuya usándolo, o de un cliente que te haya dado permiso. Sin permiso, no.",
     "La foto + el sticker «Agregá la tuya» si tus clientes te etiquetan.",
     "Estado: la misma foto, con «¿Te imaginás el tuyo?»"),
    (11, 1, "Carrusel", "Para quién es (y para quién no)",
     "Decir para quién no es da más confianza que decir que es para todos.",
     """¿[Producto] es para vos? 👇
✓ Sí, si [situación 1].
✓ Sí, si [situación 2].
✓ Sí, si [situación 3].
✕ No, si [situación en la que no conviene].
✕ No, si [otra situación].
Si dudás, escribime y te digo con sinceridad si te sirve.""",
     "Dos placas: una verde con los ✓ y una con los ✕.",
     "Encuesta: «¿Te ves en la lista del sí?»",
     "Estado: la placa de los ✓."),
    (12, 1, "Reel", "Todo el proceso en 15 segundos",
     "El proceso entero, acelerado. Hipnotiza y muestra el trabajo que hay detrás.",
     """De cero a [producto] en 15 segundos ⏱️ (en la vida real son [tiempo real]).
Cada uno se hace [a mano / a pedido / con turno].
Pedidos: [link].""",
     "Celular fijo (apoyado o con trípode) y grabás el proceso entero. Después lo acelerás en la app.",
     "Compartí el reel con «¿Cuánto creés que tardo de verdad?» y respondé con el número real.",
     "Estado: los últimos 5 segundos del reel."),
    (13, 1, "Historias", "Que tus clientes elijan",
     "Preguntar qué quieren antes de hacerlo. Es contenido y es investigación de mercado gratis.",
     """3 historias seguidas:
1. «Estoy por hacer [algo nuevo]. Ayudame a elegir 👇»
2. Encuesta: [opción A] o [opción B].
3. Deslizador: «¿Cuánto te gusta la idea?»
Al otro día, contá qué ganó. Y si lo hacés, avisales primero a los que votaron.""",
     "Fotos de las dos opciones lado a lado.",
     "Las 3 de arriba.",
     "Estado: la misma encuesta, con «Votá respondiendo A o B»."),
    (14, 1, "Historias y difusión", "Repaso de la semana 2",
     "Cerrar la semana y mandar la segunda difusión.",
     """Historias: el resultado de la encuesta del día 13 y «Esta semana te mostré [producto] de cerca. La que viene, cómo trabajo con los pedidos».
Para vos: anotá cuál de los posteos de la semana te trajo más mensajes.""",
     "Capturas de los posteos de la semana.",
     "El resultado de la encuesta.",
     """Difusión: «¡Hola! Esta semana estuve mostrando [producto]. Si te interesa, te paso fotos y precio. ¡Que tengas buena semana!
(Si no querés recibir estos mensajes, avisame y te saco 🙂)»"""),

    (15, 2, "Carrusel", "Cómo trabajo",
     "Las reglas claras evitan reclamos y dan seguridad para pagar.",
     """Cómo trabajo en [negocio] 👇
1. Pedidos: [cómo y con cuánta anticipación].
2. Seña o pago: [cuánto y con qué medios].
3. Tiempos: [plazo real de entrega o turno].
4. Envíos o retiro: [zonas, costo, días].
5. Cambios o cancelaciones: [tu política real].
Guardalo así lo tenés cuando quieras pedir.""",
     "Una placa por punto, con un ícono simple.",
     "Fijá esta publicación en tus destacadas, junto a «Cómo comprar».",
     "Estado: «Nueva guía de cómo trabajo, en mi Instagram 👉 [usuario]»."),
    (16, 2, "Reel", "Una duda frecuente, en video",
     "Que te escuchen. La voz o la cara generan más confianza que cualquier texto.",
     """Me preguntan mucho: «¿[pregunta frecuente]?»
La respuesta corta: [respuesta].
La larga, en el video 👆
¿Tenés otra duda? Dejala en comentarios.""",
     "Vos hablando a cámara 20 o 30 segundos. Si no querés mostrarte, tu voz sobre imágenes del producto.",
     "Caja de preguntas para elegir la del próximo video.",
     "Estado: el mismo video."),
    (17, 2, "Foto o captura", "Lo que dice un cliente (solo si es real)",
     "Mostrar la opinión de alguien que te compró. Solo si es real y con su permiso.",
     """Esto me escribió [nombre o inicial, con su permiso] después de [producto o servicio]:
«[su mensaje, textual]»
Gracias por la confianza 🙏 Si querés el tuyo, [cómo se pide].""",
     "Captura del chat sin el número ni la foto de perfil. Si no tenés ninguna opinión todavía, hoy no publicás esto: hoy la pedís (mirá el mensaje de WhatsApp de abajo).",
     "La captura, con el sticker de corazón.",
     """Para pedir opiniones (a quien te compró hace poco): «¡Hola [nombre]! ¿Cómo te fue con [producto]? Si te gustó, ¿me dejarías dos líneas contándolo? Si me das permiso, lo comparto en mi Instagram (sin tu número). ¡Gracias!»"""),
    (18, 2, "Carrusel", "El error más común (y cómo evitarlo)",
     "Enseñar algo útil de tu rubro. Te posiciona como alguien que sabe.",
     """El error más común con [tema de tu rubro] 👇
Placa 2: el error: [qué hace la mayoría].
Placa 3: por qué pasa: [explicación simple].
Placa 4: cómo evitarlo: [2 o 3 pasos].
Placa 5: «Si querés que [lo hagamos bien / te ayude], escribime: [link].»""",
     "Placas de texto con letra grande y una foto de ejemplo.",
     "Encuesta: «¿Te pasó alguna vez?» Sí / No",
     "Estado: la placa del error, con «¿Te pasó?»"),
    (19, 2, "Foto o reel", "Tu lugar de trabajo",
     "Mostrar dónde y con qué trabajás. Hace real al negocio.",
     """Este es mi rincón de trabajo 🛠️
Acá [qué hacés ahí]. Lo que más uso: [herramienta o material].
Lo que no se ve: [algo real, una frase].
¿Querés que te muestre algo en particular? Te leo.""",
     "Foto general del espacio ordenado y 2 o 3 detalles. No hace falta que sea lindo: tiene que ser real.",
     "Video corto recorriendo el espacio.",
     "Estado: la foto, con «Mi lugar ✨»."),
    (20, 2, "Historias", "Pedidos de la semana",
     "Mostrar trabajo real, sin datos de nadie.",
     """3 a 5 historias con lo que entregaste o hiciste esta semana (solo productos, sin nombres ni direcciones).
Texto: «Lo que salió esta semana 📦 ¡Gracias a todos los que confiaron!»""",
     "Una foto por pedido, con la misma luz y el mismo fondo.",
     "Las de arriba, y guardalas en una destacada: «Entregas».",
     "Estado: el collage de la semana."),
    (21, 2, "Historias y difusión", "Repaso de la semana 3",
     "Cerrar la semana y pedir opiniones en serie.",
     """Historias: «Esta semana te conté cómo trabajo. La que viene hay [novedad, combo o fecha], atenta/o».
Para vos: anotá el posteo de la semana que más mensajes trajo.""",
     "Capturas de los posteos de la semana.",
     "Anticipo de la semana 4: «La semana que viene hay algo especial 👀» (solo si es verdad).",
     """Difusión a quienes te compraron este mes: el mensaje del día 17 para pedir opinión. A los demás: «¡Hola! La semana que viene en [negocio] hay [novedad real]. Te aviso primero a vos. (Si no querés estos mensajes, avisame 🙂)»"""),

    (22, 3, "Carrusel", "Un combo que te cierre",
     "Subir el ticket sin regalar plata. Antes de publicarlo, calculalo con la planilla del Día 4.",
     """Combo [nombre] 👇
Incluye: [producto 1] + [producto 2] + [producto 3].
Por separado sale $[suma real]. En combo, $[precio del combo].
Ideal para [ocasión o tipo de cliente].
Pedidos: [link]. [Hasta cuándo, solo si hay una fecha real.]""",
     "Una foto con los productos del combo juntos y una placa con el detalle.",
     "La foto del combo + encuesta «¿Lo armarías distinto?»",
     "Estado: el combo, con el precio y «Consultas por acá»."),
    (23, 3, "Reel", "Directo al pedido",
     "Un video con un solo objetivo: que escriban para pedir.",
     """[Producto] 👉 $[precio]
✅ [beneficio 1]
✅ [beneficio 2]
✅ [cómo llega o cuándo]
Para pedir: escribime «QUIERO» por WhatsApp [link] y te paso todo.""",
     "8 a 10 segundos: el producto en 3 planos y el texto grande en pantalla.",
     "Compartí el reel con el sticker de link a tu WhatsApp.",
     "Respuesta rápida lista para «QUIERO»: «¡Hola! Qué bueno que te interesa [producto]. Te cuento: [precio, variantes, entrega]. ¿Te lo reservo?»"),
    (24, 3, "Foto", "Lo nuevo o lo de temporada",
     "Engancharte a una fecha o a una novedad real del calendario que armaste en el Día 6.",
     """Llegó [novedad o producto de temporada] 🎉
[Qué es y por qué ahora: fecha, estación o pedido de tus clientes].
Sale $[precio] y [hasta cuándo, solo si es real].
¿Lo querés? [cómo se pide].""",
     "La foto más linda del mes. Si es para una fecha, sumá un detalle que la recuerde.",
     "Cuenta regresiva de Instagram solo si hay una fecha real (lanzamiento, cierre de pedidos).",
     "Estado: la foto, con «Nuevo ✨»."),
    (25, 3, "Historias", "Las fechas de verdad",
     "Avisar los plazos reales. Ordena tus pedidos y ayuda a decidir.",
     """«Para recibirlo para [fecha], pedidos hasta el [día real].»
«Esta semana me quedan [número real] turnos / lugares en la producción.»
Solo con números y fechas reales: si no hay un límite, no lo inventes.""",
     "Placa de texto grande con la fecha.",
     "La placa + el sticker de link a WhatsApp.",
     "Estado: la misma placa."),
    (26, 3, "Carrusel", "Ideas para regalar",
     "Mucha gente compra para regalar. Ayudales a elegir.",
     """¿No sabés qué regalar? 👇
Hasta $[precio 1]: [opción].
Hasta $[precio 2]: [opción].
Hasta $[precio 3]: [opción o combo].
[¿Lo envolvés para regalo? Contalo.] Pedidos: [link].""",
     "Una placa por rango de precio, con la foto del producto.",
     "Encuesta: «¿Para quién estás buscando regalo?»",
     "Estado: la placa del rango más barato."),
    (27, 3, "Reel o foto", "Para el que preguntó y no compró",
     "Recuperar consultas que quedaron en el aire. Es la venta más fácil del mes.",
     """Publicación: «Las 3 dudas que hacen que alguien no se decida (y la respuesta) 👇 1) [duda: precio, tiempo, si le va a quedar bien]: [respuesta honesta]. 2) [duda]: [respuesta]. 3) [duda]: [respuesta].»""",
     "Una placa por duda, o vos contándolo a cámara.",
     "La publicación + «Si te quedó alguna duda, escribime sin compromiso».",
     """Mensaje individual a quien consultó en el mes y no compró (uno por uno, no difusión): «¡Hola [nombre]! El otro día me preguntaste por [producto]. ¿Te quedó alguna duda? Si querés, te lo reservo. Y si no es el momento, cero drama 🙂»"""),
    (28, 3, "Historias y difusión", "Repaso de la semana 4",
     "La difusión más importante del mes: la que cierra ventas.",
     """Historias: el combo, lo nuevo y las fechas reales, en 3 historias seguidas.
Para vos: anotá el posteo de la semana que más mensajes trajo.""",
     "Capturas de los posteos de la semana.",
     "Las 3 de arriba, con el sticker de link a WhatsApp en la última.",
     """Difusión: «¡Hola! Te cuento lo que hay en [negocio]: [combo o novedad], a $[precio]. [Pedidos para (fecha) hasta el (día), solo si es real.] Si querés, respondé este mensaje y lo armamos. (Si no querés estos mensajes, avisame 🙂)»"""),

    (29, 4, "Foto o carrusel", "Gracias y lo que viene",
     "Cerrar el mes agradeciendo y dejar la puerta abierta al que viene.",
     """Se termina [mes] y quiero decirte gracias 🙏
Este mes [algo real: hice X pedidos, estrené Y, aprendí Z].
El mes que viene se viene [lo que tengas planeado, si ya lo sabés].
Si estuviste mirando y todavía no te animaste, te espero por WhatsApp: [link].""",
     "Un collage de fotos del mes o una foto tuya con el producto.",
     "Caja de preguntas: «¿Qué te gustaría ver el mes que viene?»",
     "Estado: la foto, con «¡Gracias por este mes!»"),
    (30, 4, "Para vos (no se publica)", "Revisá el mes y armá el próximo",
     "En 30 minutos sabés qué repetir y qué cambiar. El mes 2 sale mucho más rápido.",
     """1. Mirá tus anotaciones de los días 7, 14, 21 y 28: ¿qué 4 posteos trajeron más mensajes?
2. Abrí las estadísticas de Instagram: ¿qué 3 publicaciones alcanzaron a más gente?
3. Completá la tabla de la página siguiente.
4. Mes 2: repetís las mismas 30 plantillas, pero con otros productos, otras preguntas y otros detalles. Los que mejor funcionaron, los hacés 2 veces.""",
     "—",
     "—",
     "Limpiá la lista de difusión: sacá a quien te pidió salir y sumá a los clientes nuevos que agendaron tu número."),
]

# Ejemplos resueltos con los 4 negocios del libro (armados para enseñar, no son negocios reales).
EJEMPLOS = [
    (1, "Caro · ropa por Instagram · Lanús",
     """Si recién llegás, hola 👋 Soy Caro y vendo ropa cómoda para todos los días desde mi casa en Lanús.
Empecé hace dos años porque no encontraba buzos lindos que no salieran una fortuna.
Hoy traigo buzos, joggers y remeras de talle S a XXL.
📦 Envíos a todo el país o retiro en Lanús Oeste.
💬 Precios y talles, por WhatsApp: link en la bio."""),
    (9, "Mati · tortas por encargo · Morón",
     """3 formas de conservar tu torta para que llegue perfecta al cumple 🎂
1. Heladera hasta 2 horas antes de servir (nunca al sol ni en el auto cerrado).
2. Sacala de la caja recién en la mesa, así no se marca la crema.
3. Si sobra, tapada con film y en heladera: dura 3 días.
¿Cuál no sabías? Contame en comentarios."""),
    (15, "Sol · uñas y pestañas · Rosario",
     """Cómo trabajo en Sol Nails 👇
1. Turnos: por WhatsApp, con una semana de anticipación (los sábados vuelan).
2. Seña: $3.000 por transferencia o Mercado Pago para reservar.
3. Duración: esculpidas, 2 horas; service, 1 hora y media.
4. Dónde: en mi estudio de barrio Echesortu (te paso la dirección al confirmar).
5. Cancelaciones: avisando con 24 horas, la seña queda para otro turno.
Guardalo así lo tenés cuando quieras reservar."""),
    (22, "Fede · entrenador personal · Córdoba",
     """Combo Arranque 👇
Incluye: evaluación inicial + plan de 4 semanas + 2 clases presenciales en la plaza.
Por separado sale $54.000. En combo, $46.000.
Ideal si hace mucho que no entrenás y querés volver de a poco, con un plan armado para vos.
Consultas: escribime «ARRANQUE» por WhatsApp."""),
]
