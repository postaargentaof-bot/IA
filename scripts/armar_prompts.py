"""Genera imagenes/prompts.md desde el catálogo de scripts/imagenes.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from imagenes import IMAGENES, REALES, ESCENAS, ESTILO, CARPETA

FMT = {'3:4': 'vertical 3:4', '1:1': 'cuadrada 1:1', '3:2': 'horizontal 3:2'}
L = ["# Prompts de las imágenes", "",
     "Lista de todas las imágenes que usan los PDF y la landing. Cada recuadro con un código (IMG-01, IMG-02…) en los PDF y la landing es una de estas.", "",
     "## Cómo generarlas", "",
     "1. Abrí ChatGPT (o Gemini) y pegá el prompt de cada imagen **tal cual**, incluida la parte del estilo: es lo que hace que todas parezcan de la misma serie.",
     "2. **Retratos de los 4 negocios (IMG-02 a IMG-05):** generá primero IMG-01 y los 4 retratos. Si una persona aparece en otra imagen, subí su retrato y agregá: «Usá a esta misma persona».",
     "3. Si algo sale con texto, letras raras, dedos de más o logos: pedí «sacá todo el texto y los logos» o generala de nuevo. **No uses una imagen con texto inventado.**",
     "4. Descargá cada imagen y guardala en la carpeta `imagenes/` del repo con el nombre exacto del código: `IMG-01.png`, `IMG-02.png`, etc. (sirve .png, .jpg o .webp).",
     "5. Avisame y vuelvo a armar los PDF y la landing: las imágenes aparecen solas en su lugar.", "",
     "**Para la landing en Impultienda:** después las subimos a Diseño de tienda → Recursos y cargamos sus direcciones en `imagenes/urls.json`.", "",
     "**Sobre las personas:** son personas generadas con IA para ilustrar ejemplos armados. No se presentan como clientes reales ni como testimonios (el libro y la landing ya lo aclaran).", "",
     "## El estilo (va al final de todos los prompts)", "", f"> {ESTILO}", ""]
grupos = [('Ebook «La IA hace, vos vendés»', [k for k in IMAGENES if int(k[4:]) < 20]),
          ('Bump · Fotos de producto con el celular + IA', [k for k in IMAGENES if 20 <= int(k[4:]) < 30]),
          ('Upsell · Las 200 instrucciones', [k for k in IMAGENES if int(k[4:]) >= 30])]
for titulo, ids in grupos:
    L += [f"## {titulo}", ""]
    for i in ids:
        fmt, donde, desc = IMAGENES[i]
        L += [f"### {i} · {donde}", f"*Formato: {FMT[fmt]}*", "", "```", f"{desc} {ESTILO} Formato {FMT[fmt]}.", "```", ""]
L += ["## Fotos reales (NO se hacen con IA)", "",
      "La guía de fotos promete «nunca cambies el producto». Por eso el antes y el después tienen que ser fotos **reales**, sacadas con el celular, siguiendo la misma guía. Guardalas en `imagenes/` con estos nombres:", "",
      "| Código | Qué foto |", "|---|---|"]
L += [f"| `{k}` | {v} |" for k, v in REALES.items()]
L += ["", "## Escenas con IA (a partir de la foto real del DESPUÉS)", "",
      "Subí a ChatGPT la foto del después y pegá el prompt. Revisá que el producto haya quedado **idéntico** (color, forma, tamaño); si cambió, no sirve.", ""]
for k, (base, escena) in ESCENAS.items():
    L += [f"### {k} · a partir de {base}", "```",
          f"Tomá el producto de esta foto y ubicalo {escena}. Que parezca una foto real de producto, no una ilustración. Mantené el producto exactamente igual: mismo color, forma, tamaño, textura y detalles. No agregues texto ni logos. Formato cuadrado 1:1.",
          "```", ""]
open(os.path.join(CARPETA, 'prompts.md'), 'w').write('\n'.join(L))
print('ok', len(IMAGENES), 'imágenes con IA,', len(REALES), 'reales,', len(ESCENAS), 'escenas')
