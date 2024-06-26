import pandas as pd
import datetime as dt
import os
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.offline as pyo
import plotly.graph_objs as go


def render_tab(df):

    layout = html.Div([html.H1('Kanały sprzedaży', style={'text-align': 'center'}),

                       html.Div([html.Div([dcc.Graph(id='pie_country')], style={'width': '50%'}),
                                 html.Div([dcc.Dropdown(id='weekday_dropdown',
                                                        options=[{'label': shop, 'value': shop} for shop in
                                                                 df['Store_type'].unique()],
                                                        value=df['Store_type'].unique()[0]),
                                           dcc.Graph(id='bar_store')], style={'width': '50%'})],
                                style={'display': 'flex'}),

                       html.Div(id='temp-out')
                       ])

    return layout
