# Cómo se arman los PDF, la landing y las imágenes

- `scripts/imagenes.py`: catálogo único de imágenes (código, formato, dónde va, prompt).
- `python3 scripts/armar_prompts.py` → `imagenes/prompts.md`
- `python3 scripts/armar_pdf.py scripts/pdf-config/ebook.json` (y `fotos.json`, `ups.json`) → `pdf/`
- `python3 scripts/armar_landing.py` → `landing/landing.html` y `landing/postcompra.html` (para Impultienda)
- `python3 scripts/armar_landing.py --preview` → `landing/preview/` (para mirar en el navegador)

Cuando una imagen está en `imagenes/<CÓDIGO>.png`, aparece sola al volver a armar. Si no está, sale un recuadro con su código.
- En los PDF van copias JPEG livianas (1400 px, calidad 80), para que no pasen los ~15 MB. Se cambia con `img_lado` / `img_calidad` en el json.
- La landing copia las fotos que usa a `landing/assets/IMG-xx.jpg` (1600 px). En la versión para Impultienda salen como `src="RECURSO:IMG-xx.jpg"` (y `RECURSO:tapa-ebook.png`, etc.) hasta que se cargan sus direcciones de Recursos en `imagenes/urls.json`, con el código o el nombre del archivo como clave.
- Requisitos: `pip install markdown pypdf pillow`, Playwright (ya viene) y `pdftoppm`.
Orden: primero los PDF (la landing usa capturas de los PDF como mockups), después la landing.
