def get_all_jobs():
    #QUERY PARA OBTENER TODOS LOS TRABAJOS DISPONIBLES
    return ['plomero', 'fontanero', 'profesor de inglés', 'paseador de perros']

def get_credentials(username):
    #QUERY PARA OBTENER EL USUARIO
    data = {
        'username': 'juan',
        'password': 'scrypt:32768:8:1$k6tvDc8SljKFlZVi$0e8352611023e37c703f94cf3646281b9981e605a50aedf5b1cbcdbab143624a767aa84062b8edc9d6a633cc3d6e6fa9efdab324d5135bcc96ca9b8ca910db03',
    }
    if data['username']==username:
        return data
    return False

def get_jobs_taked():
    #QUERY QUE OBTIENE SOLAMENTE LOS TRABAJOS QUE TIENEN AL MENOS UN PROFESIONAL
    return ['plomero', 'paseador de perros']
