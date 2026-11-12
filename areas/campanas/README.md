# Campañas (Meta)

**Agente:** `campanas` · **Comando:** `/lectura` · **Reglas:** `reglas/06-meta.md` y `08-testing-y-escalado.md`.

## Estructura vigente

**Campaña «IA · Ventas · CBO»** `52619163206735`. Estado: **BORRADOR** (armada el 12/11/2026; no gasta hasta publicarla con el «sí» de los dueños).

| Qué | Valor |
|---|---|
| Cuenta | Velas arg `1611303950747523` |
| Objetivo | Ventas · CBO · puja de volumen más alto · en el borrador figura USD 8,33 por día, **pero se publica con presupuesto total de USD 45 en 72 horas** (decisión del 12/11) |
| Tope | Presupuesto **total** de USD 45 (unos USD 15 por día), con inicio y fin a las 72 horas, que se carga al publicar. 3 días sin tocar. No va como presupuesto diario: Meta puede pasarse hasta un 75% del diario en un día |
| Conjunto | «Test 1 · Argentina abierto» `52619163277535` · Argentina · 25–55 como sugerencia (Advantage+ audience) · Facebook, Instagram y Messenger (sin Audience Network) · optimiza por Compra en el píxel «velas» `1439230865058805` |
| Identidad | Página «La IA hace, vos vendés» `1492900110562845` · Instagram @laiahacevosvendes `17841452836464057` |
| Botón | Comprar · marcado «hecho con IA» · mejoras automáticas de Advantage+ creative apagadas |
| UTM | En el link de cada anuncio: `utm_source=facebook&utm_medium=paid&utm_campaign=ia-test1&utm_content=<anuncio>` |

| Anuncio | ID del anuncio | ID del creativo | Piezas |
|---|---|---|---|
| IA1 · Precio (video) | `52619163398735` | `1523779353140309` | video 4:5 en feed; video 9:16 en historias y reels |
| IA2 · Así es tu semana (carrusel) | `52619163400735` | `2899503597098509` | 6 tarjetas 4:5 |
| IA3 · No suena a vos | `52619163402135` | `2484283928764089` | imagen 4:5 / 9:16 |
| IA4 · Sol (video) | `52619163410735` | `1703396161298212` | video 4:5 / 9:16 |
| IA5 · El audio | `52619163414535` | `29174509452217250` | imagen 4:5 / 9:16 |

**Parámetros de URL de cada anuncio** (en Seguimiento → Parámetros de URL), para que la plataforma ate cada venta a su anuncio:

```
utm_source=facebook&utm_medium=paid&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&utm_id={{ad.id}}
```

## Qué hay acá

| Archivo | Qué es |
|---|---|
| `registro.md` | Cada cambio en la cuenta: quién lo hizo, qué cambió y por qué |
| `lecturas/AAAA-MM-DD.md` | La lectura de cada día |
