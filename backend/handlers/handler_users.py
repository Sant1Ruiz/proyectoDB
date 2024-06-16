from flask import jsonify, request
from utils.wtf import UserForm
from utils import security, save_image
from db import init as db


cipher = security.load_cipher()

#Manejador de registro de un nuevo usuario
def registerUser():
    if request.method == 'GET':
        csrf_token = security.generateCSRF()
        response = jsonify({'csrf_token': csrf_token})
        response.headers['X-CSRFToken'] = csrf_token # ESTO SE SUPONE QUE GUARDA EL CSRF EN UN ENCABEZADO SIN ACCION EN EL FRONT
        return response, 200

    if request.method == 'POST':
        # OBTENER LOS DATOS EDL FORMULARIO
        email = request.form.get('email')
        password =  request.form.get('password')
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        latitud = request.form.get('latitud')
        longitud = request.form.get('longitud')
        telefono = request.form.get('telefono')

        recibo_publico = request.files['recibo_publico']

        tipo_tarjeta = request.form.get('tipo_tarjeta')
        codigo_seguridad = request.form.get('codigo_seguridad')
        fecha_expiracion = request.form.get('fecha_expiracion')
        numero_tarjeta = request.form.get('numero_tarjeta')

        # GUARDAR LAS IMAGENES SUBIDAS
        recibo_publico = save_image.save_image(recibo_publico, "user_RP")

        #ENCRIPTANDO DATOS DE LA TARJETA
        tipo_tarjeta = cipher.encrypt(tipo_tarjeta.encode())
        codigo_seguridad = cipher.encrypt(codigo_seguridad.encode())
        fecha_expiracion = cipher.encrypt(fecha_expiracion.encode())
        numero_tarjeta = cipher.encrypt(numero_tarjeta.encode())

        # HASHEAR PASSWORD
        password = security.hash(password)

        data = {
            'email': email,
            'password': password,
            'recibo_publico': recibo_publico,
            'name': name,
            'lastname': lastname,
            'latitud': latitud,
            'longitud': longitud,
            'telefono': telefono,
            'foto_perfil': '',
            'imagen_documento': '',
            'disponibilidad': True,

            # 'tipo_tarjeta': cipher.decrypt(tipo_tarjeta).decode(),
            # 'codigo_seguridad': cipher.decrypt(codigo_seguridad).decode(),
            # 'fecha_expiracion': cipher.decrypt(fecha_expiracion).decode(),
            # 'numero_tarjeta': cipher.decrypt(numero_tarjeta).decode()

            'tipo_tarjeta': tipo_tarjeta,
            'codigo_seguridad': codigo_seguridad,
            'fecha_expiracion': fecha_expiracion,
            'numero_tarjeta': numero_tarjeta
        }

        #GUARDAR LOS DATOS EN LA DB
        resp, error = db.add_user(data, 'Cliente')
        if resp:
            print("Se ha creado un nuevo registro con exito.")
            return jsonify({'msg': 'created'}), 201
        else:
            print("Fallo al crear el nuevo registro.")
            return jsonify({'ERROR': str(error)}), 400

        #credenciales_descifradas = cipher.decrypt(codigo_seguridad).decode() DESENCRIPTAR


#Registra un nuevo profesional
def registerProfessional():
    if request.method == 'GET':
        csrf_token = security.generateCSRF()
        jobs = db.get_all_jobs()
        response = jsonify({'csrf_token': csrf_token, 'labores': jobs})

        response.headers['X-CSRFToken'] = csrf_token # ESTO SE SUPONE QUE GUARDA EL CSRF EN UN ENCABEZADO SIN ACCION EN EL FRONT
        return response, 200
    
    if request.method == 'POST':
        email = request.form.get('email')
        password =  request.form.get('password')
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        latitud = request.form.get('latitud')
        longitud = request.form.get('longitud')
        labor = request.form.get('labor')
        precio_hora = request.form.get('precio_hora')
        telefono = request.form.get('telefono')

        foto_perfil = request.files['foto_perfil']
        imagen_documento = request.files['imagen_documento']

        foto_perfil = save_image.save_image(foto_perfil, "profesional_FP")
        imagen_documento = save_image.save_image(imagen_documento, "profesional_ID")

        # HASHEAR PASSWORD
        password = security.hash(password)

        data = { #Para cada labor debe poner su precio por hora o unidad de labor.
            'email': email,
            'password': password,
            'recibo_publico': '',
            'name': name,
            'lastname': lastname,
            'latitud': latitud,
            'longitud': longitud,
            'foto_perfil': foto_perfil,
            'imagen_documento': imagen_documento,
            'disponibilidad': True,
            'labor': labor,
            'precio_hora': precio_hora,
            'telefono': telefono
        }

        #GUARDAR LOS DATOS EN LA DB
        resp, error = db.add_user(data, 'Trabajador')
        if resp:
            print("Se ha creado un nuevo registro con exito.")
            return jsonify({'msg': 'created'}), 201
        else:
            print("Fallo al crear el nuevo registro.")
            return jsonify({'ERROR': str(error)}), 400

def registerAdmin():
    if request.method == 'GET':
        csrf_token = security.generateCSRF()
        response = jsonify({'csrf_token': csrf_token})

        response.headers['X-CSRFToken'] = csrf_token # ESTO SE SUPONE QUE GUARDA EL CSRF EN UN ENCABEZADO SIN ACCION EN EL FRONT
        return response, 200
    
    if request.method == 'POST':
        email = request.form.get('email')
        password =  request.form.get('password')
        name = request.form.get('name')
        lastname = request.form.get('lastname')

        # HASHEAR PASSWORD
        password = security.hash(password)

        data = { #Para cada labor debe poner su precio por hora o unidad de labor.
            'email': email,
            'password': password,
            'recibo_publico': '',
            'name': name,
            'lastname': lastname,
            'latitud': 0,
            'longitud': 0,
            'foto_perfil': '',
            'imagen_documento': '',
            'disponibilidad': True,
            'labor': '',
            'precio_hora': '',
            'telefono': ''
        }

        #GUARDAR LOS DATOS EN LA DB
        resp, error = db.add_user(data, 'Administrador')
        if resp:
            print("Se ha creado un nuevo registro con exito.")
            return jsonify({'msg': 'created'}), 201
        else:
            print("Fallo al crear el nuevo registro.")
            return jsonify({'ERROR': str(error)}), 400