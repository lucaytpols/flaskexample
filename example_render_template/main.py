from flask import Flask, render_template

app = Flask(__name__)
port = 7642

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/hello/')
def home():
    return render_template("hello.html")

if __name__ == '__main__':
    app.run(port=port)
