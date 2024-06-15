from flask import Flask, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from db import init as db
productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.99},
    {"id": 2, "nombre": "Producto 2", "precio": 20.49}
]

@jwt_required()
def index():
    # CUANDO SE RETORNEN LAS IMAGENES DEBEN DE SER CON LA IP DE ESTE SERVIDOR PARA QUE LAS PUEDA LINKEAR DIRECTAMENTE: http://IP/static/NOMBRE_IMAGEN
    id = get_jwt_identity()
    claims = get_jwt()
    username = claims.get('username') # Obtener el rol del usuario
    rol = claims.get('rol') # Obtener el rol del usuario

    return jsonify(productos, id, username, rol)

# Lista los trabajos tomados por algun profesional
@jwt_required()
def list_jobs_taked_details():
    jobs = db.list_jobs_taked_details()
    return jsonify(jobs)

# Lista a los profesionales en base a un trabajo
@jwt_required()
def get_professional_for_job(job):
    professionals = db.get_all_user_for_job(job)
    return jsonify(professionals)

# Listar el historial de solicitudes de una persona o trabajador
@jwt_required()
def list_history():
    # profesional y trabajador reciben su historial
    id = get_jwt_identity()
    claims = get_jwt()
    username = claims.get('username') # Obtener el rol del usuario
    rol = claims.get('rol') # Obtener el rol del usuario

    if rol != 'Administrador':
        history = db.get_history(id)
    elif rol == 'Administrador':
        history = db.get_history("Administrador")
    else:
        return jsonify({"ERROR(list_history)": "rol no reconocido"}) # administrador ve todos los historiales
    
    if isinstance(history, bool) and not history:
        print(history)
        return jsonify({"ERROR(list_history)": "Ha ocurrido un error con la base de datos"})
    return jsonify(history)

# lista a todos los usuarios o trabajadores
@jwt_required()
def list_users(rol):
    claims = get_jwt()
    rol = rol.title()
    if rol == 'Administrador' and rol != claims.get('rol'):
        return jsonify({"msg": "you don't have access"}), 401
    elif rol == 'Administrador' and rol == claims.get('rol'):
        clientes = db.get_users("Cliente")
        trabajadores = db.get_users("Trabajador")
        total = clientes + trabajadores
        return jsonify(total)
    users = db.get_users(rol)
    return jsonify(users)

@jwt_required()
def list_jobs_takeds_names():
    jobs = db.list_jobs_takeds_names()
    return jsonify(jobs)

@jwt_required()
def get_user_details(id):
    details = db.get_user_details(id)
    return jsonify(details)
