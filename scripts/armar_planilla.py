"""Arma el bump «La planilla lista para usar» (xlsx, compatible con Google Sheets)."""
import sys
from datetime import date
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.comments import Comment

OUT = sys.argv[1]
F = "Arial"
VIOLETA = "5B3FD1"
CLARO = "EEEAFB"
AMARILLO = "FFF4C2"
h_font = Font(name=F, bold=True, color="FFFFFF", size=11)
h_fill = PatternFill("solid", fgColor=VIOLETA)
in_fill = PatternFill("solid", fgColor=AMARILLO)
tot_fill = PatternFill("solid", fgColor=CLARO)
base = Font(name=F, size=11)
bold = Font(name=F, size=11, bold=True)
title = Font(name=F, size=18, bold=True, color=VIOLETA)
sub = Font(name=F, size=11, italic=True, color="555555")
thin = Side(style="thin", color="D0D0D0")
box = Border(left=thin, right=thin, top=thin, bottom=thin)
PESOS = '"$" #,##0;-"$" #,##0;"-"'
FECHA = "dd/mm/yyyy"
N = 500  # filas de datos

wb = Workbook()

def header(ws, row, cols, widths):
    for i, (c, w) in enumerate(zip(cols, widths), start=1):
        cell = ws.cell(row=row, column=i, value=c)
        cell.font, cell.fill, cell.border = h_font, h_fill, box
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[cell.column_letter].width = w
    ws.row_dimensions[row].height = 30
    ws.freeze_panes = ws.cell(row=row + 1, column=1)

def titulo(ws, t, s):
    ws["A1"], ws["A2"] = t, s
    ws["A1"].font, ws["A2"].font = title, sub
    ws.sheet_view.showGridLines = False

def fmt_rows(ws, first, last, ncols, formats):
    for r in range(first, last + 1):
        for c in range(1, ncols + 1):
            cell = ws.cell(row=r, column=c)
            cell.font, cell.border = base, box
            if c in formats:
                cell.number_format = formats[c]

