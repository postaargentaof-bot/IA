# Empezá acá

> Kit de arranque que armó Axel (EcomDigit) el 5/11/2026. Es el sistema con el que él vende un producto digital con Meta Ads, pero vacío y listo para tu negocio. Leelo entero una vez: son 10 minutos.

## Qué es esto, en 30 segundos

Vas a trabajar con Claude como si tuvieras un equipo. Hay un **orquestador** (el chat principal) y varios **agentes**: campañas, creativos, revisor, cerebro y Bilbao.

Los chats se olvidan de todo, así que la memoria la lleva **un repo de GitHub**. Cada chat lo lee al arrancar y lo actualiza al terminar.

```
              REPO EN GITHUB = la memoria del negocio
   CLAUDE.md · ESTADO.md · tareas.md · decisiones.md · reglas/ · areas/
          ▲                    ▲                     ▲
     lee y guarda         lee y guarda          lee y guarda
          │                    │                     │
   Chat principal        Chat «landing»        Chat «tanda 1»
   (orquestador)         (una sola tarea)      (una sola tarea)
```

**Lo que hace que funcione son tres ideas:**

1. **Lo que no está en el repo no existe.** Una decisión que quedó solo en un chat se pierde.
2. **Un chat, una tarea.** Podés tener 3 o 4 chats abiertos a la vez sin que se pisen, porque cada uno toca solo su área.
3. **Todo cierra igual:** con el estado al día, la decisión anotada y el push a GitHub. Así el próximo chat arranca sabiendo todo.

## Qué necesitás

| Qué | Para qué | Cuándo |
|---|---|---|
| Cuenta de GitHub (gratis) | El repo, que es la memoria | Día 1 |
| Un plan pago de Claude que incluya Claude Code | Los chats que trabajan sobre el repo | Día 1 |
| GitHub Desktop (gratis, opcional) | Subir el kit sin usar la terminal | Día 1 |
| El cerebro de Santiago Bilbao (gratis) | El método: ofertas, campañas y creativos | Día 1 |
| VS Code con la extensión Claude Code (opcional) | Trabajar en tu PC con archivos pesados, como los videos | Cuando hagas creativos |
| Business Manager de Meta, página, Instagram, cuenta publicitaria y tarjeta en dólares | Pautar | Antes del primer test |
| Plataforma de venta. Axel usa Impultienda con Mercado Pago; Hotmart también sirve | Landing, checkout, entrega, bump y upsell | Antes del primer test |

## Instalación (30–40 minutos)

### 1 · Subí el kit a un repo privado

1. **Descomprimí el zip.** Trae una carpeta oculta, `.claude`, con los agentes y los comandos. Aunque no la veas, está: no la borres.
   - En Windows: Explorador → Vista → Mostrar → Elementos ocultos.
   - En Mac: Cmd + Shift + punto.
2. **Opción fácil, con GitHub Desktop:**
   1. File → Add local repository → elegí la carpeta `cortex-ebooks`. Cuando avise que no es un repo, tocá «create a repository».
   2. Publish repository, **con «Keep this code private» tildado**.
3. **Opción terminal:** creá en github.com un repo privado y vacío, y después, desde la carpeta del kit:

```bash
git init && git add -A && git commit -m "arranque: kit de Axel"
```

```bash
git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
```

```bash
git branch -M main && git push -u origin main
```

**El repo va privado sí o sí:** ahí van a estar tus números, tus ofertas y tus decisiones.

### 2 · Conectá Claude Code al repo

- **Desde el navegador o el celular:** entrá a claude.ai/code, conectá tu GitHub, elegí el repo y abrí un chat nuevo.
- **Desde la PC:** VS Code → extensión Claude Code → abrí la carpeta del repo.

### 3 · Bajá el cerebro de Bilbao

