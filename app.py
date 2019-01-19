import os
import re
import base64
from urllib.parse import quote as urlquote

from flask import Flask, send_from_directory

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc

UPLOAD_DIRECTORY = '/project_marketo_app/app_uploaded_files'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# app header
_navbar = dbc.Navbar(
    children=[
    ],
    brand='Data Prox Master',
    brand_href='#',
    sticky='top'
)

# tab contents
tab1_content = (
    dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Upload(
                                    dbc.Button('Upload DY-SOI Data'),
                                    id='id-upload1')
                            ], width=3
                        ),
                    ]
                ),

                # line space
                dbc.Row(
                    [
                        html.Br()
                    ]
                ),

                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(id='id-lbl1')
                            ]
                        )
                    ]
                ),

                # line space
                dbc.Row(
                    [
                        html.Br()
                    ]
                ),

                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Upload(
                                    dbc.Button('Upload DY-SOI New Hierarchy'),
                                    id='id-upload2')
                            ], width=3
                        ),
                    ]
                ),

                # line space
                dbc.Row(
                    [
                        html.Br()
                    ]
                ),

                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(id='id-lbl2')
                            ]
                        )
                    ]
                ),

                # line space
                dbc.Row(
                    [
                        html.Br()
                    ]
                ),

                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Button('Start Process', id='id-btn1', n_clicks=0)
                            ]
                        )
                    ]
                ),
                # line space
                dbc.Row(
                    [
                        html.Br()
                    ]
                ),

                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(id='id-lbl3')
                            ]
                        )
                    ]
                )
            ]
        )
    )
)

# app body
_body = dbc.Container(
    [
        # line space
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br()
                    ]
                )
            ]
        ),

        # tab creation
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Tabs(
                            [
                                dbc.Tab(tab1_content, label='New DY-SOI'),
                                # dbc.Tab(tab2_content, label='Duplicate Tracker')
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

# create a route for downloading files directly
server = Flask(__name__)
app = dash.Dash(server=server)


@server.route('download/<path:path>')
def download(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachement=True)


# app layout
app.layout = html.Div([_navbar, _body])

# app main
if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
