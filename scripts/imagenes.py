"""Catálogo único de imágenes: lo usan los PDF, la landing y la lista de prompts.

Cuando una imagen está generada, se guarda en imagenes/<ID>.png (o .jpg/.webp) y
al volver a armar los PDF y la landing aparece sola en lugar del recuadro.
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETA = os.path.join(ROOT, 'imagenes')

ESTILO = ("Fotografía realista de estilo editorial, luz natural suave de ventana, tonos cálidos con "
          "detalles en violeta y amarillo, ambiente de casa argentina real (no de catálogo), "
          "profundidad de campo suave. Sin texto, sin letras, sin logos ni marcas en ningún lado; "
          "si aparece una pantalla de celular o compu, que el contenido se vea borroso e ilegible.")

# id: (formato, dónde se usa, qué tiene que mostrar)
IMAGENES = {
    # ---------- Ebook ----------
    'IMG-01': ('3:4', 'Tapa del ebook y fondo del inicio de la landing',
               'Una emprendedora argentina de unos 35 años, sentada en la mesa de trabajo de su casa, sonriendo mientras mira el celular que tiene en la mano. Sobre la mesa: un mate, una libreta abierta, una compu cerrada y algunos productos de su emprendimiento envueltos para enviar. Luz de ventana de costado. Plano medio, ella ocupa la mitad derecha de la imagen y deja aire arriba a la izquierda.'),
    'IMG-02': ('1:1', 'Retrato de Caro (ropa) · ebook y landing',
               'Retrato de Caro, mujer argentina de unos 30 años, pelo castaño atado, remera lisa, en un cuarto de su casa con un perchero lleno de ropa de mujer detrás, desenfocado. Sostiene una prenda doblada y mira a cámara con una sonrisa natural. Plano de pecho para arriba.'),
    'IMG-03': ('1:1', 'Retrato de Mati (pastelería) · ebook y landing',
               'Retrato de Mati, hombre argentino de unos 30 años, barba corta, delantal de cocina con un poco de harina, en la cocina de su casa con una torta decorada sobre la mesada detrás, desenfocada. Mira a cámara con una sonrisa tranquila. Plano de pecho para arriba.'),
    'IMG-04': ('1:1', 'Retrato de Sol (uñas y pestañas) · ebook y landing',
               'Retrato de Sol, mujer argentina de unos 28 años, pelo largo oscuro, uñas esculpidas color nude, en su espacio de trabajo en casa: una mesa de manicura prolija con una lámpara y frascos de esmalte detrás, desenfocados. Mira a cámara, sonrisa cálida. Plano de pecho para arriba.'),
    'IMG-05': ('1:1', 'Retrato de Fede (entrenador) · ebook y landing',
               'Retrato de Fede, hombre argentino de unos 35 años, ropa deportiva lisa, en una plaza de Córdoba con árboles y elementos de entrenamiento (colchonetas, conos) detrás, desenfocados. Mira a cámara, sonrisa segura. Plano de pecho para arriba, luz de mañana.'),
    'IMG-06': ('3:2', 'Ebook · Antes de empezar',
               'Primer plano de dos manos sosteniendo un celular, con el dedo a punto de tocar la pantalla (contenido borroso). Al costado, un mate y una libreta con una birome. Mesa de madera, luz de mañana.'),
    'IMG-07': ('3:2', 'Ebook · Día 0, la ficha de tu negocio',
               'Vista desde arriba de una mesa de trabajo: una libreta abierta con notas a mano ilegibles y algunas palabras subrayadas, una birome, un celular al lado, un mate y una tarjeta de presentación sin texto. Ordenado, cálido.'),
    'IMG-08': ('3:2', 'Ebook · Día 1, WhatsApp (también en la landing)',
               'Un celular apoyado sobre una mesa de trabajo, con la pantalla mostrando un chat lleno de mensajes (burbujas verdes y blancas, texto ilegible). Alrededor, paquetes de envío cerrados con papel kraft y una cinta. Luz de ventana.'),
    'IMG-09': ('3:2', 'Ebook · Día 2, Instagram',
               'Una emprendedora sacándole una foto con el celular a un producto (una vela en un frasco de vidrio) apoyado sobre una cartulina blanca junto a una ventana. Se la ve de espaldas o de perfil, enfocada en la pantalla del celular.'),
    'IMG-10': ('3:2', 'Ebook · Día 3, vender más',
               'Varios paquetes listos para enviar sobre una mesa, envueltos con papel de seda y una tarjetita escrita a mano (sin texto legible), con una bolsa con asas al lado. Detalle prolijo, sensación de "pedidos saliendo".'),
    'IMG-11': ('3:2', 'Ebook · Día 4, los números',
               'Mesa con una calculadora, un cuaderno con columnas de números escritos a mano (ilegibles), un celular con una planilla en pantalla (borrosa), un café y anteojos. Luz de tarde, clima tranquilo, no de oficina.'),
    'IMG-12': ('3:2', 'Ebook · Día 5, clientes difíciles',
               'Una persona sentada en un sillón, relajada, respondiendo un mensaje en el celular con expresión tranquila. Una taza en la mano libre. Ambiente de casa, luz suave.'),
    'IMG-13': ('3:2', 'Ebook · Día 6, promos e ideas',
               'Mesa con un pack de regalo armado: caja con moño, papel de seda, una tarjetita en blanco, y al costado un almanaque de papel con algunas fechas marcadas con círculos (sin números legibles). Colores festivos suaves.'),
    'IMG-14': ('3:2', 'Ebook · Día 7, tu semana en orden',
               'Escritorio ordenado con una agenda semanal abierta con algunas tareas tildadas (sin texto legible), un celular, un mate y una planta. Sensación de calma y orden.'),
    'IMG-15': ('3:2', 'Ebook · Cierre (también en la landing)',
               'Una emprendedora entregando un paquete a una clienta en la puerta de su casa, las dos sonriendo. Luz de tarde, momento cálido y real.'),
    # ---------- Bump de fotos ----------
    'IMG-20': ('3:4', 'Tapa del bump de fotos',
               'Primer plano de unas manos sosteniendo un celular que fotografía un jabón artesanal apoyado sobre una cartulina blanca curvada, junto a una ventana con luz suave. Se ve la pantalla del celular con el jabón en foco.'),
    'IMG-21': ('3:2', 'Bump de fotos · el estudio casero',
               'Un "estudio de fotos casero" armado junto a una ventana: una cartulina blanca apoyada contra la pared y curvada sobre la mesa, un producto chico encima (una vela), y del lado contrario a la ventana una plancha de telgopor parada que rebota la luz. Vista lateral que deja entender cómo está armado.'),
    'IMG-22': ('3:2', 'Bump de fotos · editar en 2 minutos',
               'Primer plano de manos editando una foto de producto en el celular: en la pantalla, una foto de una vela con una barra de ajustes abajo (íconos sin texto). Fondo desenfocado de una mesa de trabajo.'),
    # ---------- Upsell ----------
    'IMG-30': ('3:4', 'Tapa de Las 200 instrucciones',
               'Vista desde arriba de muchas tarjetas de papel de colores (violeta, amarillo, crema) ordenadas en filas como un fichero, todas sin texto, con un celular en el centro mostrando una conversación borrosa. Composición ordenada y gráfica.'),
    'IMG-31': ('3:2', 'Las 200 instrucciones · la instrucción maestra',
               'Una emprendedora en su mesa de trabajo mirando la pantalla de una compu portátil (contenido borroso) con expresión de sorpresa contenta, una mano en la boca o el mentón. Al lado, una libreta y un mate.'),
}

# Fotos que NO se hacen con IA: son reales (las pide la guía de fotos).
REALES = {
    'FOTO-A1': 'Jabón · ANTES: con la luz del techo y la cocina de fondo, sin editar',
    'FOTO-D1': 'Jabón · DESPUÉS: junto a la ventana, sobre cartulina, con rebote, editada en Snapseed',
    'FOTO-A2': 'Vela · ANTES', 'FOTO-D2': 'Vela · DESPUÉS',
    'FOTO-A3': 'Sahumerio · ANTES', 'FOTO-D3': 'Sahumerio · DESPUÉS',
}
# Escenas con IA hechas a partir de la foto DESPUÉS (edición, no imagen inventada).
ESCENAS = {
    'FOTO-E1': ('FOTO-D1', 'sobre una bandeja de mármol blanco en un baño luminoso, con una toalla doblada al costado'),
    'FOTO-E2': ('FOTO-D2', 'sobre una mesa de madera clara, con luz de ventana de costado y una planta desenfocada atrás'),
    'FOTO-E3': ('FOTO-D3', 'sobre un mantel de lino con hierbas secas y una piedra lisa al costado, luz cálida de tarde'),
}

PROPORCION = {'3:4': (3, 4), '1:1': (1, 1), '3:2': (3, 2), '4:5': (4, 5), '16:9': (16, 9)}


def archivo(id_):
    for ext in ('png', 'jpg', 'jpeg', 'webp'):
        p = os.path.join(CARPETA, f'{id_}.{ext}')
        if os.path.exists(p):
            return p
    return None


def slot(id_, clase='', url_base=None, alto=None):
    """HTML de la imagen si existe; si no, un recuadro con el ID y qué va."""
    if id_ in IMAGENES:
        fmt, donde, desc = IMAGENES[id_]
    elif id_ in REALES:
        fmt, donde, desc = '1:1', 'Foto real', REALES[id_]
    else:
        fmt, donde, desc = '1:1', 'Escena con IA', ESCENAS[id_][1]
    w, h = PROPORCION[fmt]
    p = archivo(id_)
    estilo = f'aspect-ratio:{w}/{h};' + (f'height:{alto};width:auto;' if alto else '')
    if p:
        src = (url_base + os.path.basename(p)) if url_base else 'file://' + p
        return f'<img class="img {clase}" style="{estilo}" src="{src}" alt="">'
    corto = html.escape(donde if id_.startswith('FOTO') else desc.split('.')[0])
    return (f'<div class="img ph-img {clase}" style="{estilo}"><span class="ph-id">{id_}</span>'
            f'<span class="ph-txt">{corto}</span></div>')
