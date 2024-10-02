from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello Cloud Native! - CI/CD_Pipeline <p>&#9829;</p></h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

