import os
from flaskapp import app
from flask import render_template, send_file, jsonify
from flaskapp.tree_utils import build_tree
from flaskapp.config import MEDIA_PATH

tree = build_tree()
tree.order_by_create()


@app.route('/')
def index():
    return render_template('body.html', root_nb=tree.get_root_nb())


@app.route('/refresh', methods=['POST'])
def refresh():
    """Rebuild the tree and return the homepage"""
    global tree
    tree = build_tree()
    tree.order_by_create()
    return index()


@app.route('/api/note/<nb_id>/<note_id>')
def load_note(nb_id, note_id):
    note = tree.get_note(nb_id, note_id)
    if note.content_format != 'html':
        note.change_format('html')
    return jsonify(note.__dict__)


@app.route('/api/search')
def search_data():
    note_list = tree.get_all_notes()
    search_list = [[note.title, note.notebookId + '/' + note.id]
                   for note in note_list]

    return jsonify(search_list)


@app.route('/media/<path:img_path>')
def load_media(img_path):
    filename = os.path.join(MEDIA_PATH, img_path)
    return send_file(filename)
