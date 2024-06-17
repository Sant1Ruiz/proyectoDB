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
            data['disponibilidad'],
            data['telefono']
        )
        cur.execute("""INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, disponibilidad, telefono) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING usuario_id""", 
            (values1))

        conn.commit()
        new_user_id = cur.fetchone()[0]

        if tipo_usuario == 'Cliente':
            values2 = (
                psycopg2.Binary(data['tipo_tarjeta']),
                psycopg2.Binary(data['codigo_seguridad']),
                psycopg2.Binary(data['fecha_expiracion']),
                psycopg2.Binary(data['numero_tarjeta']),
                new_user_id
            )
            cur.execute("""INSERT INTO Tarjeta (tipo_tarjeta, codigo_seguridad, fecha_expiracion, numero_tarjeta, titular_id)
                        VALUES (%s, %s, %s, %s, %s)""",
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




def add_solicitud(conn, fecha, descripcion, trabajador_id, cliente_id):
    try:
        cur = conn.cursor()

        # Labor -> Lo obtengo del trabajador
        cur.execute("SELECT labor_id FROM usuariolabor WHERE usuario_id = %s", (trabajador_id,))
        labor_id = cur.fetchone()[0]

        # TarjetaID -> Lo obtengo del cliente
        cur.execute("SELECT tarjeta_id FROM tarjeta WHERE titular_id = %s", (cliente_id,))
        tarjeta_id = cur.fetchone()[0]

        cur.execute("""INSERT INTO solicitud (fecha, descripcion, usuario_id, usuario_labor_id, labor_id, tarjeta_id)
                    VALUES (%s, %s, %s, %s, %s, %s) RETURNING solicitud_id""", 
                    (fecha, descripcion, cliente_id, trabajador_id, labor_id, tarjeta_id))
        conn.commit()
        new_solicitud_id = cur.fetchone()[0]

        # Trabajador -> Cambiar disponibilidad
        cur.execute("UPDATE usuario SET disponibilidad = FALSE WHERE usuario_id = %s", (trabajador_id,))        
        conn.commit()

        # Obtenemos los datos añadidos
        cur.execute("SELECT * FROM solicitud WHERE solicitud_id = %s", (new_solicitud_id,))
        rows = cur.fetchall()
        data = []
        for row in rows:
            dict_row = {}
            for idx, col in enumerate(cur.description):
                dict_row[col[0]] = row[idx]
            data.append(dict_row)
        return True, data
    except  (Exception, psycopg2.Error) as e:
        print(f"Error al crear cursor: {e}")
        conn.rollback()
        return False, e
    finally:
        if cur:
            cur.close()


def add_rating(conn, estrellas, comentario, fecha, solicitud_id, id_cliente):
    try:
        cur = conn.cursor()
        
        cur.execute("SELECT usuario_id FROM solicitud WHERE solicitud_id = %s", (solicitud_id,))
        cliente_solicitid = cur.fetchone()[0]
        if id_cliente == cliente_solicitid:
            cur.execute("""INSERT INTO calificacion (estrellas, comentario, fecha_calificacion, solicitud_id)
                        VALUES (%s, %s, %s, %s) RETURNING calificacion_id""",
                        (estrellas, comentario, fecha, solicitud_id))
            conn.commit()
            new_calificacion_id = cur.fetchone()[0]

            cur.execute("SELECT * FROM calificacion WHERE calificacion_id = %s", (new_calificacion_id,))
            rows = cur.fetchall()
            data = []
            for row in rows:
                dict_row = {}
                for idx, col in enumerate(cur.description):
                    dict_row[col[0]] = row[idx]
                data.append(dict_row)
            return True, data
        else:
            print("El usuario no puede calificar esta solicitud pues no es el cliente de ella")
            return False, 'Este usuario no puede calificar esta solicitud. Esta solicitud no te pertenece'

    except  (Exception, psycopg2.Error) as e:
        print(f"Error al crear cursor: {e}")
        conn.rollback()
        return False, e
    finally:
        if cur:
            cur.close()
    



def set_solicitud_done(conn, solicitud_id, trabajador_id):
    try: # VALIDAR QUE EL USUARIO QUE CALIFICA SEA EL MISMO QUE RECIBIO EL SERVICIO!!!!
        cur = conn.cursor()
        
        cur.execute("SELECT usuario_labor_id FROM solicitud WHERE solicitud_id = %s", (solicitud_id,))
        trabajador_solicitid = cur.fetchone()[0]
        if trabajador_id == trabajador_solicitid:
            cur.execute("UPDATE usuario SET disponibilidad = TRUE WHERE usuario_id = %s", (trabajador_id,))        
            conn.commit()
            return True, ''
        else:
            print("El usuario no puede calificar esta solicitud pues no es el cliente de ella")
            return False, 'Este usuario no puede terminar esta solicitud. Esta solicitud no te pertenece'

    except  (Exception, psycopg2.Error) as e:
        print(f"Error al crear cursor: {e}")
        conn.rollback()
        return False, e
    finally:
        if cur:
            cur.close()
    