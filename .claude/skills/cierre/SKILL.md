---
name: cierre
description: Cerrar el día - tareas al día, números, estado, decisiones y todo guardado en el repo. Usar con "/cierre", "cerremos", "terminamos por hoy".
---

# /cierre

1. **Números del día** (si hay campañas): delegá en el agente `campanas` la ganancia real, el costo por venta real y lo que se cambió.
2. **Tareas:** repasá `tareas.md`.
   - Lo hecho hoy pasa a «Hecho», con su nota.
   - Lo nuevo que salió entra como tarea, con quién y para cuándo.
   - Las de Claude que quedaron «en curso» sin un chat abierto vuelven a «por hacer», con una nota.
   - Las notas con «para decisiones.md» van a `decisiones.md`.
3. **Estado:** reescribí `estado.md` en una página: qué pasó hoy, qué quedó abierto y qué toca mañana.
4. **Decisiones:** si hubo, van arriba de `decisiones.md`.
5. **Guardá:** `git pull --rebase`, `git add -A`, commit (`cierre: AAAA-MM-DD`) y push a `main`.
6. **Terminá con lo primero que hay que hacer mañana**, en una línea.