def dv_list(ws, items, rng):
    dv = DataValidation(type="list", formula1='"' + ",".join(items) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(rng)

# ---------- Cómo usar ----------
ws = wb.active
ws.title = "Cómo usar"
titulo(ws, "La planilla de tu negocio", "Bonus de «La IA hace, vos vendés»")
ws.column_dimensions["A"].width = 100
lineas = [
    ("Cómo subirla a Google Sheets", True),
    ("1. Entrá a drive.google.com con tu cuenta de Google.", False),
    ("2. Tocá «Nuevo» → «Subir archivo» y elegí este archivo.", False),
    ("3. Abrilo y andá a «Archivo» → «Guardar como Hojas de cálculo de Google». Listo: ya la podés usar desde el celular con la app Hojas de cálculo.", False),
    ("", False),
    ("Qué hay en cada pestaña", True),
    ("• Ventas: anotá cada venta el mismo día.", False),
    ("• Gastos: anotá cada gasto, marcando si es material o gasto fijo.", False),
    ("• Pedidos: tus pedidos o turnos. La fila se pinta sola según el estado (rojo = entrega en menos de 48 h).", False),
    ("• Costos: la calculadora del Día 4. Te dice cuánto te cuesta un producto y a qué precio venderlo.", False),
    ("• Resumen: elegí el mes y te dice cuánto vendiste, cuánto gastaste y cuánto te quedó.", False),
    ("", False),
    ("Reglas", True),
    ("• Escribí solo en las celdas AMARILLAS (en Costos y Resumen) y en las filas de las tablas. Lo demás se calcula solo.", False),
    ("• Cada pestaña trae una fila de EJEMPLO en gris. Borrala (o escribí encima) cuando cargues lo tuyo.", False),
    ("• Las columnas con flechita tienen opciones para elegir: tocá la celda y elegí.", False),
    ("• Los números se revisan con la calculadora la primera vez: si algo no te cierra, pegale la fórmula a la IA y preguntale qué hace.", False),
]
for i, (t, b) in enumerate(lineas, start=4):
    c = ws.cell(row=i, column=1, value=t)
    c.font = Font(name=F, size=12 if b else 11, bold=b, color=VIOLETA if b else "222222")
    c.alignment = Alignment(wrap_text=True, vertical="top")

gris = Font(name=F, size=11, italic=True, color="888888")

# ---------- Ventas ----------
ws = wb.create_sheet("Ventas")
titulo(ws, "Ventas", "Una fila por venta. Anotala el mismo día.")
cols = ["Fecha", "Cliente", "Qué compró", "Cantidad", "Precio unitario", "Total", "Medio de pago"]
header(ws, 4, cols, [13, 22, 32, 11, 16, 16, 18])
fmt_rows(ws, 5, 4 + N, 7, {1: FECHA, 5: PESOS, 6: PESOS})
for r in range(5, 5 + N):
    ws.cell(row=r, column=6, value=f'=IF(OR(D{r}="",E{r}=""),"",D{r}*E{r})')
ej = [date(2026, 11, 3), "Ejemplo: Ana", "Ejemplo: torta 20 porciones", 1, 66000]
for c, v in enumerate(ej, start=1):
    ws.cell(row=5, column=c, value=v).font = gris
ws.cell(row=5, column=7, value="Transferencia").font = gris
dv_list(ws, ["Efectivo", "Transferencia", "Mercado Pago", "Tarjeta", "Otro"], f"G5:G{4+N}")

# ---------- Gastos ----------
ws = wb.create_sheet("Gastos")
titulo(ws, "Gastos", "Todo lo que sale: materiales, envíos, luz, publicidad, etc.")
cols = ["Fecha", "En qué", "Tipo", "Monto"]
header(ws, 4, cols, [13, 40, 20, 16])
fmt_rows(ws, 5, 4 + N, 4, {1: FECHA, 4: PESOS})
for c, v in enumerate([date(2026, 11, 2), "Ejemplo: harina, manteca y huevos", "Material", 18000], start=1):
    ws.cell(row=5, column=c, value=v).font = gris
dv_list(ws, ["Material", "Gasto fijo", "Envío", "Publicidad", "Otro"], f"C5:C{4+N}")

# ---------- Pedidos ----------
ws = wb.create_sheet("Pedidos")
titulo(ws, "Pedidos y turnos", "Rojo = se entrega en menos de 48 h · Amarillo = en proceso · Verde = entregado")
cols = ["Fecha del pedido", "Cliente", "Qué pidió", "Entrega / turno", "Monto", "Seña cobrada", "Saldo", "Estado"]
header(ws, 4, cols, [15, 22, 32, 16, 15, 15, 15, 15])
fmt_rows(ws, 5, 4 + N, 8, {1: FECHA, 4: FECHA, 5: PESOS, 6: PESOS, 7: PESOS})
for r in range(5, 5 + N):
    ws.cell(row=r, column=7, value=f'=IF(E{r}="","",E{r}-N(F{r}))')
for c, v in enumerate([date(2026, 11, 1), "Ejemplo: Laura", "Ejemplo: mesa dulce 30 personas", date(2026, 11, 15), 120000, 40000], start=1):
    ws.cell(row=5, column=c, value=v).font = gris
ws.cell(row=5, column=8, value="Pendiente").font = gris
dv_list(ws, ["Pendiente", "En proceso", "Listo", "Entregado"], f"H5:H{4+N}")
rng = f"A5:H{4+N}"
ws.conditional_formatting.add(rng, FormulaRule(formula=['$H5="Entregado"'], fill=PatternFill("solid", fgColor="D9F2DC"), stopIfTrue=True))
ws.conditional_formatting.add(rng, FormulaRule(formula=['AND($D5<>"",$D5-TODAY()<=2)'], fill=PatternFill("solid", fgColor="F8D2D2"), stopIfTrue=True))
ws.conditional_formatting.add(rng, FormulaRule(formula=['$H5="En proceso"'], fill=PatternFill("solid", fgColor="FFF1C4"), stopIfTrue=True))
ws.conditional_formatting.add(rng, FormulaRule(formula=['$H5="Listo"'], fill=PatternFill("solid", fgColor="DDE8FA"), stopIfTrue=True))

# ---------- Costos ----------
ws = wb.create_sheet("Costos")
titulo(ws, "Calculadora de costos y precio", "Completá las celdas amarillas. El resto se calcula solo. (Día 4 del libro)")
ws.column_dimensions["A"].width = 44
ws.column_dimensions["B"].width = 18
ws.column_dimensions["C"].width = 18
ws.column_dimensions["D"].width = 18

def lab(r, t, b=False):
    c = ws.cell(row=r, column=1, value=t)
    c.font = bold if b else base

def inp(r, v, f=PESOS, col=2):
    c = ws.cell(row=r, column=col, value=v)
    c.fill, c.font, c.border, c.number_format = in_fill, base, box, f

def calc(r, formula, f=PESOS, col=2, strong=False):
    c = ws.cell(row=r, column=col, value=formula)
    c.font = bold if strong else base
    c.border, c.number_format = box, f
    if strong:
        c.fill = tot_fill

lab(4, "Producto o servicio", True); inp(4, "Ejemplo: torta 20 porciones", "@")
lab(6, "1 · MATERIALES (por unidad)", True)
ws["A7"], ws["B7"] = "Material", "Costo"
for c in ("A7", "B7"):
    ws[c].font, ws[c].fill = h_font, h_fill
mats = [("Ingredientes", 18000), ("Caja y base", 3500), ("", None), ("", None), ("", None), ("", None)]
for i, (n, v) in enumerate(mats, start=8):
    c = ws.cell(row=i, column=1, value=n); c.fill, c.font, c.border = in_fill, base, box
    inp(i, v)
lab(14, "Total materiales"); calc(14, "=SUM(B8:B13)", strong=True)

lab(16, "2 · TU TIEMPO", True)
lab(17, "Horas que te lleva una unidad"); inp(17, 5, "0.0")
lab(18, "Cuánto vale tu hora"); inp(18, 6000)
lab(19, "Total tiempo"); calc(19, "=B17*B18", strong=True)

lab(21, "3 · GASTOS DEL NEGOCIO (repartidos)", True)
lab(22, "Gastos fijos del mes (luz, gas, internet, alquiler…)"); inp(22, 30000)
lab(23, "Unidades que vendés por mes"); inp(23, 20, "0")
lab(24, "Gastos fijos por unidad"); calc(24, '=IF(N(B23)=0,0,B22/B23)', strong=True)

lab(26, "COSTO TOTAL POR UNIDAD", True); calc(26, "=B14+B19+B24", strong=True)

lab(28, "4 · PRECIO", True)
lab(29, "Comisión del cobro (Mercado Pago, tarjeta). Mirala en tu cuenta"); inp(29, 0, "0.0%")
ws["B29"].comment = Comment("Poné la comisión que te cobran, como porcentaje. Si cobrás en efectivo o transferencia, dejá 0%.", "Planilla")
lab(30, "Lo que cobrás hoy"); inp(30, 45000)

ws["A32"], ws["B32"], ws["C32"], ws["D32"] = "Ganancia sobre el costo", "20%", "30%", "40%"
for c in ("A32", "B32", "C32", "D32"):
    ws[c].font, ws[c].fill = h_font, h_fill
    ws[c].alignment = Alignment(horizontal="center")
ws["A33"] = "Margen"; ws["A34"] = "Precio sugerido (con comisión)"; ws["A35"] = "Te queda limpio por unidad"
for col, m in zip("BCD", (0.2, 0.3, 0.4)):
    inp(33, m, "0%", col=" BCD".index(col) + 1)
    calc(34, f'=IF(N($B$29)>=1,"",$B$26*(1+{col}33)/(1-N($B$29)))', col=" BCD".index(col) + 1, strong=True)
    calc(35, f'=IF({col}34="","",{col}34*(1-N($B$29))-$B$26)', col=" BCD".index(col) + 1)
for r in (33, 34, 35):
    ws.cell(row=r, column=1).font = base

lab(37, "Con lo que cobrás hoy, te queda por unidad"); calc(37, "=B30*(1-N(B29))-B26", strong=True)
lab(38, "¿Cubre el costo?"); calc(38, '=IF(B37>=0,"Sí","NO: estás perdiendo plata")', "@", strong=True)

# ---------- Resumen ----------
ws = wb.create_sheet("Resumen")
titulo(ws, "Resumen del mes", "Escribí el primer día del mes en la celda amarilla (ej.: 01/11/2026).")
ws.column_dimensions["A"].width = 36
ws.column_dimensions["B"].width = 20
ws["A4"] = "Mes"; ws["A4"].font = bold
ws["B4"] = date(2026, 11, 1)
ws["B4"].fill, ws["B4"].font, ws["B4"].border, ws["B4"].number_format = in_fill, bold, box, "mmmm yyyy"
V, G = f"Ventas!$A$5:$A${4+N}", f"Gastos!$A$5:$A${4+N}"
rango_mes = '">="&$B$4,{d},"<"&EDATE($B$4,1)'
filas = [
    (6, "Total vendido", f'=SUMIFS(Ventas!$F$5:$F${4+N},{V},">="&$B$4,{V},"<"&EDATE($B$4,1))'),
    (7, "Cantidad de ventas", f'=COUNTIFS({V},">="&$B$4,{V},"<"&EDATE($B$4,1))'),
    (8, "Venta promedio", '=IF(B7=0,0,B6/B7)'),
    (10, "Gastos en materiales", f'=SUMIFS(Gastos!$D$5:$D${4+N},{G},">="&$B$4,{G},"<"&EDATE($B$4,1),Gastos!$C$5:$C${4+N},"Material")'),
    (11, "Otros gastos", '=B12-B10'),
    (12, "Total gastado", f'=SUMIFS(Gastos!$D$5:$D${4+N},{G},">="&$B$4,{G},"<"&EDATE($B$4,1))'),
    (14, "LO QUE TE QUEDÓ", '=B6-B12'),
]
for r, t, f in filas:
    ws.cell(row=r, column=1, value=t).font = bold if r == 14 else base
    c = ws.cell(row=r, column=2, value=f)
    c.font, c.border = (bold if r in (6, 12, 14) else base), box
    c.number_format = "0" if r == 7 else PESOS
    if r == 14:
        c.fill = tot_fill
ws["A16"] = "Ventas del mes por medio de pago"; ws["A16"].font = bold
for i, m in enumerate(["Efectivo", "Transferencia", "Mercado Pago", "Tarjeta", "Otro"], start=17):
    ws.cell(row=i, column=1, value=m).font = base
    c = ws.cell(row=i, column=2, value=f'=SUMIFS(Ventas!$F$5:$F${4+N},{V},">="&$B$4,{V},"<"&EDATE($B$4,1),Ventas!$G$5:$G${4+N},A{i})')
    c.font, c.border, c.number_format = base, box, PESOS

for s in wb.worksheets:
    s.sheet_properties.tabColor = VIOLETA
wb.save(OUT)
print("ok", OUT)
