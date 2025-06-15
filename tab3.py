from dash import html, dcc
import pandas as pd
import plotly.graph_objects as go
def render_tab(df):

    layout = html.Div([html.H1('Kanały sprzedaży',style={'text-align':'center'}),
                        html.Div([html.Div([dcc.Graph(id='weekdays-sales')],style={'width':'50%'})],style={'display':'flex'})
                        ])

    return layout