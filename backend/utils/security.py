# CIFRAR
from cryptography.fernet import Fernet

def load_cipher():
    try:
        with open('.key', 'rb') as archivo_clave:
            key = archivo_clave.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open('.key', 'wb') as archivo_clave:
            archivo_clave.write(key)
        print("LA LLAVE DE CIFRADO HA CAMBIADO")
    return Fernet(key)

# HASHEAR
from werkzeug.security import generate_password_hash, check_password_hash

def hash(password):
    hashed_password = generate_password_hash(password)
    return hashed_password

def verify_hash(password, hashed_password):
    if check_password_hash(hashed_password, password):
        return True
    else:
        return False
    
# CSRF
from flask_wtf.csrf import generate_csrf, validate_csrf

def generateCSRF():
    csrf_token = generate_csrf()
    return csrf_token