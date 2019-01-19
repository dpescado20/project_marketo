import os
import base64
from urllib.parse import quote as urlquote

from flask import Flask, send_from_directory

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

UPLOAD_DIRECTORY = '/project_marketo_app/app_uploaded_files'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# create a route for downloading files directly
server = Flask(__name__)
app = dash.Dash(server=server)


@server.route('download/<path:path>')
def download(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachement=True)
