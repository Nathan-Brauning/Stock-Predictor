from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/<name>')
# def hello_world(name):
#     return(f'<p>hello world! you are {escape(name)}</p>')

@app.route('/')
def main():
    return render_template('base.html')