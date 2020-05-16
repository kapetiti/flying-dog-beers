# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import requests
from io import BytesIO
from zipfile import ZipFile


st_dat = pd.read_csv(r"https://storage.googleapis.com/kagglesdsdata/datasets/549702/1159896/brazil_covid19.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1589853272&Signature=DKAi9dyP8LNUA7%2BOPiYrf8N23R4I5dr9sBW1iML1RQVFlyG3JfdI0S%2FRCQfgXYyYLW0Uni0ZsYkeQXLg1b5GfLIK8hehB%2B8cXJww1ZEBYCacwyPTonlcZ37GM0qOcZb3WmM5ctHt3vDEr4iIEN9p4gjuj8GqJvpsDvMt%2FrRtDP0dX%2FyKtQ8uCTARt%2BkStP7vjbV7CZBPuFeOBYdOt2Dk%2Bt%2F9qV6WgeMOnAFE1%2BkB5TKsNgNpqa%2BC8An5JR9%2BFwZS6%2B9i9Ng9h%2FLdswNY5UHgGlhtUoVegS%2F4VPWYkhcWQZU2DKGHPg9L5Raywxb4d5FDo%2FGpsK3z9iVLigoX8bsTjA%3D%3D&response-content-disposition=attachment%3B+filename%3Dbrazil_covid19.csv")

url_ct_dat = requests.get(r"https://storage.googleapis.com/kaggle-data-sets/549702/1159896/compressed/brazil_covid19_cities.csv.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1589915585&Signature=gJcMKRXeong6vzml5jqnO30MCuGdgzgAL%2BPFTLo15jShiuw11r9aTsSoGq7SbPLdqak0jRcRry3RSTlqIrJDlkLE3Fp%2Bvj5GA4LJEXJ%2FCJunWxrWJZRrJBYAS2xLP7ts6QtBPnKXTpSHj04hnj6a7H5gRYW4Q4gToegQkpPk1InZYzdFCyXQM7OVPI6q%2BSvoAHrH0HXPgtaTLA0mNdmVU4sI5irSUxoUKxHKceZaSQOMqll%2BgMag%2BXZwUAunYKnR8B%2BnMxjBdoyRYf4aU0TBQG4DKpmxpACPKrSQ4hkBcbSPbQ%2Bwe7AQnO%2BOG8iuNBYhwTze%2BeehAiA2Wkeb6diafQ%3D%3D&response-content-disposition=attachment%3B+filename%3Dbrazil_covid19_cities.csv.zip")

zipfile = ZipFile(BytesIO(url_ct_dat.content))

ct_dat = pd.read_csv(zipfile.open(zipfile.namelist()[0]))

states = st_dat.state.unique()

x1 = np.linspace(0, 10, 1000)

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True
server = app.server
app.title = "nsjdfkjsd"

layout_home = html.Div([
	html.Div(
		style={"height":100, "width":"100vw", "margin-left":-8, "margin-top":-10, "background-color":"#9015BD", "display":"flex"},
		children=[
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("SHIT IS REAL")], href="/", style={"color":"black", "text-decoration":"none"}),
				],
			),
			#~ html.Div(
				#~ style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				#~ children=[
					#~ dcc.Link([html.H1("States")], href="/page-states", style={"color":"black", "text-decoration":"none"}),
				#~ ],
			#~ ),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("Cities")], href="/page-cities", style={"color":"black", "text-decoration":"none"}),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					html.A([html.H1("GitHub")], href="https://github.com/joaopedro-vm/flying-dog-beers", target="_blank", style={"color":"black", "text-decoration":"none"}),
				],
			),
		],
	),	
])

graph_states = {"data": [{"x":st_dat[st_dat.state==states[0]].date, "y":st_dat[st_dat.state==states[0]].cases, "name":"Casos", "showlegend":True}, {"x":st_dat[st_dat.state==states[0]].date, "y":st_dat[st_dat.state==states[0]].deaths, "name":"Mortes", "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":40, "r":0, "t":20, "b":30}}}

#~ layout_states = html.Div([
	#~ html.Div(
		#~ style={"height":100, "width":"100vw", "margin-left":-8, "margin-top":-10, "background-color":"#9015BD", "display":"flex"},
		#~ children=[
			#~ html.Div(
				#~ style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				#~ children=[
					#~ dcc.Link([html.H1("SHIT IS REAL")], href="/", style={"color":"black", "text-decoration":"none"}),
				#~ ],
			#~ ),
			#~ html.Div(
				#~ style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				#~ children=[
					#~ dcc.Link([html.H1("States")], href="/page-states", style={"color":"black", "text-decoration":"none"}),
				#~ ],
			#~ ),
			#~ html.Div(
				#~ style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				#~ children=[
					#~ dcc.Link([html.H1("Cities")], href="/page-cities", style={"color":"black", "text-decoration":"none"}),
				#~ ],
			#~ ),
			#~ html.Div(
				#~ style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				#~ children=[
					#~ html.A([html.H1("GitHub")], href="https://github.com/joaopedro-vm/flying-dog-beers", target="_blank", style={"color":"black", "text-decoration":"none"}),
				#~ ],
			#~ ),
		#~ ],
	#~ ),
	#~ html.Div(style={"height":20}),
	#~ html.Div(
	#~ [
		#~ html.P(id='drop-out-states', children=['Estado: '], style={"width":60}),    
		#~ dcc.Dropdown(
			#~ id="drop-states",
			#~ options=[{'label': i, 'value': i} for i in states],
			#~ value=states[0],
			#~ style={"width":200}
		#~ ),
	#~ ],
	#~ style={"width":300, "display":"flex"}
	#~ ),
	#~ dcc.Graph(id='graph-states', figure=graph_states),
	#~ html.P(["Fonte: ", html.A(["kaggle/unanimad/corona-virus-brazil"], href="https://www.kaggle.com/unanimad/corona-virus-brazil", target="_blank")]),
