from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Gitlab CI/CD!'

if __name__ == '__main__':
    app.run('0.0.0.0', host="8080")