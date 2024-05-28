from flask import jsonify, request
from flask_wtf.csrf import generate_csrf, validate_csrf
from utils.wtf import UserForm
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import uuid
import jwt
from cryptography.fernet import Fernet
from PIL import Image
from db import gets
WTF_CSRF_ENABLED = False #DESACTIVA CSRF
UPLOAD_FOLDER = 'uploads'

def load_cipher():
    try:
        with open('.key', 'rb') as archivo_clave:
            key = archivo_clave.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open('.key', 'wb') as archivo_clave:
            archivo_clave.write(key)
        print("LA LLAVE DE CIFRADO HA CAMBIADO")
    return key

cipher = Fernet(load_cipher())

def save_image(img, prefix):
    filename = f'{prefix}_{format(datetime.now().strftime("%Y%m%d_%H%M%S"))}_{str(uuid.uuid4())}.jpg'
    path = os.path.join(UPLOAD_FOLDER, filename)
    imagen_pil = Image.open(img)
    if imagen_pil.mode != 'RGB':
        imagen_pil = imagen_pil.convert('RGB')
    imagen_pil.save(path, 'JPEG')
    return filename

# Genera el token CSRF
def generateCSRF():
    csrf_token = generate_csrf()
    return csrf_token

#Manejador de registro de un nuevo usuario
def registerUser():
    if request.method == 'GET':
        csrf_token = generateCSRF()
        response = jsonify({'csrf_token': csrf_token})
        response.headers['X-CSRFToken'] = csrf_token # ESTO SE SUPONE QUE GUARDA EL CSRF EN UN ENCABEZADO SIN ACCION EN EL FRONT
        return response, 200

    if request.method == 'POST':
            #data =
        #csrf_token = request.headers.get('X-CSRFToken')
        #if not validate_csrf(csrf_token):
        #    return jsonify({'error': 'Token CSRF inválido'}), 400
        #form = UserForm(request.form)
        #if form.validate():


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
        recibo_publico = save_image(recibo_publico, "user_RP")


        """
        filename = 'user_RP_{}_{}'.format(datetime.now().strftime("%Y%m%d_%H%M%S"), str(uuid.uuid4()))
        recibo_publico.save(os.path.join(UPLOAD_FOLDER, filename))
        recibo_publico = filename

        filename = 'user_FP_{}_{}'.format(datetime.now().strftime("%Y%m%d_%H%M%S"), str(uuid.uuid4()))
        foto_perfil.save(os.path.join(UPLOAD_FOLDER, filename))
        foto_perfil = filename

        filename = 'user_ID_{}_{}'.format(datetime.now().strftime("%Y%m%d_%H%M%S"), str(uuid.uuid4()))
        imagen_documento.save(os.path.join(UPLOAD_FOLDER, filename))
        imagen_documento = filename
        """

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

        #credenciales_descifradas = cipher.decrypt(codigo_seguridad).decode() DESENCRIPTAR
        print(data)
        return jsonify(data), 200




#Registra un nuevo profesional
def registerProfessional():
    if request.method == 'GET':
        csrf_token = generateCSRF()
        jobs = gets.get_jobs()
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

        foto_perfil = save_image(foto_perfil, "profesional_FP")
        imagen_documento = save_image(imagen_documento, "profesional_ID")

        data = {
            'email': email,
            'name': name,
            'lastname': lastname,
            'latitud': latitud,
            'longitud': longitud,
            'foto_perfil': foto_perfil,
            'imagen_documento': imagen_documento,            
        }

        return jsonify(data)

#Autentica a un usuario o profesional.
def login(credentials):
    return jsonify(credentials)

#Cierra la sesión de un usuario o profesional.
def logout(token):
    return jsonify(token)


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
