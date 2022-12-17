from dash import html, dcc

layout = html.Div([
    html.H5('Please select function type to perform check:', style={'margin': '10px'}),
    dcc.RadioItems([
        {'label': html.Span(['Factorial'], style={'margin-left': '5px'}), 'value': 'factorial'},
        {'label': html.Span(['Palindrome'], style={'margin-left': '5px'}), 'value': 'palindrome'},
    ],
        value='factorial',
        id='chosen-value',
        style={'margin': '10px 10px 20px', 'display': 'flex', 'justify-content': 'space-around'},

    ),
    html.Em('and upload .py file, which contains corresponding function'),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]
        ),
        style={
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'cursor': 'pointer',
        },
    ),
    html.Div(id='output-data-upload'),
    html.H1(id="message"),
    dcc.Location(id='url')
], style={'max-width': '480px', 'text-align': 'center', 'margin': '20px auto'}, )
