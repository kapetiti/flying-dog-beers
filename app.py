# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

x1 = np.linspace(0, 10, 1000)
graph = go.Scatter(
	x=x1,
	y=np.sin(x1)
)

dat = [graph]

beer_fig = go.Figure(data=dat)

app = dash.Dash(__name__)
server = app.server
app.title = "nsjdfkjsd"
app.layout = html.Div([
    dcc.Slider(
        id='my-slider',
        min=0,
        max=20,
        step=0.5,
        value=1,
    ),
    html.Div(id='slider-output-container'),
	dcc.Graph(id='flyingdog'),
])


@app.callback(
    [Output('slider-output-container', 'children'), Output('flyingdog', 'figure')],
    [Input('my-slider', 'value')])
def update_output(value):

	return 'You have selected "{}"'.format(value), 
	{"data": [{"x":x1, "y":np.sin(value*x1), "name":"sin({}x)".format(value), "showlegend":True}],
	 "layout": [{"width":800, "height":500}]}
	

if __name__ == '__main__':
    app.run_server(debug=True)
