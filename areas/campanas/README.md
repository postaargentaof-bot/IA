# Campañas (Meta)

**Agente:** `campanas` · **Comando:** `/lectura` · **Reglas:** `reglas/06-meta.md` y `08-testing-y-escalado.md`.

## Estructura vigente

Se completa cuando se publica la primera campaña: nombre, ID, presupuesto y armado.

| Conjunto | ID | Mínimo | Anuncios (nombre e ID) |
|---|---|---|---|

**Parámetros de URL de cada anuncio** (en Seguimiento → Parámetros de URL), para que la plataforma ate cada venta a su anuncio:

```
utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&utm_id={{ad.id}}
```

## Qué hay acá

| Archivo | Qué es |
|---|---|
| `registro.md` | Cada cambio en la cuenta: quién lo hizo, qué cambió y por qué |
| `lecturas/AAAA-MM-DD.md` | La lectura de cada día |
