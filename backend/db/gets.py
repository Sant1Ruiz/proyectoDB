import psycopg2


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

def get_credentials(conn, username, case):
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
    if case == 'login':
        for row in rows:
            if row[4] == username or row[5] == username:
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
                return True, data
    else:
        for row in rows:
            if row[3] == username:
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
                return True, data
    return False, 'No se encontro ningun usuario que coincida'

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
    job = job.lower()
    cur.execute("""SELECT u.*
                FROM Usuario u
                JOIN UsuarioLabor ul ON u.usuario_id = ul.usuario_id
                JOIN Labor l ON ul.labor_id = l.labor_id
                WHERE LOWER(l.nombre_labor) = %s;
                """, (job,))
    rows = cur.fetchall()
    data = []
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

# para obtener el promedio de estrellas de un usuario en base a su usuario_labor_id
def get_star_average(conn, id):
    cur = conn.cursor()

    query = """
        SELECT AVG(c.estrellas) 
        FROM Calificacion c
        JOIN Solicitud s ON c.solicitud_id = s.solicitud_id
        WHERE s.usuario_labor_id = %s;
    """
    cur.execute(query, (id,))
    result = cur.fetchone()
    
    cur.close()
    
    return result[0] if result[0] is not None else 0

# Obtiene el usuario por su id con sus detalles completos
def get_user_details(conn, id):
    cur = conn.cursor()

    cur.execute("""SELECT *
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

# Obtiene el rol del id del usuario
def get_rol(conn, id):
    cur = conn.cursor()
    try:    
        cur.execute("""SELECT r.nombre_rol
                    FROM usuario u 
                    INNER JOIN usuariorol ur ON u.usuario_id = ur.usuario_id
                    INNER JOIN rol r ON r.rol_id = ur.rol_id
                    WHERE u.usuario_id = %s
                    """, (id,))
        rol = cur.fetchone()[0]
        return rol
    except  (Exception, psycopg2.Error) as e:
        print(f"Error al crear cursor: {e}")
        return False
    finally:
        if cur:
            cur.close()
    

# Obtiene las solicitudes hechas o recibidas de un cliente o de un trabajador
def get_solicitud(conn, id):
    cur = conn.cursor()
    rol = get_rol(conn, id)

# SELECT s.*
# FROM calificacion c
# JOIN Solicitud s ON c.solicitud_id = s.solicitud_id
# WHERE s.usuario_id = %s

    if not rol:
        return {'error': 'No se encontro el usuario'}
    elif rol == 'Cliente':
        cur.execute("""SELECT s.*
                    FROM solicitud s
                    WHERE s.usuario_id = %s
                    """, (id,))
    elif rol == 'Trabajador':
        cur.execute("""SELECT s.*
                    FROM solicitud s
                    WHERE s.usuario_labor_id = %s
                    """, (id,))
    elif rol == 'Administrador':
        print("El id es de un administrador")
        cur.close()
        return {'error': 'El id es de un administrador'}
    else:
        print("No se reconoce el rol del usuario")
        cur.close()
        return {'error': 'No se reconoce el rol del usuario'}

    rows = cur.fetchall()
    data = []
    for row in rows:
        dict_row = {}
        for idx, col in enumerate(cur.description):
            dict_row[col[0]] = row[idx]
        data.append(dict_row)
    cur.close()
    return data
