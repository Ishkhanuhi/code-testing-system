import os.path

from flask import Blueprint, send_from_directory


blueprint = Blueprint('route_root', __name__, template_folder='../../templates')


@blueprint.route('/tmp_file/<path:file_path>')
def tmp_file(file_path):
    return send_from_directory('/tmp/', file_path.split('/', 1)[1])


@blueprint.route('/footage_input_data/<path:filename>')
def footage_input_data(filename):
    return send_from_directory(os.getenv('FOOTAGE_INPUT_DIR'), filename)


@blueprint.route('/footage_output_data/<path:filename>')
def footage_output_data(filename):
    return send_from_directory(os.getenv('FOOTAGE_OUTPUT_DIR'), filename)
