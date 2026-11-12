# 01 · Cómo trabajamos

_Última actualización: {{FECHA}}._

- **Este repo es el cerebro.** Las reglas están en `reglas/`, el estado en `ESTADO.md`, las tareas en `tareas.md` y las decisiones en `decisiones.md`. Hay un orquestador y un agente por área (ver `CLAUDE.md`).
- **Modo honestidad:** Claude marca excusas, puntos ciegos e inconsistencias, y rompe los planes con fallas antes que el mercado. La vida personal queda afuera: acá se habla del negocio.
- **Gasto antes de generar:** antes de cualquier generación paga (voces, imágenes, video, API), Claude pasa la cuenta (cantidad × costo unitario = total, en créditos o en USD, y el saldo que queda) y espera el OK. Primero va una prueba chica en la calidad más barata y después el lote. _(A Axel se le fueron ~210 créditos en fotos sin presupuesto previo.)_
- **Meta por conector:** Claude lee campañas, conjuntos, métricas y el píxel cuando quiera. **No cambia nada en la cuenta sin un «sí» de {{NOMBRE}} en ese momento**, y eso incluye las pausas.
- **Cada cambio en Meta se anota** en `areas/campanas/registro.md`, lo haga quien lo haga: {{NOMBRE}}, un asesor o Claude.
- **Las ventas se cuentan en la plataforma de venta.** Meta atribuye de menos: a Axel le mostraba ~86% de las ventas reales.
- **Plata en dólares:** si cobrás en tu moneda y pagás la pauta en dólares, toda cuenta de ganancia se hace con lo que de verdad te cuesta cada dólar que cargás. No con el oficial ni con un número redondo (ver `02-ecuacion.md`).
- **Lo que se puede hacer ahora, se hace ahora.** Se espera solo con un motivo concreto, y se dice cuál:
  - que le corte el aprendizaje a Meta (por ejemplo, los 3 días sin tocar);
  - que choque con una promesa de precio o de fecha;
  - que dependa de un dato que todavía no está.
- **Una regla que no se puede medir es una opinión:** cada cambio dice cómo vamos a saber si funcionó.
- **Cerrar siempre:** cada tarea termina con `ESTADO.md` al día, la decisión anotada si la hubo, la tarea en «hecho» y commit + push.
