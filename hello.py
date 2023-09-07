from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return {'message': 'Hello, World!'}

def handler(request: Request):
    return app(request)

if __name__ == '__main__':
    app.run(debug=True)
