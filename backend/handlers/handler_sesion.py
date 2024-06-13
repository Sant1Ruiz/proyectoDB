from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from utils import wtf, security
from db import init as db

revoked_tokens = set()

#Autentica a un usuario o profesional.
def login():
    if request.method == 'GET':
        csrf_token = security.generateCSRF()
        response = jsonify({'csrf_token': csrf_token})
        response.headers['X-CSRFToken'] = csrf_token # ESTO SE SUPONE QUE GUARDA EL CSRF EN UN ENCABEZADO SIN ACCION EN EL FRONT
        return response, 200

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = db.get_credentials(username)
        if user and security.verify_hash(password, user['password']):
            access_token = create_access_token(identity=user['id'], additional_claims={
                'username': username,
                'rol': user['rol']
            })
            return jsonify({'access_token': access_token, 'role': user['rol']}), 200
        return jsonify({'error': 'Invalid credentials'}), 401


#Cierra la sesión de un usuario o profesional.
@jwt_required()
def logout():
    jti = get_jwt()['jti']  # JTI es el identificador único del JWT
    revoked_tokens.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200
