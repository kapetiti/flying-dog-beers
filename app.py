# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

x1 = np.linspace(0, 10, 1000)

app = dash.Dash(__name__)
server = app.server
app.title = "nsjdfkjsd"
app.layout = html.Div([
	dcc.Graph(id='flyingdog'),
	html.Div(
	[
		html.P(id='slider-output-container'),    
		dcc.Slider(
		    id='my-slider',
		    min=0,
		    max=20,
		    step=0.5,
		    value=1,
	    ),
	],
	style={"width":500}
	),
])


@app.callback(
    [Output('slider-output-container', 'children'), Output('flyingdog', 'figure')],
    [Input('my-slider', 'value')])
def update_output(value):

	return 'You have selected "{}"'.format(value), {"data": [{"x":x1, "y":np.sin(value*x1), "name":"sin({}x)".format(value), "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":0, "r":0, "t":0, "b":0}}}
	

if __name__ == '__main__':
    app.run_server(debug=True)
