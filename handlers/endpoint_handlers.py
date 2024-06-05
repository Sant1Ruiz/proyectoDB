from flask import Flask, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import gets
productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.99},
    {"id": 2, "nombre": "Producto 2", "precio": 20.49}
]

@jwt_required()
def index():
    username = get_jwt_identity()
    jobs = gets.get_jobs_taked()
    return jsonify(productos, username, jobs)



