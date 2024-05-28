from flask import Flask, jsonify, request
from routes.endpoints import api
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asd51qds6g,-.o+ǵs51asd2s6a4342+'

    csrf = CSRFProtect(app)
    csrf.init_app(app)

    app.register_blueprint(api)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=7770)
