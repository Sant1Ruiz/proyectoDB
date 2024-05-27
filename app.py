from flask import Flask, jsonify, request
from routes.endpoints import api
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asd51qds6g,-.o+ǵs51asd2s6a4342+'

    csrf = CSRFProtect(app)
    csrf.init_app(app)

    app.register_blueprint(api)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=7770)





"""
# Datos de ejemplo para simular una base de datos
productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 10.99},
    {"id": 2, "nombre": "Producto 2", "precio": 20.49}
]

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

# Ruta para obtener un producto por su ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

# Ruta para crear un nuevo producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    nuevo_producto = request.json
    productos.append(nuevo_producto)
    return jsonify({"mensaje": "Producto creado correctamente"}), 201

"""