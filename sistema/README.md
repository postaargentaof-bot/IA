# Cómo funciona este Cortex

## Las piezas

| Pieza | Qué es | Quién la escribe |
|---|---|---|
| `CLAUDE.md` | Las instrucciones del orquestador: cómo hablar, qué leer, cómo cerrar y las reglas que no se rompen | Claude, con el OK de {{NOMBRE}} |
| `ESTADO.md` | La foto de hoy, en una página | El chat principal o `/cierre` |
| `tareas.md` | El tablero de tareas | Cada chat, solo la fila de su tarea |
| `decisiones.md` | La historia de las decisiones | El chat principal o `/cierre` |
| `reglas/` | El cómo de cada cosa | Solo con `/aprender` y un sí |
| `areas/` | El trabajo de cada área | El chat de esa área |
| `.claude/agents/` | Los especialistas a los que delega el orquestador | Se tocan poco |
| `.claude/skills/` | Los comandos (`/lectura`, `/tanda`…) | Se tocan poco |

## Un día normal

```
Mañana    Chat principal: «¿qué toca hoy?» → lee estado + tareas → te dice las 3 cosas que mueven la plata
          (con campañas andando) /lectura → semáforo + propuestas → vos decís sí / no
Durante   Un chat por tarea grande, cada uno con su primer mensaje
          Las ideas que te llegan → /aprender
Noche     /cierre → tareas, estado y decisiones al día, y push
```

## Chats en paralelo (cómo se conectan)

Los chats no se hablan entre sí: **se hablan a través del repo.**

1. **El chat principal crea la tarea** en `tareas.md` y te deja el primer mensaje del chat nuevo.
2. **Abrís un chat nuevo sobre el repo**, con un nombre corto que diga qué hace: «landing», «tanda 3», «caza · recetas», «producto», «test · <oferta>».
3. **El chat trabaja solo en los archivos de su área.** Al terminar:
   - pasa su tarea a «hecho» y le deja una nota;
   - si decidiste algo, lo marca en la nota con «para decisiones.md»;
   - hace commit y push.
4. **El chat principal (o `/cierre`)** lee las notas y pasa lo decidido a `ESTADO.md` y a `decisiones.md`.

**Plantilla del primer mensaje de un chat paralelo:**

```
Sos el chat «<nombre>» del Cortex de {{NEGOCIO}}. Tarea: «<título de la tarea en tareas.md>» (pasala a «en curso» con este chat).
Leé primero CLAUDE.md, <README del área> y <las reglas que tocan>.
Qué hay que hacer: <qué, con qué criterio y para cuándo>.
Qué NO tocar: ESTADO.md, decisiones.md y los archivos de otras áreas.
Al terminar: tarea en «hecho» con una nota, commit y push a main.
```

**Cuántos chats a la vez:** los que puedas seguir. El límite no es Claude: es que vos puedas contestar las preguntas de cada uno.

## Ramas y push

Todo se sube a `main` (`git push origin HEAD:main`). Si el chat trabaja en una rama propia (pasa en claude.ai/code), sube a esa rama **y** a `main`. Si no se sube a `main`, el próximo chat no ve el trabajo.

## Fase 2: un Centro visual (opcional)

Cuando tengas ventas, podés pedirle a Claude un tablero propio: «armame un Centro como el de Axel». Es una página privada en claude.ai con:

- **Hoy**;
- **Tareas**, para tildar desde el celular;
- **Campañas**, con el semáforo;
- **Ventas**;
- **Cerebro**.

Usa su propia base de datos. Hasta entonces, `tareas.md` y `ESTADO.md` hacen el mismo trabajo.

## Fase 3: lecturas automáticas (opcional)

Con campañas andando, Claude puede correr la lectura solo todas las mañanas (una tarea programada) y dejarla en `areas/campanas/lecturas/`. Se arma cuando haya algo que leer.
