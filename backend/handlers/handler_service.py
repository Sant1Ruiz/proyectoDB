from flask import jsonify

#Crea una nueva solicitud de servicio
def searchService(userId, serviceDetails):
    return jsonify(userId)

# Obtiene las solicitudes pendientes para un profesional.
def getPendingRequests(professionalId):
    return jsonify(professionalId)

# Actualiza el estado de una solicitud de servicio
def updateRequestStatus(requestId, status):
    return jsonify(requestId)