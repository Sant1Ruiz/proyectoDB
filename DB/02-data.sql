INSERT INTO Rol (nombre_rol) VALUES
('Cliente'),
('Trabajador'),
('Administrador');

-- Clientes
INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, telefono) VALUES
('cliente1@mail.com', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', '123456789', 'Ana', 'García', 4.710989, -74.072092, '+573001234567'),
('cliente2@mail.com', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', '987654321', 'Carlos', 'Martínez', 4.656971, -74.058196, '+573009876543'),
('cliente3@mail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', '246813579', 'Laura', 'Rodríguez', 4.676260, -74.048219, '+573005678901');

INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES
(1, 1), (2, 1), (3, 1);

-- Trabajadores
INSERT INTO Usuario (email, password, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad) VALUES
('trabajador1@mail.com', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 'Pedro', 'Sánchez', 4.651265, -74.055855, '/static/default/perfil1.jpg', 'doc1.jpg', '+573002345678', true),
('trabajador2@mail.com', 'fe2592b42a727e977f055947385b709cc82b16b9a87f88c6abf3900d65d0cdc3', 'María', 'López', 4.666568, -74.056714, '/static/default/perfil2.jpg', 'doc2.jpg', '+573007890123', true),
('trabajador3@mail.com', '37f1ee3881605db26be0f7203c326f235cca6668acb788912871907005005b8c', 'Juan', 'Gómez', 4.628308, -74.064699, '/static/default/perfil3.jpg', 'doc3.jpg', '+573004567890', false);

INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES
(4, 2), (5, 2), (6, 2);

-- Administradores
INSERT INTO Usuario (email, password, nombre, apellido) VALUES
('admin1@mail.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'Sofía', 'Herrera'),
('admin2@mail.com', 'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f', 'Daniel', 'Torres'),
('admin3@mail.com', '7b8b965ad4bca0e41ab51de7b31363a1487f6b5166717eab1fa2e79776f0f70a', 'Isabella', 'Vargas'),
('admin4@mail.com', 'd7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592', 'Miguel', 'Castro');

INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES
(7, 3), (8, 3), (9, 3), (10, 3);

INSERT INTO Tarjeta (tipo_tarjeta, codigo_seguridad, fecha_expiracion, numero_tarjeta, titular_id) VALUES
('Visa', '123', '2025-12-31', '4111111111111111', 1),
('MasterCard', '456', '2024-10-31', '5555555555554444', 2),
('American Express', '789', '2026-06-30', '371449635398431', 3),
('Visa', '234', '2025-09-30', '4012888888881881', 1),
('MasterCard', '567', '2024-11-30', '5105105105105100', 2),
('Visa', '890', '2026-03-31', '4222222222222', 3),
('American Express', '345', '2025-07-31', '378282246310005', 4),
('MasterCard', '678', '2024-08-31', '5555555555554444', 5),
('Visa', '901', '2026-01-31', '4111111111111111', 6),
('American Express', '234', '2025-05-31', '371449635398431', 1);


INSERT INTO Labor (descripcion, nombre_labor, imagen_labor) VALUES
('Limpieza general del hogar', 'Limpieza', '/static/default/limpieza.jpg'),
('Cuidado de niños', 'Niñera', '/static/default/ninera.jpg'),
('Reparaciones eléctricas', 'Electricista', '/static/default/electricista.jpg'),
('Reparación de tuberías y desagües', 'Plomero', '/static/default/plomero.jpg'),
('Corte de césped y mantenimiento de jardines', 'Jardinero', '/static/default/jardinero.jpg'),
('Pintura de interiores y exteriores', 'Pintor', '/static/default/pintor.jpg'),
('Reparación y mantenimiento de aires acondicionados', 'Técnico A/C', '/static/default/tecnico_ac.jpg'),
('Clases particulares de matemáticas', 'Tutor', '/static/default/tutor.jpg'),
('Paseo y cuidado de mascotas', 'Paseador de perros', '/static/default/paseador.jpg'),
('Servicio de transporte personal', 'Chofer', '/static/default/chofer.jpg');

INSERT INTO UsuarioLabor (usuario_id, labor_id, precio_hora) VALUES
(4, 1, 25000.00),
(5, 3, 35000.00),
(6, 5, 30000.00);


INSERT INTO Solicitud (fecha, descripcion, usuario_id, usuario_labor_id, labor_id, tarjeta_id) VALUES
('2024-03-01', 'Limpieza general de la casa', 1, 4, 1, 1),
('2024-03-05', 'Reparación de corto circuito', 2, 5, 3, 2),
('2024-03-10', 'Mantenimiento de jardín', 3, 6, 5, 3),
('2024-03-15', 'Limpieza profunda post-evento', 1, 4, 1, 4),
('2024-03-20', 'Instalación de nuevo cableado', 2, 5, 3, 5),
('2024-03-25', 'Poda de árboles y arbustos', 3, 6, 5, 6),
('2024-04-01', 'Limpieza de alfombras', 1, 4, 1, 7),
('2024-04-05', 'Reparación de tomacorrientes', 2, 5, 3, 8),
('2024-04-10', 'Siembra de nuevas plantas', 3, 6, 5, 9),
('2024-04-15', 'Limpieza de ventanas', 1, 4, 1, 10);

INSERT INTO Calificacion (estrellas, comentario, fecha_calificacion, solicitud_id) VALUES
(5, 'Excelente servicio, muy profesional', '2024-03-02', 1),
(4, 'Buen trabajo, resolvió el problema rápidamente', '2024-03-06', 2),
(5, 'El jardín quedó hermoso, muy satisfecho', '2024-03-11', 3),
(5, 'Limpieza impecable, altamente recomendado', '2024-03-16', 4),
(4, 'Instalación correcta, solo un poco de retraso', '2024-03-21', 5),
(5, 'Trabajo de poda perfecto, muy cuidadoso', '2024-03-26', 6),
(5, 'Las alfombras quedaron como nuevas', '2024-04-02', 7),
(4, 'Solucionó el problema, pero tardó más de lo esperado', '2024-04-06', 8),
(5, 'Las nuevas plantas le dan vida al jardín, gracias', '2024-04-11', 9),
(5, 'Windows spotless, great attention to detail', '2024-04-16', 10);
