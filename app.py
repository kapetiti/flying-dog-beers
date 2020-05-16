# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd

p = pd.read_csv(r"https://storage.googleapis.com/kagglesdsdata/datasets/549702/1159896/brazil_covid19.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1589853272&Signature=DKAi9dyP8LNUA7%2BOPiYrf8N23R4I5dr9sBW1iML1RQVFlyG3JfdI0S%2FRCQfgXYyYLW0Uni0ZsYkeQXLg1b5GfLIK8hehB%2B8cXJww1ZEBYCacwyPTonlcZ37GM0qOcZb3WmM5ctHt3vDEr4iIEN9p4gjuj8GqJvpsDvMt%2FrRtDP0dX%2FyKtQ8uCTARt%2BkStP7vjbV7CZBPuFeOBYdOt2Dk%2Bt%2F9qV6WgeMOnAFE1%2BkB5TKsNgNpqa%2BC8An5JR9%2BFwZS6%2B9i9Ng9h%2FLdswNY5UHgGlhtUoVegS%2F4VPWYkhcWQZU2DKGHPg9L5Raywxb4d5FDo%2FGpsK3z9iVLigoX8bsTjA%3D%3D&response-content-disposition=attachment%3B+filename%3Dbrazil_covid19.csv")
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
					dcc.Link([html.H1("sin2(x)")], href="/page-sin2"),
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
					dcc.Link([html.H1("sin2(x)")], href="/page-sin2"),
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

layout_sin2 = html.Div([
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
					dcc.Link([html.H1("sin2(x)")], href="/page-sin2"),
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
	dcc.Graph(id='graph-sin2', figure=fig_sin),
	html.Div(
	[
		html.P(id='drop-out-sin2', children=['Angular Frequency:']),    
		dcc.Dropdown(
			id="drop-freq-sin",
			options=[{'label': i, 'value': i} for i in range(0, 21)],
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
					dcc.Link([html.H1("sin2(x)")], href="/page-sin2"),
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
    elif pathname == "/page-sin2":
        return layout_sin2
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
    Output('graph-sin2', 'figure'),
    [Input('drop-freq-sin', 'value')])
def update_output(value):

	return {"data": [{"x":x1, "y":np.sin(value*x1), "name":"sin({}x)".format(value), "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":0, "r":0, "t":0, "b":0}}}


@app.callback(
    [Output('slider-out-cos', 'children'), Output('graph-cos', 'figure')],
    [Input('slider-cos', 'value')])
def update_output(value):

	return 'Angular Frequency: {}'.format(value), {"data": [{"x":x1, "y":np.cos(value*x1), "name":"cos({}x)".format(value), "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":0, "r":0, "t":0, "b":0}}}
	

if __name__ == '__main__':
    app.run_server(debug=True)
