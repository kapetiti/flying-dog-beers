# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

x1 = np.linspace(0, 10, 1000)

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
server = app.server
app.title = "nsjdfkjsd"

layout_home = html.Div([
	html.Div(
		style={"height":100, "background-color":"#9015BD","display":"flex"},
		children=[
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("SHIT IS REAL")], href="/"),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("sin(x)")], href="/page-sin"),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("cos(x)")], href="/page-cos"),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					html.A([html.H1("GitHub")], href="https://github.com/joaopedro-vm/flying-dog-beers", target="_blank"),
				],
			),
		],
	),
])

fig_sin = {"data": [{"x":x1, "y":np.sin(x1), "name":"sin(1x)", "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":0, "r":0, "t":0, "b":0}}}
fig_cos = {"data": [{"x":x1, "y":np.cos(x1), "name":"cos(1x)", "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":0, "r":0, "t":0, "b":0}}}

layout_sin = html.Div([
	html.Div(
		style={"height":100, "background-color":"#9015BD","display":"flex"},
		children=[
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("SHIT IS REAL")], href="/"),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("sin(x)")], href="/page-sin"),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("cos(x)")], href="/page-cos"),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					html.A([html.H1("GitHub")], href="https://github.com/joaopedro-vm/flying-dog-beers", target="_blank"),
				],
			),
		],
	),
	html.Div(style={"height":20}),
	dcc.Graph(id='graph-sin', figure=fig_sin),
	html.Div(
	[
		html.P(id='slider-out-sin', children=['Angular Frequency: 1']),    
		dcc.Slider(
		    id='slider-sin',
		    min=0,
		    max=20,
		    step=0.5,
		    value=1,
	    ),
	],
	style={"width":500}
	),
])

layout_cos = html.Div([
	html.Div(
		style={"height":100, "background-color":"#9015BD","display":"flex"},
		children=[
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("SHIT IS REAL")], href="/"),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("sin(x)")], href="/page-sin"),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("cos(x)")], href="/page-cos"),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					html.A([html.H1("GitHub")], href="https://github.com/joaopedro-vm/flying-dog-beers", target="_blank"),
				],
			),
		],
	),
	html.Div(style={"height":20}),
	dcc.Graph(id='graph-cos', figure=fig_cos),
	html.Div(
	[
		html.P(id='slider-out-cos', children=['Angular Frequency: 1']),    
		dcc.Slider(
		    id='slider-cos',
		    min=0,
		    max=20,
		    step=0.5,
		    value=1,
	    ),
	],
	style={"width":500}
	),
])

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

app.layout = url_bar_and_content_div

app.validation_layout = html.Div([
	url_bar_and_content_div,
    layout_home,
    layout_sin,
    layout_cos,
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/page-sin":
        return layout_sin
    elif pathname == "/page-cos":
        return layout_cos
    else:
        return layout_home

@app.callback(
    [Output('slider-out-sin', 'children'), Output('graph-sin', 'figure')],
    [Input('slider-sin', 'value')])
def update_output(value):

	return 'Angular Frequency: {}'.format(value), {"data": [{"x":x1, "y":np.sin(value*x1), "name":"sin({}x)".format(value), "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":0, "r":0, "t":0, "b":0}}}

@app.callback(
    [Output('slider-out-cos', 'children'), Output('graph-cos', 'figure')],
    [Input('slider-cos', 'value')])
def update_output(value):

	return 'Angular Frequency: {}'.format(value), {"data": [{"x":x1, "y":np.cos(value*x1), "name":"cos({}x)".format(value), "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":0, "r":0, "t":0, "b":0}}}
	

if __name__ == '__main__':
    app.run_server(debug=True)
