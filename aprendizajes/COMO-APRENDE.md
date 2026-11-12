# Cómo aprende el Cortex

{{NOMBRE}} aprende todo el tiempo: clases, videos, lo que ve en Meta, lo que dice un asesor, lo que hace la competencia. El cerebro tiene que crecer con eso **sin perder lo que ya funciona**.

## El ciclo, en 4 pasos

```
  1. ENTRA             2. SE PROCESA           3. DECIDE {{NOMBRE}}   4. QUEDA
  /aprender o un       El agente «cerebro»     Sí / No / Probar       Regla editada
  archivo en           lo clasifica y lo                              + decisiones.md
  aprendizajes/        contrasta con las                              + commit
  bandeja/             reglas vigentes
```

### 1. Entra

- **En un chat:** `/aprender` y lo que aprendiste (con el link, si hay).
- **Un archivo** en `aprendizajes/bandeja/`, por ejemplo las notas de una clase.

### 2. Se procesa

El agente `cerebro` clasifica cada aprendizaje en uno de estos tipos:

| Tipo | Qué es | Qué pasa |
|---|---|---|
| **Cambia una regla** | Contradice o mejora algo de `reglas/` | Una propuesta de cambio, con el antes y el después |
| **Táctica a probar** | Algo que hay que testear antes de que sea regla | Va como prueba a `ESTADO.md`, con su criterio de éxito |
| **Conocimiento** | Contexto útil que todavía no cambia nada | Se resume en `conocimiento/` |
| **Ya lo sabíamos** | Repite una regla vigente | Se marca como confirmación: suma evidencia |

Para cada uno dice:

- de dónde viene;
- qué tipo de fuente es: Bilbao (con video y fecha), un dato propio, la práctica de otro que vende algo parecido o una opinión;
- qué regla toca.

**Si contradice algo que nuestros números ya probaron, lo dice.**

### 3. Decide {{NOMBRE}}

Nada cambia en `reglas/` sin un sí. Las respuestas posibles son:

- **Sí:** se aplica.
- **No:** queda descartado, con el motivo.
- **Probar:** entra como test, con fecha y criterio.

### 4. Queda

Con el sí, el orquestador:

1. edita la regla y le actualiza la fecha;
2. anota en `decisiones.md` qué cambió, por qué y de dónde salió;
3. mueve el aprendizaje a `aprendizajes/procesados/AAAA-MM.md`;
4. hace commit (`reglas: …`) y push.

La versión anterior de cada regla queda en el historial de git: nada se pierde.

## Regla de oro

**Una regla nueva que no se puede medir es una opinión.** Cada cambio dice cómo vamos a saber si funcionó.
