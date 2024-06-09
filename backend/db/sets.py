#Archivo para almacenar registros en la base de datos
import psycopg2

def add_user(conn, data, tipo_usuario):
    try:
        cur = conn.cursor()
        values1 = (
            data['email'], 
            data['password'], 
            data['recibo_publico'], 
            data['name'], 
            data['lastname'], 
            data['latitud'], 
            data['longitud'], 
            data['foto_perfil'], 
            data['imagen_documento'], 
            data['disponibilidad']
        )
        cur.execute("""INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, disponibilidad) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING usuario_id""", 
            (values1))

        conn.commit()
        new_user_id = cur.fetchone()[0]

        if tipo_usuario == 'Cliente':
            values2 = (
                data['tipo_tarjeta'],
                data['codigo_seguridad'],
                data['fecha_expiracion'],
                data['numero_tarjeta'],
            )
            cur.execute("""INSERT INTO Tarjeta (tipo_tarjeta, codigo_seguridad, fecha_expiracion, numero_tarjeta)
                        VALUES (%s, %s, %s, %s)""",
                        (values2))
        conn.commit()

        #OBTENIENDO ROL ID
        cur.execute("SELECT rol_id, nombre_rol FROM rol")
        rols = cur.fetchall()
        id_rol = None
        for rol in rols:
            if rol[1] == tipo_usuario:
                id_rol = rol[0]
                break

        # CREANDO LA RELACION CON EL ROL
        if id_rol is not None:
            cur.execute("""INSERT INTO usuariorol (usuario_id, rol_id)
                        VALUES (%s, %s)""",
                        (new_user_id, id_rol))
            print("rol")
        else:
            print("NO SE ENCONTRO ROL")


        if tipo_usuario == 'Trabajador':
            # OBTENIENDO LABOR ID
            cur.execute("SELECT labor_id, nombre_labor FROM labor")
            labores = cur.fetchall()
            id_labor = None
            for labor in labores:
                if labor[1] == data['labor']:
                    id_labor = labor[0]
                    break
            # CREANDO LA RELACION CON LA LABOR
            if id_labor is not None:
                cur.execute("""INSERT INTO usuariolabor (usuario_id, labor_id, precio_hora)
                            VALUES (%s, %s, %s)""",
                            (new_user_id, id_labor, data['precio_hora']))
            else:
                print("NO SE ENCONTRO LABOR")        

        conn.commit()
    except  (Exception, psycopg2.Error) as e:
        print(f"Error al crear cursor: {e}")
        conn.rollback()
        return False, e
    finally:
        if cur:
            cur.close()
    return True, ''

