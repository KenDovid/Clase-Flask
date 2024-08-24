from flask import Flask
from controller import etapa

app = Flask(__name__)

app.register_blueprint(etapa)

if __name__ == '__main__':
    app.run(debug=True)
