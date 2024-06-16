from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from db import init as db
from datetime import date
from utils import calc_distance, security
@jwt_required()
def index():
    id = get_jwt_identity()
    claims = get_jwt()
    username = claims.get('username') # Obtener el rol del usuario
    rol = claims.get('rol') # Obtener el rol del usuario

    return jsonify(id, username, rol)

# Lista los trabajos tomados por algun profesional
@jwt_required()
def list_jobs_taked_details():
    jobs = db.list_jobs_taked_details()
    return jsonify(jobs)

# Lista a los profesionales en base a un trabajo ordenado por distancia | si es admin no ordena
@jwt_required()
def get_professional_for_job(job):
    claims = get_jwt()
    latitud_cliente = float(claims.get('latitud'))
    longitud_cliente = float(claims.get('longitud'))
    professionals = db.get_all_user_for_job(job)
    
    #AÑADO LA DISTANCIA
    for professional in professionals:
        distancia = calc_distance.haversine(latitud_cliente, longitud_cliente, professional['latitud'], professional['longitud'])
        professional['distancia'] = distancia

    # ORDERNO POR DISTANCIA
    professionals.sort(key=lambda x: x['distancia'])
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

@jwt_required()
def get_solicitud(id):
    solcitudes = db.get_solicitud(id)
    cipher = security.load_cipher()
    for solicitud in solcitudes:
        solicitud['tipo_tarjeta'] = cipher.decrypt(solicitud['tipo_tarjeta']).decode()
        solicitud['numero_tarjeta'] = cipher.decrypt(solicitud['numero_tarjeta']).decode()
    
    return jsonify(solcitudes)

@jwt_required()
def generate_solictud():
    # FECHA AAAA-MM-DD -> Lo genero yo datetime
    # Descripcion - request
    # Cliente -> tmbn obtner su tarjeta - request
    # Trabajador -> Cambiar disponibilidad - request
    # Labor -> Lo obtengo del trabajador
    # TarjetaID -> Lo obtengo del cliente
    claims = get_jwt()
    rol = claims.get('rol')

    if rol == 'Cliente':
        fecha = date.today()
        descripcion = request.form.get('descripcion')
        trabajador_id = request.form.get('trabajador_id')
        if descripcion is not None and trabajador_id is not None:
            cliente_id = get_jwt_identity()
            state, data = db.add_solicitud(fecha, descripcion, trabajador_id, cliente_id)
            if state:
                return jsonify(data)
            else:
                return jsonify({'error': f'{data}'})
        else:
            print("Error: descripcion o trabajador_id has not provided")
            return jsonify({'error': 'descripcion o trabajador_id has not provided'})
    else:
        print(f"Un {rol} no puede generar solicitudes, solo clientes")
        return jsonify({'error': f"Un {rol} no puede generar solicitudes, solo clientes"}), 400


@jwt_required()
def add_calificacion(solicitud_id):
    claims = get_jwt()
    rol = claims.get('rol')

    if rol == 'Cliente':
        fecha =  date.today()
        estrellas = request.form.get('estrellas')
        comentario = request.form.get('comentario')
        if estrellas is not None and comentario is not None:

            id_cliente = get_jwt_identity()

            state, data = db.add_rating(estrellas, comentario, fecha, solicitud_id, id_cliente)
            if state:
                return jsonify(data)
            else:
                return jsonify({'error': f'{data}'})
        else:
            print("Error: estrellas o comentario has not provided")
            return jsonify({'error': 'estrellas o comentario has not provided'})            

    else:
        print(f"Un {rol} no puede calificar solicitudes, solo clientes")
        return jsonify({'error': f"Un {rol} no puede calificar solicitudes, solo clientes"}), 400
