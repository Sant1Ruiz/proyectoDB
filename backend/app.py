from flask import Flask
from routes.endpoints import api
from flask_wtf.csrf import CSRFProtect
from flask_jwt_extended import JWTManager
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asd51qds6g,-.o+ǵs51asd2s6a4342+'

    csrf = CSRFProtect(app)
    csrf.init_app(app)


    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Cambia esta clave a una más segura
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=3)  # Tiempo de expiración del token

    jwt = JWTManager(app)


    app.register_blueprint(api)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
