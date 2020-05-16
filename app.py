import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import kaggle
import os
import pandas as pd

kaggle.api.authenticate()
kaggle.api.dataset_download_files("unanimad/corona-virus-brazil", "brazil-covid")
os.chdir("brazil-covid")
os.system("unzip corona-virus-brazil.zip")
os.chdir("..")
os.system("git add .")
os.system('git commit -m "test"')
os.system("git push")

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
