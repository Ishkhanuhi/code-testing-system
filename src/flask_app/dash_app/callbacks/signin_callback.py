import hashlib

from dash import Output, Input, State

from src.flask_app.extensions import db
from src.models import User


def handle_button_click(username, password):
    user = db.session.query(User).filter(User.username == username).first()
    if user is None:
        return '/', '', ''
    else:
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if user.passwd != password_hash:
            return '/', '', ''
        return '/dashboard', '', ''


def register_callbacks(dash_app, config):
    @dash_app.callback([
        Output('url', 'pathname'),
        Output('username', 'value'),
        Output('password', 'value'),
    ],
        Input('submit_btn', 'n_clicks'),
        [State('username', 'value'), State('password', 'value')]
    )
    def process(n_clicks, username, password):
        if n_clicks is not None:
            res = handle_button_click(username, password)
            return res
        else:
            return '/', '', ''
