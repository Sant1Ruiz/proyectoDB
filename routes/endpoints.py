from flask import Blueprint
import handlers.endpoint_handlers as handler
import handlers.handler_users as handler_users
api = Blueprint('api', __name__)

api.add_url_rule('/', 'landing', handler.index)

# Envia el CSRF token para validar el formulario - GET
# Recibe los datos del registro de un profesional - POST
api.add_url_rule('/register/user', 'endpoint registrar usuario', handler_users.registerUser, methods=['POST', 'GET'])
api.add_url_rule('/register/professional', 'endpoint registrar profesional', handler_users.registerProfessional, methods=['POST', 'GET'])

