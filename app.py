
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Carrega o arquivo CSV
df = pd.read_csv("ecommerce_estatistica.csv")

# Inicializa o app
app = Dash(__name__)
app.title = "Dashboard Ecommerce"

# Layout do app
app.layout = html.Div([
    html.H1("Dashboard de Análise - Ecommerce", style={"textAlign": "center"}),

    dcc.Graph(
        id='histograma',
        figure=px.histogram(df, x='Preco', nbins=30, title='Distribuição de Preços')
    ),

    dcc.Graph(
        id='dispersao',
        figure=px.scatter(df, x='Preco', y='Quantidade', color='Categoria',
                          title='Relação entre Preço e Quantidade')
    ),

    dcc.Graph(
        id='mapa_calor',
        figure=px.imshow(df.corr(numeric_only=True), text_auto=True,
                         title='Mapa de Calor das Correlações')
    ),

    dcc.Graph(
        id='barra',
        figure=px.bar(df.groupby('Categoria')['Quantidade'].sum().reset_index(),
                      x='Categoria', y='Quantidade', title='Quantidade por Categoria')
    ),

    dcc.Graph(
        id='pizza',
        figure=px.pie(df, names='Categoria', title='Distribuição de Categorias')
    ),

    dcc.Graph(
        id='densidade',
        figure=px.density_contour(df, x='Preco', y='Quantidade',
                                  title='Densidade de Preço vs Quantidade')
    ),

    dcc.Graph(
        id='regressao',
        figure=px.scatter(df, x='Preco', y='Quantidade', trendline='ols',
                          title='Regressão Linear: Preço vs Quantidade')
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
