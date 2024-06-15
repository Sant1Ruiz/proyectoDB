-- Active: 1717902967589@@172.17.0.1@5432@paelsam@public
INSERT INTO Rol (nombre_rol) VALUES
('Cliente'),
('Trabajador'),
('Administrador');

INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad) VALUES
('usuario1@email.com', 'e38ad214943daad1d64c102faec29de4afe9da3d', 'RP001', 'Juan', 'Pérez', -33.448890, -70.669265, 'perfil1.jpg', 'doc1.jpg', '1234567890', true),
('usuario2@email.com', '2aa60a8ff7fcd473d321e0146afd9e26df395147', 'RP002', 'María', 'González', 4.651265, -74.055855, 'perfil2.jpg', 'doc2.jpg', '0987654321', false),
('usuario3@email.com', '1119cfd37ee247357e034a08d844eea25f6fd20f', 'RP003', 'Pedro', 'Sánchez', -33.460000, -70.650000, 'perfil3.jpg', 'doc3.jpg', '1122334455', true),
('usuario4@email.com', 'a1881c06eec96db9901c7bbfe41c42a3f08e9cb4', 'RP004', 'Ana', 'Martínez', 4.666568, -74.056714, 'perfil4.jpg', 'doc4.jpg', '5566778899', false),
('usuario5@email.com', 'fb209e3feaa9680e507bcb2557b76a9190426a5a', 'RP005', 'Luis', 'Rodríguez', -33.480000, -70.630000, 'perfil5.jpg', 'doc5.jpg', '9988776655', true),
('usuario6@email.com', '4b4b04529d87a5ca7568730533b7a0d6e0a2482d', 'RP006', 'Carmen', 'López', -33.490000, -70.620000, 'perfil6.jpg', 'doc6.jpg', '3322114455', false),
('usuario7@email.com', 'db8e1af0cb3aca1ae2d0018624204529970560fe', 'RP007', 'Javier', 'Fernández', 4.628308, -74.064699, 'perfil7.jpg', 'doc7.jpg', '6677889900', true),
('usuario8@email.com', 'a5dea47281fb1c97b9306e468c1e9f7d5d0f95bb', 'RP008', 'Sofía', 'Díaz', -33.510000, -70.600000, 'perfil8.jpg', 'doc8.jpg', '1199887766', false),
('usuario9@email.com', 'cb4e5208b4cd87268b208e49452ed6e89a68e0b8', 'RP009', 'Diego', 'Morales', -33.520000, -70.590000, 'perfil9.jpg', 'doc9.jpg', '5544332211', true),
('usuario10@email.com', 'da39a3ee5e6b4b0d3255bfef95601890afd80709', 'RP010', 'Valentina', 'Herrera', -33.530000, -70.580000, 'perfil10.jpg', 'doc10.jpg', '9911223344', false);

INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES
(1, 1), (2, 2), (3, 1), (4, 2), (5, 3),
(6, 1), (7, 2), (8, 1), (9, 2), (10, 1);

INSERT INTO Tarjeta (tipo_tarjeta, codigo_seguridad, fecha_expiracion, numero_tarjeta) VALUES
('Visa', '123', '2025-12-31', '4111111111111111'),
('MasterCard', '456', '2024-10-31', '5555555555554444'),
('American Express', '789', '2026-06-30', '378282246310005'),
('Visa', '234', '2023-09-30', '4012888888881881'),
('MasterCard', '567', '2025-03-31', '5105105105105100'),
('Visa', '890', '2024-07-31', '4222222222222'),
('American Express', '345', '2026-01-31', '371449635398431'),
('MasterCard', '678', '2023-11-30', '5200828282828210'),
('Visa', '901', '2025-08-31', '4111111111111111'),
('American Express', '432', '2024-04-30', '378734493671000');

INSERT INTO MetodoPago (tipo_pago, nombre_titular, tarjeta_id) VALUES
('Tarjeta', 'Juan Pérez', 1),
('Efectivo', 'María González', NULL),
('Tarjeta', 'Pedro Sánchez', 3),
('Tarjeta', 'Ana Martínez', 4),
('Efectivo', 'Luis Rodríguez', NULL),
('Tarjeta', 'Carmen López', 6),
('Efectivo', 'Javier Fernández', NULL),
('Tarjeta', 'Sofía Díaz', 8),
('Tarjeta', 'Diego Morales', 9),
('Efectivo', 'Valentina Herrera', NULL);