#~ ])

st = ct_dat[ct_dat.state==states[0]]
stcts = st.name.unique()

graph_cities = {"data": [{"x":st[st.name==stcts[0]].date, "y":st[st.name==stcts[0]].cases, "name":"Casos", "showlegend":True}, {"x":st[st.name==stcts[0]].date, "y":st[st.name==stcts[0]].deaths, "name":"Mortes", "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":40, "r":0, "t":20, "b":30}}}

layout_cities = html.Div([
	html.Div(
		style={"height":100, "width":"100vw", "margin-left":-8, "margin-top":-10, "background-color":"#9015BD", "display":"flex"},
		children=[
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("SHIT IS REAL")], href="/", style={"color":"black", "text-decoration":"none"}),
				],
			),
			#~ html.Div(
				#~ style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				#~ children=[
					#~ dcc.Link([html.H1("States")], href="/page-states", style={"color":"black", "text-decoration":"none"}),
				#~ ],
			#~ ),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					dcc.Link([html.H1("Cities")], href="/page-cities", style={"color":"black", "text-decoration":"none"}),
				],
			),
			html.Div(
				style={"margin":{"l":0, "r":0, "t":0, "b":0}, "padding":10, "height":100, "width":300, "text-align":"center"},
				children=[
					html.A([html.H1("GitHub")], href="https://github.com/joaopedro-vm/flying-dog-beers", target="_blank", style={"color":"black", "text-decoration":"none"}),
				],
			),
		],
	),
	html.Div(style={"height":20,}),
	html.Div(
	[
		html.P(id='drop-out-states2', children=['Estado:'], style={"width":60}),    
		dcc.Dropdown(
			id="drop-states2",
			options=[{'label': i, 'value': i} for i in states],
			value=states[0],
			style={"width":200}
		),
	],
	style={"width":300, "display":"flex"}
	),
	html.Div(
	[
		html.P(id='drop-out-cities', children=['Cidade:'], style={"width":60}),    
		dcc.Dropdown(
			id="drop-cities",
			options=[{"label":"Todo o Estado", "value":0}] + [{'label': i, 'value': i} for i in stcts],
			value=0,
			style={"width":200}
		),
	],
	style={"width":300, "display":"flex"}
	),
	dcc.Graph(id='graph-cities', figure=graph_states),
	html.P(["Fonte: ", html.A(["kaggle/unanimad/corona-virus-brazil"], href="https://www.kaggle.com/unanimad/corona-virus-brazil", target="_blank")]),
])

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

app.layout = url_bar_and_content_div

app.validation_layout = html.Div([
	url_bar_and_content_div,
    layout_home,
    #~ layout_states,
	layout_cities
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/page-cities":
        return layout_cities
    #~ elif pathname == "/page-states":
        #~ return layout_states
    else:
        return layout_home

#~ @app.callback(
    #~ Output('graph-states', 'figure'),
    #~ [Input('drop-states', 'value')])
#~ def update_output(value):

	#~ return {"data": [{"x":st_dat[st_dat.state==value].date, "y":st_dat[st_dat.state==value].cases, "name":"Casos", "showlegend":True}, {"x":st_dat[st_dat.state==value].date, "y":st_dat[st_dat.state==value].deaths, "name":"Mortes", "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":40, "r":0, "t":20, "b":30}}}

@app.callback(
    [Output('drop-cities', 'options'), Output('graph-cities', 'figure')],
    [Input('drop-states2', 'value'), Input('drop-cities', 'value')])
def update_output(st, ct):
	
	st_ = ct_dat[ct_dat.state==st]
	stcts_ = st_.name.unique()
	
	if(ct == 0):
		
		return [{"label":"Todo o Estado", "value":0}]+[{'label': i, 'value': i} for i in stcts_], {"data": [{"x":st_dat[st_dat.state==st].date, "y":st_dat[st_dat.state==st].cases, "name":"Casos", "showlegend":True}, {"x":st_dat[st_dat.state==st].date, "y":st_dat[st_dat.state==st].deaths, "name":"Mortes", "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":40, "r":0, "t":20, "b":30}}}
	
	else:
		
		return [{"label":"Todo o Estado", "value":0}]+[{'label': i, 'value': i} for i in stcts_], {"data": [{"x":st_[st_.name==ct].date, "y":st_[st_.name==ct].cases, "name":"Casos", "showlegend":True}, {"x":st_[st_.name==ct].date, "y":st_[st_.name==ct].deaths, "name":"Mortes", "showlegend":True}], "layout":{"width":500, "height":300, "margin":{"l":40, "r":0, "t":20, "b":30}}}

if __name__ == '__main__':
    app.run_server(debug=True)
