from flaskapp import app
from flask import render_template
from flaskapp.tree_utils import build_tree

tree = build_tree()
tree.print_tree()


@app.route('/')
def hello_world():
    # print tree.get_root_nb.get_children()
    return render_template('body.html', root_nb=tree.get_root_nb())


@app.route('/example')
def example():
    tree.print_tree()
    return render_template('example.html')
