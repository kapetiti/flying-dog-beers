import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import kaggle
import os
import pandas as pd

p = pd.read_csv(r"https://storage.googleapis.com/kagglesdsdata/datasets/549702/1159896/brazil_covid19.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1589853272&Signature=DKAi9dyP8LNUA7%2BOPiYrf8N23R4I5dr9sBW1iML1RQVFlyG3JfdI0S%2FRCQfgXYyYLW0Uni0ZsYkeQXLg1b5GfLIK8hehB%2B8cXJww1ZEBYCacwyPTonlcZ37GM0qOcZb3WmM5ctHt3vDEr4iIEN9p4gjuj8GqJvpsDvMt%2FrRtDP0dX%2FyKtQ8uCTARt%2BkStP7vjbV7CZBPuFeOBYdOt2Dk%2Bt%2F9qV6WgeMOnAFE1%2BkB5TKsNgNpqa%2BC8An5JR9%2BFwZS6%2B9i9Ng9h%2FLdswNY5UHgGlhtUoVegS%2F4VPWYkhcWQZU2DKGHPg9L5Raywxb4d5FDo%2FGpsK3z9iVLigoX8bsTjA%3D%3D&response-content-disposition=attachment%3B+filename%3Dbrazil_covid19.csv")


########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
x = np.linspace(0, 10, 1000)
y1 = np.sin(x)
y2 = np.cos(x)
color1='blue'
color2='red'
mytitle='Shazam'
tabtitle='!BIRL!'
myheading='*GRÁFICOS CARALHO*'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
bitterness = go.Scatter(
    x=x,
    y=y1,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Scatter(
    x=x,
    y=y2,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

a = p[p.state == "Alagoas"]
d = np.linspace(0, 1, len(a["cases"]))
graph = go.Scatter(
	x=d
	y=a["cases"]
)

dat = [graph]

beer_fig = go.Figure(data=dat, layout=beer_layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
