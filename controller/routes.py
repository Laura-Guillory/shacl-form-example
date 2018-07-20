from flask import Blueprint, render_template, request, Response, redirect, url_for
from jinja2.exceptions import TemplateNotFound
import os
import config as config
from shaclform import Form2RDFController, generate_form

routes = Blueprint('controller', __name__)


@routes.route('/')
def form():
    try:
        return render_template('form_contents.html')
    except TemplateNotFound:
        return render_template('generate_form_prompt.html')


@routes.route('/generate_form')
def gen_form():
    form_filepath = config.TEMPLATES_DIR + '/form_contents.html'
    map_filepath = 'map.ttl'
    try:
        with open(config.SHAPES_FILE_PATH) as shape:
            generate_form(shape, form_destination=form_filepath, map_destination=map_filepath)
    except FileNotFoundError:
        return Response('No SHACL shapes file provided at ' + config.SHAPES_FILE_PATH,
                        status=500,
                        mimetype='text/plain')
    return redirect(url_for('controller.form'))


@routes.route('/post', methods=['POST'])
def post():
    form2rdf_controller = Form2RDFController('http://example.org/ex#')
    try:
        rdf_result = form2rdf_controller.convert(request, 'map.ttl')
    except ValueError as e:
        return Response(str(e))
    except FileNotFoundError:
        return Response('Map.ttl is missing!', status=500, mimetype='text/plain')
    rdf_result.serialize(destination='result.ttl', format='turtle')
    return render_template('post.html')

