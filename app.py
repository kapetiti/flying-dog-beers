# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

x = np.linspace(0, 10, 1000)
graph = go.Scatter(
	x=x,
	y=np.sin(x)
)

dat = [graph]

beer_fig = go.Figure(data=dat, layout=beer_layout)

app = dash.Dash(__name__)
server = app.server
app.title = "nsjdfkjsd"
app.layout = html.Div([
    dcc.Slider(
        id='my-slider',
        min=0,
        max=20,
        step=0.5,
        value=10,
    ),
    html.Div(id='slider-output-container'),
	dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
])


@app.callback(
    [Output('slider-output-container', 'children'),
	 Output('flyingdog', 'figure')],
    [Input('my-slider', 'value')])
def update_output(value):
	
	y = np.sin(value*x)

	graph = go.Scatter(
		x=x,
		y=np.sin(x)
	)
	
	dat = [graph]

	beer_fig = go.Figure(data=dat, layout=beer_layout)

    return 'You have selected "{}"'.format(value), beer_fig
	

if __name__ == '__main__':
    app.run_server(debug=True)
