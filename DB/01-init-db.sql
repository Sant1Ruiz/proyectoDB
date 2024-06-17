CREATE TABLE Usuario (
    usuario_id SERIAL PRIMARY KEY,
    email VARCHAR(350) NOT NULL UNIQUE,
    password VARCHAR(350) NOT NULL,
    recibo_publico VARCHAR(255),
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    latitud DECIMAL(9,6),
    longitud DECIMAL(9,6),
    foto_perfil VARCHAR(255),
    imagen_documento VARCHAR(255),
    telefono VARCHAR(14) UNIQUE,
    disponibilidad BOOLEAN DEFAULT TRUE
);

CREATE TABLE Rol (
    rol_id SERIAL PRIMARY KEY,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE
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
    tipo_tarjeta VARCHAR(255) NOT NULL,
    codigo_seguridad VARCHAR(255) NOT NULL,
    fecha_expiracion VARCHAR(255) NOT NULL,
    numero_tarjeta VARCHAR(255) NOT NULL,
    titular_id INT NOT NULL UNIQUE,
    FOREIGN KEY (titular_id) REFERENCES Usuario(usuario_id)
);


CREATE TABLE Labor (
    labor_id SERIAL PRIMARY KEY,
    descripcion TEXT NOT NULL,
    nombre_labor VARCHAR(100) NOT NULL,
    imagen_labor VARCHAR(255) NOT NULL 
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
    fecha DATE NOT NULL DEFAULT NOW(),
    descripcion TEXT NOT NULL,
    usuario_id INT NOT NULL,
    usuario_labor_id INT NOT NULL,
    labor_id INT NOT NULL,
    tarjeta_id INT NOT NULl,
    completado BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (tarjeta_id) REFERENCES Tarjeta(tarjeta_id),    
    FOREIGN KEY (usuario_id) REFERENCES Usuario(usuario_id),
    FOREIGN KEY (usuario_labor_id, labor_id) REFERENCES UsuarioLabor(usuario_id, labor_id)
);

CREATE TABLE Calificacion (
    calificacion_id SERIAL PRIMARY KEY,
    estrellas INT NOT NULL,
    comentario TEXT,
    fecha_calificacion DATE NOT NULL DEFAULT NOW(),
    solicitud_id INT NOT NULL UNIQUE,
    FOREIGN KEY (solicitud_id) REFERENCES Solicitud(solicitud_id)
);
