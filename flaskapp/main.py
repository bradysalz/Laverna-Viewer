from flask import Flask, render_template
from tree_utils import build_tree

app = Flask(__name__)

tree = build_tree()
tree.print_tree()


@app.route('/')
def hello_world():
    return render_template('body.html')


@app.route('/example')
def example():
    tree.print_tree()
    return render_template('example.html')

app.run(debug=True)
