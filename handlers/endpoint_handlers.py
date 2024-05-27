from flask import Flask, jsonify

productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.99},
    {"id": 2, "nombre": "Producto 2", "precio": 20.49}
]

def index():
    return jsonify(productos)




# 6. Notificaciones

## 6.1. Envío de Notificaciones
def sendNotification():
    # Aquí iría la lógica para enviar la notificación
    return jsonify({"mensaje": "Notificación enviada exitosamente"}), 200

# 7. Gestión de Base de Datos

## 7.1. Inicialización de la Base de Datos
def initializeDatabase():
    return jsonify({"mensaje": "Base de datos inicializada exitosamente"}), 200

## 7.2. Backup de la Base de Datos
def backupDatabase():
    # Aquí iría la lógica para realizar un respaldo de la base de datos
    return jsonify({"mensaje": "Respaldo de base de datos creado exitosamente"}), 200

## 7.3. Restauración de la Base de Datos
def restoreDatabase():
    # Aquí iría la lógica para restaurar la base de datos desde un archivo de respaldo
    return jsonify({"mensaje": "Base de datos restaurada exitosamente"}), 200

# 8. Gestión de Seguridad

## 8.1. Encriptación de Datos
def encryptData():
    return jsonify({"mensaje": "Datos encriptados exitosamente"}), 200

## 8.2. Desencriptación de Datos
def decryptData():
    return jsonify({"mensaje": "Datos desencriptados exitosamente"}), 200

# 9. Auditoría y Log

## 9.1. Registro de Actividades
def logActivity():
    return jsonify({"mensaje": "Actividad registrada exitosamente"}), 200

## 9.2. Obtención de Logs
def getLogs(userId):
    return jsonify([])

