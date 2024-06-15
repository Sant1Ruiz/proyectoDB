from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, get_jwt_identity
from utils import wtf, security
from db import init as db

revoked_tokens = set()

# Verifica la sesion activa con su JWT
@jwt_required()
def verify_sesion():
    id = get_jwt_identity()
    claims = get_jwt()
    username = claims.get('username') # Obtener el rol del usuario
    rol = claims.get('rol') # Obtener el rol del usuario
    user = db.get_credentials(username)

    if user['rol'] == 'Cliente':
        return jsonify({'id': user['id'], 'name': user['username'], 'lastname': user['lastname'], 'phone': user['phone'], 'rol': user['rol'], 'longitud': user['longitud'], 'latitud': user['latitud']}), 200
    elif user['rol'] == 'Trabajador':
        stars = db.get_star_average(user['id'])
        return jsonify({'id': user['id'], 'name': user['username'], 'lastname': user['lastname'], 'phone': user['phone'], 'rol': user['rol'], 'star': stars}), 200
    elif user['rol'] == 'Administrador':
        return jsonify({'id': user['id'], 'name': user['username'], 'lastname': user['lastname'], 'email': user['email'], 'rol': user['rol']}), 200
    else:
        print("No se encontro el rol"+user['rol'])
        return jsonify({'error': 'No se encontro el rol'+user['rol']}), 400

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
        if username is None: 
            print("No se recibio el username")
            return jsonify({'error': 'username has not provided'}), 401

        elif password is None:
            print("No se recibio la contraseña")
            return jsonify({'error': 'password has not provided'}), 401
        
        else:
            user = db.get_credentials(username)
            if user and security.verify_hash(password, user['password']):
                access_token = create_access_token(identity=user['id'], additional_claims={
                    'username': user['username'],
                    'rol': user['rol']
                })
                if user['rol'] == 'Cliente':
                    return jsonify({'access_token': access_token, 'name': user['username'], 'lastname': user['lastname'], 'phone': user['phone'], 'rol': user['rol'], 'longitud': user['longitud'], 'latitud': user['latitud']}), 200
                elif user['rol'] == 'Trabajador':
                    stars = db.get_star_average(user['id'])
                    return jsonify({'access_token': access_token, 'name': user['username'], 'lastname': user['lastname'], 'phone': user['phone'], 'rol': user['rol'], 'star': stars}), 200
                elif user['rol'] == 'Administrador':
                    return jsonify({'access_token': access_token, 'name': user['username'], 'lastname': user['lastname'], 'email': user['email'], 'rol': user['rol']}), 200
                else:
                    print("No se encontro el rol"+user['rol'])
                    return jsonify({'error': 'No se encontro el rol'+user['rol']}), 400

            return jsonify({'error': 'Invalid credentials'}), 401


#Cierra la sesión de un usuario o profesional.
@jwt_required()
def logout():
    jti = get_jwt()['jti']  # JTI es el identificador único del JWT
    revoked_tokens.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200
