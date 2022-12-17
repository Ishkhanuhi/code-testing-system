from dash import Dash

from src.flask_app.dash_app.layouts import signup_layout, signin_layout, dashboard_layout
from src.flask_app.dash_app.callbacks import register_signin_callbacks, register_signup_callbacks, \
    register_dashboard_callbacks

pages = {
    'signup': {
        'title': 'Sign Up',
        'layout': signup_layout,
        'register_callback': register_signup_callbacks,
        'route': '/sign-up/'
    },
    'signin': {
        'title': 'Sign In',
        'layout': signin_layout,
        'route': '/',
        "register_callback": register_signin_callbacks
    },
    'dashboard': {
        'title': 'Dashboard',
        'layout': dashboard_layout,
        'route': '/dashboard/',
        'register_callback': register_dashboard_callbacks
    }

}


def register_dash_app_page(server_app, page_key, config):
    page = pages[page_key]

    app = Dash(
        __name__,
        server=server_app,
        routes_pathname_prefix=page['route'],
        external_stylesheets=[
            "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
        ]
    )

    # app._favicon = 'favicon.ico'

    with server_app.app_context():
        app.title = page['title']
        app.layout = page['layout']
        page['register_callback'](app, config)


def register_dash_app(server_app, config):
    for page_key in pages:
        register_dash_app_page(server_app, page_key, config)
