from flask import jsonify, request
from utils.wtf import UserForm
from utils import security, save_image
from db import gets, sets

WTF_CSRF_ENABLED = False #DESACTIVA CSRF

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
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        latitud = request.form.get('latitud')
        longitud = request.form.get('longitud')
        numero_celular = request.form.get('numero_celular')

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


        data = {
            'email': email,
            'name': name,
            'lastname': lastname,
            'latitud': latitud,
            'longitud': longitud,
            'numero_celular': numero_celular,
            'recibo_publico': recibo_publico,

            'tipo_tarjeta': cipher.decrypt(tipo_tarjeta).decode(),
            'codigo_seguridad': cipher.decrypt(codigo_seguridad).decode(),
            'fecha_expiracion': cipher.decrypt(fecha_expiracion).decode(),
            'numero_tarjeta': cipher.decrypt(numero_tarjeta).decode()
        }

        #GUARDAR LOS DATOS EN LA DB
        resp = sets.new_user(data, 'user')
        if resp:
            print("Se ha creado un nuevo registro con exito.")
            return jsonify(data), 201
        else:
            print("Fallo al crear el nuevo registro.")
            return jsonify(data), 400

        #credenciales_descifradas = cipher.decrypt(codigo_seguridad).decode() DESENCRIPTAR


#Registra un nuevo profesional
def registerProfessional():
    if request.method == 'GET':
        csrf_token = security.generateCSRF()
        jobs = gets.get_all_jobs()
        response = jsonify({'csrf_token': csrf_token, 'labores': jobs})

        response.headers['X-CSRFToken'] = csrf_token # ESTO SE SUPONE QUE GUARDA EL CSRF EN UN ENCABEZADO SIN ACCION EN EL FRONT
        return response, 200
    
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        latitud = request.form.get('latitud')
        longitud = request.form.get('longitud')

        foto_perfil = request.files['foto_perfil']
        imagen_documento = request.files['imagen_documento']

        foto_perfil = save_image.save_image(foto_perfil, "profesional_FP")
        imagen_documento = save_image.save_image(imagen_documento, "profesional_ID")

        data = { #Para cada labor debe poner su precio por hora o unidad de labor.
            'email': email,
            'name': name,
            'lastname': lastname,
            'latitud': latitud,
            'longitud': longitud,
            'foto_perfil': foto_perfil,
            'imagen_documento': imagen_documento,            
        }

        #GUARDAR LOS DATOS EN LA DB
        resp = sets.new_user(data, 'professional')
        if resp:
            print("Se ha creado un nuevo registro con exito.")
            return jsonify(data), 201
        else:
            print("Fallo al crear el nuevo registro.")
            return jsonify(data), 400



# 5. Gestión de Información de Usuarios

## 5.1. Obtención de Información
def getUserProfile(userId):
    return jsonify({"error": "Usuario no encontrado"}), 404

def getProfessionalProfile(professionalId):
    return jsonify({"error": "Profesional no encontrado"}), 404

## 5.2. Actualización de Información
def updateUserProfile(userId):
    return jsonify({"error": "Usuario no encontrado"}), 404

def updateProfessionalProfile(professionalId):
    return jsonify({"error": "Profesional no encontrado"}), 404
