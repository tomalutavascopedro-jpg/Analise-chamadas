import plotly.express as px

Meses = ["Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro"]
Chamada = [12000, 14500, 9000, 20000, 17000, 35000, 40000]
Região = ["Huambo", "Benguela", "Moxico", "Mbanza Congo", "Bengo", "Uíge", "Luanda"]

fig = px.bar(
    x=Meses,
    y=Chamada,
    color=Região,
    text=Chamada,
    title="Avaliação das Chamadas",
    labels={"x": "Meses", "y": "Chamadas", "color": "Região"},
)

# Gráfico em HTML (sem página completa), para colocar dentro da nossa página
grafico_html = fig.to_html(full_html=False, include_plotlyjs="cdn")

pagina = f"""<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gráfico de Chamadas</title>
  <style>
    body {{ font-family: Arial, Helvetica, sans-serif; margin: 0; padding: 40px 20px; background: #ffffff; color: #111111; }}
    .container {{ max-width: 1070px; margin: 0 auto; }}
    a.voltar {{ display: inline-block; margin-bottom: 20px; color: #1c2733; text-decoration: none; font-weight: bold; }}
    a.voltar:hover {{ text-decoration: underline; }}
  </style>
</head>
<body>
  <div class="container">
    <a class="voltar" href="index.html">← Voltar</a>
    {grafico_html}
  </div>
</body>
</html>
"""

with open("grafico.html", "w", encoding="utf-8") as f:
    f.write(pagina)

print("Ficheiro grafico.html criado com sucesso.")
