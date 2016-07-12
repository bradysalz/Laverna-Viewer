import os
from flaskapp import app
from flask import render_template, send_file
from flaskapp.tree_utils import build_tree
from config import MEDIA_PATH

tree = build_tree()


@app.route('/')
def hello_world():
    return render_template('body.html', root_nb=tree.get_root_nb())


@app.route('/note/<nb_id>/<note_id>')
def load_note(nb_id, note_id):
    note = tree.get_note(nb_id, note_id)
    if note.content_format != 'html':
        note.change_format('html')
    return note.content
    # return render_template('body.html',
    #                          root_nb=tree.get_root_nb(),
    #                          note=note)


@app.route('/example')
def example():
    return render_template('example.html')


@app.route('/media/<path:img_path>')
def load_media(img_path):
    filename = os.path.join(MEDIA_PATH, img_path) 
    return send_file(filename)
