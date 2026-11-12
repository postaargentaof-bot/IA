---
name: tanda
description: Arrancar una tanda nueva de 5 creativos - ideas, guiones, revisión y fichas. Usar cuando se pide "tanda nueva", "creativos para mañana", "ganchos" o "/tanda".
---

# /tanda

El flujo de una tanda, con una parada para {{NOMBRE}} en cada paso:

```
Ideas (8) ──► elige 5 ──► Guiones ──► Revisor ──► aprueba ──► Voces y render ──► Fichas ──► Meta (con sí)
```

1. **Ideas:** delegá en `creativos` 8 ideas de gancho, con el ángulo y el porqué, mirando el banco de ganchos y lo que vendió. Mostralas en una tabla y pedí que elija 5: el 70% variaciones de ganadores y el 30% nuevo (`reglas/07`).
2. **Guiones:** `creativos` escribe los 5 guiones completos, con sus fuentes. Guardalos en `areas/creativos/tandas/tanda-N/guiones.md`.
3. **Revisión:** pasale los guiones a `revisor`. Mostrá el veredicto y aplicá lo que bloquea.
4. **Aprobación:** {{NOMBRE}} aprueba los textos. Si hay generaciones pagas (voces, imágenes), pasá la cuenta (cantidad × costo = total, y el saldo que queda) y esperá el OK.
5. **Producción:** las voces y el render (en la PC, con VS Code o CapCut). Los archivos pesados no van al repo.
6. **Fichas:** una fila por pieza en `areas/creativos/banco-de-ganchos.md`.
7. **Meta:** {{NOMBRE}} sube los videos a la biblioteca multimedia. El conjunto de renovación se arma con su sí (`reglas/08`, filas 10 y 11) y con los parámetros de URL de `areas/campanas/README.md`.
8. **Cerrá:** tarea en «hecho», commit y push.
