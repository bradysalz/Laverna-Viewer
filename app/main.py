from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('body.html')


@app.route('/example')
def example():
    return render_template('example.html')
