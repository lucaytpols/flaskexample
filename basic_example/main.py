from flask import Flask

app = Flask(__name__)
port = 7642

@app.route('/')
def home():
    return "Hey! This works!"

if __name__ == '__main__':
    app.run(port=port)
