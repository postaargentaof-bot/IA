---
name: lectura
description: Lectura del día - cómo viene Meta contra las ventas reales, qué subir, bajar, renovar o apagar, y alertas. Usar cuando se pide "cómo viene", "lectura", "qué pauso" o "/lectura".
---

# /lectura

1. **Delegá en el agente `campanas`** la lectura completa: Meta, las ventas reales (por día y por anuncio), las reglas de `reglas/08` y las alertas.
2. **Mostrá la lectura, corta y visual:**
   - el **semáforo** en una línea (🟢 gana / 🟡 justo / 🔴 pierde): la ganancia de ayer y la de 3 días, y el costo por venta real contra el equilibrio;
   - la **tabla de propuestas:** conjunto · acción · por qué, en números;
   - las **alertas**, si hay.
3. **Guardá la lectura** en `areas/campanas/lecturas/AAAA-MM-DD.md`.
4. **Si hay cambios propuestos, preguntá:** «¿Hago X e Y? (sí / no / solo X)».

   Recién con el sí:
   1. ejecutalo con el conector de Meta;
   2. verificá que quedó publicado y no en borrador;
   3. anotalo en `areas/campanas/registro.md`.
5. **Cerrá:** `ESTADO.md` si cambió algo, commit y push.
