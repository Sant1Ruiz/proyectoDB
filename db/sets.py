#Archivo para almacenar registros en la base de datos

def new_user(data, tipo_usuario):
    if tipo_usuario == 'user':
        print("Se ha creado un nuevo usuario: "+data['email'])
    elif tipo_usuario == 'professional':
        print("Se ha creado un nuevo profesional: "+data['email'])
    else:
        print("No se ha especificado el tipo de usuario, no se ha registrado")
        return False

    return True