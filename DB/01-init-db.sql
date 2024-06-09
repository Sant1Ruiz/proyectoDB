-- Active: 1717902967589@@172.17.0.1@5432@paelsam@public
CREATE TABLE Usuario (
    usuario_id SERIAL PRIMARY KEY,
    email VARCHAR(350) NOT NULL,
    password VARCHAR(350) NOT NULL,
    recibo_publico VARCHAR(255),
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    latitud DECIMAL(9,6),
    longitud DECIMAL(9,6),
    foto_perfil VARCHAR(255),
    imagen_documento VARCHAR(255),
    telefono VARCHAR(13),
    disponibilidad BOOLEAN
);

CREATE TABLE Rol (
    rol_id SERIAL PRIMARY KEY,
    nombre_rol VARCHAR(50) NOT NULL
);

CREATE TABLE UsuarioRol (
    usuario_id INT NOT NULL,
    rol_id INT NOT NULL,
    PRIMARY KEY (usuario_id, rol_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (rol_id) REFERENCES Rol(rol_id)
);

CREATE TABLE Tarjeta (
    tarjeta_id SERIAL PRIMARY KEY,
    tipo_tarjeta VARCHAR(50) NOT NULL,
    codigo_seguridad VARCHAR(10) NOT NULL,
    fecha_expiracion DATE NOT NULL,
    numero_tarjeta VARCHAR(20) NOT NULL
);

CREATE TABLE MetodoPago (
    metodopago_id SERIAL PRIMARY KEY,
    tipo_pago VARCHAR(50) NOT NULL,
    nombre_titular VARCHAR(100) NOT NULL,
    tarjeta_id INT,
    FOREIGN KEY (tarjeta_id) REFERENCES Tarjeta(tarjeta_id)
);

CREATE TABLE Labor (
    labor_id SERIAL PRIMARY KEY,
    descripcion TEXT NOT NULL,
    nombre_labor VARCHAR(100) NOT NULL
);

CREATE TABLE UsuarioLabor (
    usuario_id INT NOT NULL UNIQUE,
    labor_id INT NOT NULL,
    precio_hora DECIMAL(11,2) NOT NULL,
    PRIMARY KEY (usuario_id, labor_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (labor_id) REFERENCES Labor(labor_id)
);

CREATE TABLE Solicitud (
    solicitud_id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    descripcion TEXT NOT NULL,
    estado VARCHAR(50) NOT NULL,
    precio_total DECIMAL(11,2) NOT NULL,
    usuario_id INT NOT NULL,
    usuario_labor_id INT NOT NULL,
    labor_id INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (usuario_labor_id, labor_id) REFERENCES UsuarioLabor(usuario_id, labor_id)
);

CREATE TABLE Calificacion (
    calificacion_id SERIAL PRIMARY KEY,
    estrellas INT NOT NULL,
    comentario TEXT,
    fecha_calificacion DATE NOT NULL,
    solicitud_id INT NOT NULL,
    FOREIGN KEY (solicitud_id) REFERENCES Solicitud(solicitud_id)
);