Es gratis y lo publica él: **lp.santiagobilbao.com/cerebro/**. Junta todo lo que enseñó en su canal (más de 160 videos transcritos, con fecha), ordenado para que Claude te responda con su método.

1. Bajá el zip.
2. Copiá sus carpetas `WIKI/` y `RAW/` adentro de `conocimiento/bilbao/` de tu repo.
3. Copiá las 2 skills de bonus del zip (están en su carpeta oculta `.claude/skills/`) a `.claude/skills/` de tu repo. Una es la de **buscar ofertas**.
4. Subí los cambios con GitHub Desktop (Commit + Push).

**No viene en el kit a propósito:** es de Bilbao, lo actualiza seguido, y la regla del sistema es usar siempre lo más nuevo.

### 4 · El primer chat

Abrí un chat nuevo sobre el repo y escribí:

> Hola, arranquemos. Haceme la entrevista de arranque.

Claude te va a hacer unas 14 preguntas: quién sos, tu país, cuánta plata tenés para pautar, cuántas horas le dedicás, qué herramientas tenés y qué querés lograr. Con eso completa `CLAUDE.md`, `ESTADO.md`, `tareas.md` y la ecuación. **Desde ahí, el sistema ya es tuyo.**

### 5 · Los conectores (cuando llegues a pautar)

En claude.ai → Configuración → Conectores, sumá:

- **Meta Ads**, para que Claude lea tus campañas;
- el de tu plataforma de venta, si tiene (Impultienda tiene uno).

La regla: **Claude lee siempre, pero cambia algo en Meta solo con tu «sí» en ese momento.**

## Cómo se trabaja todos los días

| Momento | Qué hacés | Qué escribís |
|---|---|---|
| Al arrancar el día | En el chat principal, ves qué toca hoy | «¿Qué toca hoy?» |
| Cada tarea grande | Abrís un chat nuevo con un nombre corto, como «landing», «tanda 2» o «caza · recetas» | El primer mensaje que te deja el chat principal |
| Ideas, clases, videos, lo que dice un asesor | Lo sumás al cerebro | `/aprender` y lo que aprendiste |
| Con campañas andando | Lees cómo vienen | `/lectura` |
| Creativos | Armás una tanda de 5 | `/tanda` |
| Al terminar el día | Cerrás | `/cierre` |

**Así se conectan los chats:** no se hablan entre sí, se hablan **a través del repo**.

1. El chat principal crea la tarea en `tareas.md` y te deja **el primer mensaje** listo para el chat nuevo.
2. Ese chat la hace, deja el resultado en sus archivos y en la nota de su tarea, y sube los cambios.
3. El chat principal lo ve la próxima vez que lee el repo.

Detalle en `sistema/README.md`.

## Las reglas de oro (las mismas de Axel)

1. **Meta:** Claude lee siempre y cambia algo solo con tu «sí».
2. **Gasto antes de generar:** antes de gastar créditos (voces, imágenes, video), Claude te pasa la cuenta y espera tu OK.
3. **Nada falso:** ni testimonios, ni contadores, ni urgencias inventadas.
4. **Licencias:** todo lo que usás es tuyo, de dominio público o con licencia a tu nombre.
5. **Nada de cloaking**, nunca.
6. **Las ventas se cuentan en tu plataforma, no en Meta.**
7. **Bilbao manda, pero solo lo más nuevo y con la fecha a la vista.**

## Tus primeros 30 días

| Semana | Qué | Termina cuando |
|---|---|---|
| 1 | Armar las cuentas (Meta y plataforma) y cazar ofertas (`areas/ofertas/`) | Elegiste **una** oferta que pasa los 8 filtros de `reglas/03` |
| 2 | Producto MVP, bonos y bump; tienda y landing | La compra de prueba anda y el evento Compra aparece en Resumen del Administrador de eventos |
| 3 | De 5 a 10 creativos y lanzar el test: una CBO, 2–3 tickets por día, 3 días sin tocar | El test está al aire |
| 4 | Veredicto a los 5–7 días: escalar, ajustar o descartar | La decisión quedó en `decisiones.md` |

El tope de pérdida por oferta lo definís en la entrevista. Axel usa USD 200.

## Lo que Axel aprendió pagando (para que no lo pagues vos)

| Qué pasó | Qué regla salió |
|---|---|
| Se gastaron ~210 créditos de imágenes sin presupuesto previo | **Gasto antes de generar** |
| Meta le mostraba menos ventas de las que había: veía ~86% | La cuenta se juzga con las ventas de la plataforma |
| Cobra en pesos y paga la pauta en dólares | Las cuentas se hacen con lo que de verdad cuesta cada dólar que cargás |
| La demo de la plataforma traía testimonios hechos con IA, contadores y cupos falsos | Se apaga todo eso antes de pautar |
| Casi armó una estructura de campañas con un consejo de Bilbao que él ya había cambiado | **Solo contenido vigente, con fecha** |
| Un filtro que inventamos nosotros (45 días al aire) lo hacía llegar tarde a cada ola | Los filtros salen de la fuente, con fecha |
| Cambiar muchas cosas juntas en Meta no deja medir | **3 días sin tocar** después de arrancar |
| Sin bump ni upsell, no se puede pagar más por venta | El bump va desde el día 1 y el upsell, cuando la oferta valida |
| Un cambio en el checkout puede romper el evento Compra | Compra de prueba después de cada cambio |
| Facturar se deja para después y después es tarde | Factura por cada venta desde la primera (en Argentina, con el monotributo) |

## Qué hay en cada carpeta

| Dónde | Qué hay |
|---|---|
| `CLAUDE.md` | Las instrucciones del orquestador. Las lee cada chat al arrancar |
| `ESTADO.md` | Qué pasa hoy, en una página |
| `tareas.md` | El tablero de tareas: quién hace qué y para cuándo |
| `decisiones.md` | Cada decisión, con su fecha y su porqué. La más nueva va arriba |
| `reglas/` | El playbook: ecuación, ofertas, producto, landing, Meta, creativos, testeo y reglas de juego |
| `areas/` | El trabajo de cada área: ofertas, oferta, landing, creativos y campañas |
| `aprendizajes/` | Cómo entra al cerebro lo que vas aprendiendo |
| `conocimiento/` | Las fuentes (el cerebro de Bilbao, cursos, videos) |
| `sistema/` | Cómo funciona este sistema |
| `archivo/` | Lo viejo. Se busca ahí cuando hace falta, pero no se carga en cada chat |
| `.claude/` | Los agentes y los comandos (`/arranque`, `/lectura`, `/tanda`, `/aprender`, `/cierre`) |

## Dudas

- **Del sistema:** preguntale a Claude «¿cómo funciona este sistema?» (lo va a leer de `sistema/README.md`).
- **Del negocio:** a Axel.