INSERT INTO Labor (descripcion, nombre_labor) VALUES
('Limpieza general del hogar', 'Limpieza'),
('Cuidado de niños', 'Niñera'),
('Corte de césped y jardinería', 'Jardinería'),
('Reparaciones eléctricas', 'Electricista'),
('Pintura de interiores y exteriores', 'Pintor'),
('Plomería y reparaciones de tuberías', 'Plomero'),
('Clases particulares de matemáticas', 'Tutor'),
('Paseo y cuidado de mascotas', 'Paseador de perros'),
('Reparación y mantenimiento de computadoras', 'Técnico informático'),
('Cocina y preparación de comidas', 'Chef a domicilio');

INSERT INTO UsuarioLabor (usuario_id, labor_id, precio_hora) VALUES
(2, 1, 15.50),  -- María González es trabajadora de limpieza
(4, 2, 18.00),  -- Ana Martínez es niñera
(7, 4, 25.00),  -- Javier Fernández es electricista
(9, 6, 30.00),  -- Diego Morales es plomero
(5, 3, 20.00),  -- Luis Rodríguez es jardinero (aunque es admin, podría ser un super usuario)
(6, 8, 12.50),  -- Carmen López es paseadora de perros (aunque es cliente, podría ser un error o caso especial)
(8, 7, 25.00),  -- Sofía Díaz es tutora (aunque es cliente, podría ser un error o caso especial)
(10, 10, 40.00),  -- Valentina Herrera es chef a domicilio (aunque es cliente, podría ser un error o caso especial)
(1, 5, 22.00),  -- Juan Pérez es pintor (aunque es cliente, podría ser un error o caso especial)
(3, 9, 35.00);  -- Pedro Sánchez es técnico informático (aunque es cliente, podría ser un error o caso especial)

INSERT INTO Solicitud (fecha, descripcion, estado, precio_total, usuario_id, usuario_labor_id, labor_id) VALUES
('2024-06-10', 'Limpieza de toda la casa', 'Completada', 62.00, 1, 2, 1),
('2024-06-11', 'Cuidado de mi hijo por 4 horas', 'Pendiente', 72.00, 3, 4, 2),
('2024-06-12', 'Corte de césped y poda de arbustos', 'En progreso', 80.00, 6, 5, 3),
('2024-06-13', 'Reparación de enchufe y luces', 'Completada', 50.00, 8, 7, 4),
('2024-06-14', 'Pintar sala y comedor', 'Pendiente', 176.00, 2, 1, 5),
('2024-06-15', 'Reparación de fuga en el baño', 'En progreso', 90.00, 3, 9, 6),
('2024-06-16', 'Clases de matemáticas, 2 horas', 'Completada', 50.00, 6, 8, 7),
('2024-06-17', 'Paseo de mi perro por 1 hora', 'Pendiente', 12.50, 8, 6, 8),
('2024-06-18', 'Formateo y limpieza de PC', 'En progreso', 70.00, 1, 3, 9),
('2024-06-19', 'Cena para evento familiar', 'Completada', 160.00, 3, 10, 10);

INSERT INTO Calificacion (estrellas, comentario, fecha_calificacion, solicitud_id) VALUES
(5, 'Excelente trabajo, muy limpio', '2024-06-10', 1),
(4, 'Muy buena atención con mi hijo', '2024-06-11', 2),
(5, 'Jardín quedó espectacular', '2024-06-12', 3),
(4, 'Rápido y eficiente', '2024-06-13', 4),
(3, 'Pintura bien, pero tardó más de lo esperado', '2024-06-14', 5),
(5, 'Solucionó la fuga rápidamente', '2024-06-15', 6),
(5, 'Mi hijo mejoró mucho en matemáticas', '2024-06-16', 7),
(4, 'Puntual y cariñoso con mi perro', '2024-06-17', 8),
(4, 'PC funciona mucho mejor ahora', '2024-06-18', 9),
(5, 'La cena estuvo deliciosa, todos quedaron encantados', '2024-06-19', 10);