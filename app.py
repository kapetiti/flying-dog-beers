# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
   html.Label('Text Input'),
   dcc.Input(value='MTL', type='text'),
	
   html.Label('Slider'),
   dcc.Slider(
      min=0,
      max=9,
      marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
      value=5,
   ),
]
)

if __name__ == '__main__':
   app.run_server(debug=True)
