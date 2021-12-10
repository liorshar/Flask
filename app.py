from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def print_hello():
    return redirect('/hello')

@app.route('/home')
def call_hello_def():
    return redirect(url_for('hello_func'))


@app.route('/hello')
def hello_func():  # put application's code here
    return 'HELLO!'

if __name__ == '__main__':
    app.run(debug=True)
