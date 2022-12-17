import hashlib

from dash import Output, Input, State, html
from dash.exceptions import PreventUpdate

from src.flask_app.extensions import db
from src.models import User
from src.utils import check

error_msg_style = {'background-color': '#fce4e4', 'border': '1px solid #fcc2c3', 'float': 'left', 'padding': '20px',
                   'width': '450px', 'margin': '0 auto'}


def handle_button_click(username, password, email):
    is_valid_email = check(email)
    if not is_valid_email:
        message = 'Invalid email'
        url_path = '/sign-up'
        return url_path, html.P(message, style=error_msg_style)
    existing_user = db.session.query(User).filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        message = 'A user exists with given credentials'
        url_path = '/sign-up'
        return url_path, html.P(message, style=error_msg_style)
    else:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = User()
        user.username = username
        user.password = hashed_password
        user.email = email
        db.session.add(user)
        db.session.commit()
        return '/dashboard', ''


def register_callbacks(dash_app, config):
    @dash_app.callback([
        Output('url', 'pathname'),
        Output('message', 'children')
    ],
        Input('submit_btn', 'n_clicks'),
        [State('username', 'value'), State('password', 'value'), State('email', 'value')]
    )
    def process(n_clicks, username, password, email):
        if n_clicks is not None and username and password and email:
            res = handle_button_click(username, password, email)
            return res
        else:
            return '/sign-up/', ''
