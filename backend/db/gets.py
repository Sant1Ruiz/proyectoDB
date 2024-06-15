


def get_all_jobs(conn):
    #QUERY PARA OBTENER TODOS LOS TRABAJOS DISPONIBLES
    cur = conn.cursor()
    cur.execute("SELECT nombre_labor FROM LABOR")
    rows = cur.fetchall()
    data = []
    for row in rows:
        data.append(row[0])

    cur.close()
    return data

def get_credentials(conn, username):
    #QUERY PARA OBTENER EL USUARIO
    cur = conn.cursor()
    cur.execute("""SELECT u.nombre, u.password, r.nombre_rol, u.usuario_id, u.telefono, u.email, u.apellido, u.longitud, u.latitud
                FROM usuario u 
                INNER JOIN usuariorol ur ON u.usuario_id = ur.usuario_id
                INNER JOIN rol r ON r.rol_id = ur.rol_id

                """)
    rows = cur.fetchall()
    #print(rows)
    data = {}
    for row in rows:
        if row[0] == username or row[4] == username or row[5] == username:
            print(row[0])
            print(row[4])
            print(row[5])

            data = {
                'id': row[3],
                'username': row[0],
                'password': row[1],
                'rol': row[2],
                'lastname': row[6],
                'phone': row[4],
                'longitud': row[7],
                'latitud': row[8],
                'email': row[5]
            }
            return data
    return False

def list_jobs_taked_details(conn):
    #QUERY QUE OBTIENE SOLAMENTE LOS TRABAJOS QUE TIENEN AL MENOS UN PROFESIONAL Y SUS DETALLES
    cur = conn.cursor()
    cur.execute("""SELECT l.nombre_labor, l.imagen_labor, l.descripcion, COUNT(ul.usuario_id) AS cantidad_usuarios
                FROM labor l
                JOIN UsuarioLabor ul ON l.labor_id = ul.labor_id
                GROUP BY 
                    l.nombre_labor, l.imagen_labor, l.descripcion;
                """)
    rows = cur.fetchall()
    data = []
    for row in rows:
        labor_data = {
            'nombre': row[0],
            'imagen': row[1],
            'descripcion': row[2],
            'trabajadores': row[3]
        }
        data.append(labor_data)
    cur.close()
    return data

def list_jobs_takeds_names(conn):
    #QUERY QUE OBTIENE SOLAMENTE LOS TRABAJOS QUE TIENEN AL MENOS UN PROFESIONAL SOLO NOMBRE DE LA LABOR
    cur = conn.cursor()
    cur.execute("""SELECT DISTINCT l.nombre_labor
                FROM labor l
                JOIN UsuarioLabor ul ON l.labor_id = ul.labor_id
                """)
    rows = cur.fetchall()
    data = []
    for row in rows:
        data.append(row[0])
    cur.close()
    return data


def get_all_user_for_job(conn, job):
    # QUERY QUE SELECCIONE A TODOS LOS USUARIOS EN BASE AL TRABAJO
    cur = conn.cursor()
    job = job.title()
    cur.execute("""SELECT u.*
                FROM Usuario u
                JOIN UsuarioLabor ul ON u.usuario_id = ul.usuario_id
                JOIN Labor l ON ul.labor_id = l.labor_id
                WHERE l.nombre_labor = %s;
                """, (job,))
    #cur.execute("""
    #    SELECT u.*, c.*, ul.precio_hora, l.*
    #    FROM usuario u 
    #    JOIN solicitud s ON u.usuario_id = s.usuario_id 
    #    JOIN calificacion c ON c.solicitud_id = s.solicitud_id
    #    JOIN usuariolabor ul ON ul.usuario_id  = u.usuario_id
    #    JOIN labor l ON l.labor_id = ul.labor_id 
    #    WHERE l.nombre_labor = %s
    #    ORDER BY c.estrellas DESC, ul.precio_hora DESC 
    #    
    #    """, (job,))    
    rows = cur.fetchall()
    data = []
    # for row in rows:
    #     dict_row = {}
    #     for idx, col in enumerate(cur.description):
    #         dict_row[col[0]] = row[idx]
    #     data.append(dict_row)
    for row in rows:
        dict_row = {}
        for idx, col in enumerate(cur.description):
            dict_row[col[0]] = row[idx]
        # Obtener el promedio de estrellas y agregarlo al diccionario
        usuario_id = dict_row['usuario_id']
        dict_row['estrellas'] = get_star_average(conn, usuario_id)
        data.append(dict_row)

    cur.close()
    
    return data

def get_history(conn, user):
    # Dependiendo del usuario
    # Listar el historial de solicitudes de una persona
    # Listar el historial de solicitudes de un trabajador
    cur = conn.cursor()
    if user != 'Administrador':
        cur.execute("""SELECT s.*
                FROM solicitud s
                WHERE s.usuario_id = %s;
                """, (user,))
        
    elif user == 'Administrador':
        cur.execute("""SELECT s.*
                FROM Solicitud s
                """)
    else:
        return False
    
    rows = cur.fetchall()
    data = []
    for row in rows:
        dict_row = {}
        for idx, col in enumerate(cur.description):
            dict_row[col[0]] = row[idx]
        data.append(dict_row)
    cur.close()
    return data

def get_users(conn, rol):
    #QUERY QUE RETORNA TODOS LOS USUARIOS rol = trabajadores o clientes
    cur = conn.cursor()

    if rol == 'Trabajador':
        cur.execute("""SELECT u.*, l.nombre_labor, r.nombre_rol
                FROM usuario u
                JOIN usuariolabor ul ON u.usuario_id = ul.usuario_id
                JOIN labor l ON ul.labor_id = l.labor_id
                JOIN usuariorol ur ON u.usuario_id = ur.usuario_id
                JOIN rol r ON ur.rol_id = r.rol_id
                WHERE r.nombre_rol = 'Trabajador';
                """)
    elif rol == 'Cliente':
        cur.execute("""SELECT u.*, r.nombre_rol
                FROM usuario u
                JOIN usuariorol ur ON u.usuario_id = ur.usuario_id
                JOIN rol r ON ur.rol_id = r.rol_id
                WHERE r.nombre_rol = 'Cliente';
                """)

    else:
        return False
    
    rows = cur.fetchall()
    data = []
    for row in rows:
        dict_row = {}
        for idx, col in enumerate(cur.description):
            dict_row[col[0]] = row[idx]
        data.append(dict_row)
    cur.close()
    return data


def get_star_average(conn, id):
    cur = conn.cursor()

    #QUERY PARA OBTENER EL PROMEDIO DE ESTRELLAS

    return 4

def get_user_details(conn, id):
    cur = conn.cursor()

    cur.execute("""SELECT 
                FROM usuario
                WHERE usuario_id = %s
                """, (id,))
    rows = cur.fetchall()

    data = {}

    for row in rows:
        for idx, col in enumerate(cur.description):
            col_name = col[0]
            if col_name not in data:
                data[col_name] = row[idx]
        # Obtener el promedio de estrellas y agregarlo al diccionario
        star_avg = get_star_average(conn, id)
        data['estrellas'] = star_avg

    return data