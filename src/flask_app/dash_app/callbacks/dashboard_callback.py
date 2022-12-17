import base64
import os
import tempfile
import subprocess

from dash import Output, Input, State, html


def parse_contents(contents, filename, config, chosen_value):
    input_txt = ''
    output_txt = ''
    expected_txt = ''
    output = ''
    try:
        if 'py' in filename:
            content_type, content_string = contents.split(',')
            decoded = base64.b64decode(content_string)
            temp_file = tempfile.NamedTemporaryFile(suffix='.py', delete=True)
            try:
                temp_file.write(decoded)
                temp_file.seek(0)
                with open(os.path.join(config['input_file_path'], f'{chosen_value}_input.txt')) as f1:
                    process = subprocess.run(["python", f"{temp_file.name}"], stdin=f1, capture_output=True)
                with open(os.path.join(config['output_file_path'], f'{chosen_value}_expected_output.txt')) as f:
                    expected_value = f.readline()
                with open(os.path.join(config['input_file_path'], f'{chosen_value}_input.txt')) as f1:
                    input_txt = f"Input: {f1.readline()}"
                if process.returncode == 0:
                    output = str(process.stdout.decode('utf-8')).replace("\n", "")
                    output_txt = f"Output: {output}"
                else:
                    output_txt = f"Output: None"
                expected_txt = f"Expected Output: {expected_value}"
            finally:
                temp_file.close()
        else:
            input_txt = 'Only .py files are supported'
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.', '', ''
        ])

    expected_style = {}
    if expected_value == output:
        expected_style = {'color': 'green'}
    return html.Div([
        html.H5(input_txt),
        html.H5(output_txt, style=expected_style),
        html.H5(expected_txt, style=expected_style),
    ])


def register_callbacks(dash_app, config):
    @dash_app.callback([Output('output-data-upload', 'children')],
                       [Input('upload-data', 'contents'),
                        State('upload-data', 'filename'),
                        Input('chosen-value', 'value')
                        ])
    def update_output(content, name, chosen_value):
        if content is not None and chosen_value is not None:
            children = [parse_contents(content, name, config, chosen_value)]
            return children
        else:
            return ['']
