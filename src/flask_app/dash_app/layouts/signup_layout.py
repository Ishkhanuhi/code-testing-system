from dash import html, dcc

label_style = {'text-align': 'left'}
input_style = {'border': '2px solid #a0a3a2', 'border-radius': '2px', 'min-height': '40px'}
input_container_style = {'width': '450px', 'padding': '10px', 'margin': '0 auto',
                         'font-size': '16px', 'border-width': '3px', 'border-color': '#a0a3a2', "display": 'flex',
                         "flex-direction": 'column'
                         }
button_container_style = {'padding-top': '30px'}
button_style = {'cursor': 'pointer', 'border': '0', 'font-size': '14px', 'border-radius': '4px', 'font-weight': '600',
                'width': '200px', 'padding': '10px 0', 'box-shadow': '0 0 20px rgba(104, 85, 224, 0.2)',
                'transition': '0.4s', 'background-color': '#6855e0', 'color': '#fff'}

error_msg_style = {'background-color': '#fce4e4', 'border': '1px solid #fcc2c3', 'float': 'left', 'padding': '20px',
                   'width': '450px', 'margin': '0 auto'}

layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.H1("Signup"),
    html.Div(id='message', style={'margin': '0 auto'}),
    html.Div([html.Label("Username", style=label_style),
              dcc.Input(type="text", placeholder="Please enter your username", id='username',
                        style=input_style, required=True)],
             style=input_container_style),
    html.Div([html.Label("Email", style=label_style),
              dcc.Input(type="email", placeholder="Please enter your email", id='email',
                        style=input_style, required=True)],
             style=input_container_style),
    html.Div([html.Label("Password", style=label_style),
              dcc.Input(type="password", placeholder="Please enter your password", id='password',
                        style=input_style, required=True)],
             style=input_container_style),
    html.Div([html.Button("Sign Up", type='submit', id='submit_btn', style=button_style)],
             style=button_container_style),
], style={'margin': '20px auto', 'text-align': 'center', 'display': 'flex', 'flex-direction': 'column'})
