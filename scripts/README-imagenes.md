# Cómo se arman los PDF, la landing y las imágenes

- `scripts/imagenes.py`: catálogo único de imágenes (código, formato, dónde va, prompt).
- `python3 scripts/armar_prompts.py` → `imagenes/prompts.md`
- `python3 scripts/armar_pdf.py scripts/pdf-config/ebook.json` (y `fotos.json`, `ups.json`) → `pdf/`
- `python3 scripts/armar_landing.py` → `landing/landing.html` y `landing/postcompra.html` (para Impultienda)
- `python3 scripts/armar_landing.py --preview` → `landing/preview/` (para mirar en el navegador)

Cuando una imagen está en `imagenes/<CÓDIGO>.png`, aparece sola al volver a armar. Si no está, sale un recuadro con su código.
Orden: primero los PDF (la landing usa capturas de los PDF como mockups), después la landing.
