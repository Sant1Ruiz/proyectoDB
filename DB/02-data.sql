-- Tabla Rol
INSERT INTO Rol (nombre_rol) VALUES ('Cliente');
INSERT INTO Rol (nombre_rol) VALUES ('Trabajador');
INSERT INTO Rol (nombre_rol) VALUES ('Administrador');

-- Tabla Usuario
INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad)
VALUES ('cliente1@example.com', 'password1', '123456789', 'Juan', 'Pérez', 3.451776, -76.532650, NULL, NULL, '3001234567', true);
INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad)
VALUES ('cliente2@example.com', 'password2', '987654321', 'María', 'Gómez', 3.374162, -76.522503, NULL, NULL, '3005678901', true);
INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad)
VALUES ('trabajador1@example.com', 'password3', NULL, 'Pedro', 'Rodríguez', 3.427175, -76.509567, '/static/default/perfil1.jpg', 'documento1.pdf', '3002345678', true);
INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad)
VALUES ('trabajador2@example.com', 'password4', NULL, 'Ana', 'Martínez', 3.398567, -76.541234, '/static/default/perfil2.jpg', 'documento2.pdf', '3009876543', false);
INSERT INTO Usuario (email, password, nombre, apellido)
VALUES ('admin1@example.com', 'scrypt:32768:8:1$iIQoF2zUI5fDTQUu$aa084fcf8b69a21c8af35e68e529917072a96458969379e38522bc6b5f5f8777af985deab642c23a8e5169a63f0c00a18c21f77b790dc9153ea2063d261c7875', 'Carlos', 'Ramírez');
INSERT INTO Usuario (email, password, nombre, apellido)
VALUES ('admin2@example.com', 'password6', 'Laura', 'Torres');
INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad)
VALUES ('cliente3@example.com', 'password7', '741852963', 'Luis', 'Hernández', 3.366492, -76.539781, NULL, NULL, '3107654321', true);
INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad)
VALUES ('cliente4@example.com', 'password8', '159753684', 'Sofía', 'Moreno', 3.415927, -76.491032, NULL, NULL, '3101234567', true);
INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad)
VALUES ('trabajador3@example.com', 'password9', NULL, 'Carlos', 'Gutiérrez', 3.389154, -76.524673, '/static/default/perfil3.jpg', 'documento3.pdf', '3209876543', true);
INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad)
VALUES ('trabajador4@example.com', 'password10', NULL, 'Valentina', 'Díaz', 3.442381, -76.498265, '/static/default/perfil4.jpg', 'documento4.pdf', '3105647382', false);

INSERT INTO Usuario (email, password, recibo_publico, nombre, apellido, latitud, longitud, foto_perfil, imagen_documento, telefono, disponibilidad)
VALUES 
('cliente5@example.com', 'password11', '123123123', 'Andrea', 'Lopez', 3.451176, -76.532850, NULL, NULL, '3001111111', true),
('cliente6@example.com', 'password12', '321321321', 'Miguel', 'Cruz', 3.374262, -76.522603, NULL, NULL, '3002222222', true),
('trabajador5@example.com', 'password13', NULL, 'Diego', 'Ramirez', 3.427275, -76.509667, '/static/default/perfil5.jpg', 'documento5.pdf', '3003333333', true),
('trabajador6@example.com', 'password14', NULL, 'Sara', 'Hernandez', 3.398667, -76.541334, '/static/default/perfil6.jpg', 'documento6.pdf', '3004444444', false),
('admin3@example.com', 'password15', NULL, 'Luis', 'Garcia', NULL, NULL, NULL, NULL, NULL, NULL),
('admin4@example.com', 'password16', NULL, 'Elena', 'Ruiz', NULL, NULL, NULL, NULL, NULL, NULL),
('cliente7@example.com', 'password17', '741741741', 'David', 'Martinez', 3.366592, -76.539881, NULL, NULL, '3101111111', true),
('cliente8@example.com', 'password18', '951951951', 'Laura', 'Diaz', 3.415827, -76.491132, NULL, NULL, '3102222222', true),
('trabajador7@example.com', 'password19', NULL, 'Jorge', 'Gutierrez', 3.389254, -76.524773, '/static/default/perfil7.jpg', 'documento7.pdf', '3201111111', true),
('trabajador8@example.com', 'password20', NULL, 'Carolina', 'Diaz', 3.442481, -76.498365, '/static/default/perfil8.jpg', 'documento8.pdf', '3103333333', false),
('cliente9@example.com', 'password21', '852852852', 'Carlos', 'Ortiz', 3.401776, -76.533850, NULL, NULL, '3005555555', true),
('cliente10@example.com', 'password22', '753753753', 'Camila', 'Jimenez', 3.422162, -76.523503, NULL, NULL, '3006666666', true),
('trabajador9@example.com', 'password23', NULL, 'Mario', 'Vega', 3.435175, -76.511567, '/static/default/perfil9.jpg', 'documento9.pdf', '3007777777', true),
('trabajador10@example.com', 'password24', NULL, 'Lucia', 'Santos', 3.396567, -76.543234, '/static/default/perfil10.jpg', 'documento10.pdf', '3008888888', false),
('admin5@example.com', 'password25', NULL, 'Jose', 'Luna', NULL, NULL, NULL, NULL, NULL, NULL),
('admin6@example.com', 'password26', NULL, 'Ana', 'Marin', NULL, NULL, NULL, NULL, NULL, NULL),
('cliente11@example.com', 'password27', '963963963', 'Andres', 'Castro', 3.376492, -76.540781, NULL, NULL, '3103334444', true),
('cliente12@example.com', 'password28', '159159159', 'Isabella', 'Ramos', 3.426927, -76.492032, NULL, NULL, '3104445556', true),
('trabajador11@example.com', 'password29', NULL, 'Javier', 'Mendez', 3.387154, -76.525673, '/static/default/perfil11.jpg', 'documento11.pdf', '3203334444', true),
('trabajador12@example.com', 'password30', NULL, 'Valeria', 'Cruz', 3.445381, -76.499265, '/static/default/perfil12.jpg', 'documento12.pdf', '3104445555', false);


-- Tabla UsuarioRol
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (1, 1); -- Cliente
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (2, 1); -- Cliente
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (3, 2); -- Trabajador
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (4, 2); -- Trabajador
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (5, 3); -- Administrador
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (6, 3); -- Administrador
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (7, 1); -- Cliente
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (8, 1); -- Cliente
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (9, 2); -- Trabajador
INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES (10, 2); -- Trabajador

INSERT INTO UsuarioRol (usuario_id, rol_id) VALUES 
(11, 1), (12, 1), (13, 2), (14, 2), (15, 3), (16, 3), (17, 1), (18, 1), (19, 2), (20, 2),
(21, 1), (22, 1), (23, 2), (24, 2), (25, 3), (26, 3), (27, 1), (28, 1), (29, 2), (30, 2);


-- Tabla Labor
INSERT INTO Labor (descripcion, nombre_labor, imagen_labor)
VALUES ('Servicio de limpieza de hogares', 'Limpieza de Hogar', '/static/default/limpieza.jpg');
INSERT INTO Labor (descripcion, nombre_labor, imagen_labor)
VALUES ('Servicio de jardinería', 'Jardinería', '/static/default/jardinero.jpg');
INSERT INTO Labor (descripcion, nombre_labor, imagen_labor)
VALUES ('Servicio de pintura de interiores y exteriores', 'Pintura', '/static/default/pintor.jpg');
INSERT INTO Labor (descripcion, nombre_labor, imagen_labor)
VALUES ('Servicio de mudanza y transporte de muebles', 'Mudanza', '/static/default/mudanza.jpg');
INSERT INTO Labor (descripcion, nombre_labor, imagen_labor)
VALUES ('Servicio de plomería', 'Plomería', '/static/default/plomero.jpg');
INSERT INTO Labor (descripcion, nombre_labor, imagen_labor)
VALUES ('Servicio de electricidad', 'Electricidad', '/static/default/electricista.jpg');
INSERT INTO Labor (descripcion, nombre_labor, imagen_labor)
VALUES ('Servicio de carpintería', 'Carpintería', '/static/default/carpinteria.jpg');
INSERT INTO Labor (descripcion, nombre_labor, imagen_labor)
VALUES ('Servicio de mecánica automotriz', 'Mecánica Automotriz', '/static/default/mecanica.jpg');
INSERT INTO Labor (descripcion, nombre_labor, imagen_labor)
VALUES ('Servicio de programación y desarrollo de software', 'Programación', '/static/default/programacion.jpg'),
('Clases particulares de matemáticas', 'Tutor', '/static/default/tutor.jpg'),
('Servicio de transporte personal', 'Chofer', '/static/default/chofer.jpg'),
('Paseo y cuidado de mascotas', 'Paseador de perros', '/static/default/paseador.jpg'),
('Reparación y mantenimiento de aires acondicionados', 'Técnico de aires acondicionados', '/static/default/tecnico_ac.jpg'),
('Cuidado de niños', 'Niñera', '/static/default/ninera.jpg');


INSERT INTO UsuarioLabor (usuario_id, labor_id, precio_hora) VALUES 
(3, 1, 22000), (4, 2, 23000), (9, 3, 26000), (10, 4, 19000),
(13, 5, 21000), (14, 6, 15000), (19, 7, 20000), (20, 8, 33000),
(23, 9, 23000), (24, 10, 24000), (29, 11, 20500), (30, 12, 12000);


INSERT INTO Tarjeta (tipo_tarjeta, codigo_seguridad, fecha_expiracion, numero_tarjeta, titular_id) VALUES 
('gAAAAABmbnCminJJif-5Ph2v7dbZWN0k0mijmOz_IvlOjt24105CEERLJjfXzXUMhXWnVMMKAChlKG3fslw2MAI1dcl57Y3ROA==', 'gAAAAABmbnCm9mOmikEnFCMg623z-AOkLnyP2TBuRqIdqGVa2yS_gp-FYGUxEuujEgNaa4vvcvGaHCvgkYFatw-urjpXoIBN7Q==', 'gAAAAABmbnCmeGT7DxY2AMESBjSqEpA7Oc-HVOzCeCpUrvLG0cHZnm8-zVCBjdvCKLd4ylIvAJhgpuuGANG-ED-7zwDUIwGsQw==', 'gAAAAABmbnCmhMw47harPfRSjNN-oN0HZ1bvVP4mALgIIrPOW-lJLISPl4QOl24fNyIU7P2QPQuwKPQvqd7j6HsxGLl75cZ40eQ041N9K9SOF6qR0YRGKLQ=', 2),
('gAAAAABmbnCmLYXvTmnYjzasf7MroUgXnxJ5X5KrGgqZDGwk6imT4bnE7qe5ezI_krkX3VNTU06TTPGa-Xb9WfnWYpF-F_HDlQ==', 'gAAAAABmbnCmpK8vMf8mpTFVf2fGq0O_Px__EdRF565v0Lv62u_nLmFYi9-vmhkAY_QmCjNlDmlLeIJn5_rf3vrwYIypxE6IjA==', 'gAAAAABmbnCme5hBcsnCuS9Hd8PJ7IRYX-nhHCXBioVapCWB8UjGlzyQJvGJgwZxezSYmI7d1xc2LsH52L82a1wafYiXZ6o92A==', 'gAAAAABmbnCmrgI9uEoNjDP-YeUMdRxCR-YJb20c728k1oamSEo32vJRn_QIyiMFjOiLPhi0t8nUEKG8gU_gHwy1t0GCRKzJb6atXxmG0c1lySdmyValBB4=', 7),
('gAAAAABmbnCmm5B3iLALTd00KL28NqM0_zViGhXLQQT3BHWFt2rtZBDyD7SWgDvDnrSYOuP9m4nBp1yNUkv4PEEFZCeA25HV3w==', 'gAAAAABmbnCmZE6HcpNj1lmpNgADAO_945VoCHQmpW8l-oxJB36_iLKw-vv6edVCUVHp3PMCRZ_YxD0N_5WfQQrHxaty0fkafg==', 'gAAAAABmbnCmJ1KJmCWuPLZGNMPHSYMLI3gNWChG5O9oNbUKjqaBmLrhxoBfCDlGZN2j7O_DZCx254s7B83BvnaLvnd29Pb-Zg==', 'gAAAAABmbnCmKmsT8p9wCrSspNpbCgNEQdb4i5BCGgvss1Uqdk9MHYKZ5zingLty2PX2PLRn47KdFpxhvn5d8yOJQcUg706RyoVoHFffaIxleNwDu9zAW2E=', 8),
('gAAAAABmbnCmPPCfljTNbDHzDipBRl9uR9sfQlGVZznr-BXsxzRX_q3WbaUF9zTk8fQUZ12073t3XVzxdjqIwJ6QC6YpuJJU3w==', 'gAAAAABmbnCmdSxH0Y7Sbd57hKAzsFBacPS0guQf-z2PE0ptnvjNo1u9o0uKi72OgzYuO0Gzfv7ThPnOzWmvqnx9Ye3zvudvpg==', 'gAAAAABmbnCmbqYL7XpLLxG7YN1hx9-CFNHYMnfID25Eybb7h_WOi9QsrAayeo31QfrODrO_ViDpu1rWgYQgEG72PT1cICypLw==', 'gAAAAABmbnCmihd37GDgMLpAcQE-tSLJE38Dvy3iPMrkfegpXotEJc31kC65wQrzk0cO-SKl-QUoGZwF7AnIBCMgvUOvw18kJjFteH1aHitnjq0sUxMg6Pg=', 11),
('gAAAAABmbnCmG2NfnQK4KMDIGJJEF2AZyLqneEiy_5-GAgjBUsvpbWXbrLeyhgHAAktEOzCQ6tQd5Z9tEscSq7_J5-Rz3r8biQ==', 'gAAAAABmbnCm9XnaeqYyX1ln2loSf2789FMlugDyEokwHp8GuQ9sr_oGi-JiP3l90oWsWYzsghqWMso96mTDJbRMOLuQoU3MbQ==', 'gAAAAABmbnCmtQHRFenTGpltbTEYN1s4nBJbGGsvmg4jqMMHld8lQfvROZxa8ueoOCHHLs9_d6Oax8mT838RtaVG-I_7g3vcug==', 'gAAAAABmbnCmFJsazsy8r7p5i68XHJygxLieDLR97QpMUmK4VMUqMPiwOKgtYdg89WH-SbYhPoUhwh0DrB4uMucePFU8Bh0hNnNsGb4dLhgC4Bl5rUaePp4=', 12),
('gAAAAABmbnCmMArTmESSdMdWkXbgKphjuXYI3SstOUdHQtaaCRZVUkGzzMBt3mtgy6pazEX5ju7sT1p9PEK5lJ2H2YaETTzzTw==', 'gAAAAABmbnCmZQeU0rgJmJZ1tO4I7YdOtoohi1omJWmFSV0k5BfyYq-1jveS-iC2OBwAfnc5F0d5LlAooPdNQeuTSPl4DZmcXQ==', 'gAAAAABmbnCmdaXyBEEhEjRd74CMus4CGMt54wv0vqMc0ZnI3rwFilBtKvSb6JoWtbVSJ_XBV73v-_IOO1H4qYdG4orqysrZ5Q==', 'gAAAAABmbnCmzmZpghk_Q-HCGy9EoC5jxpSXd11wX_mUZ0Z3BBmWPQhwTMI3cfU0UEeLwzSfp8M36KDdA4D5C6dZEynoRLKCvebwmWpGWhyucccNvsbi3K8=', 17),
('gAAAAABmbnCmjVKxYzPILo-5h2qUq6ZEFORuYUXacurAXQGNJet-4bj-dk95n5XRu0w5RU3PkHbKgAFcqFyxISy_Vssx2FFDcA==', 'gAAAAABmbnCmkXvs1QQMCMbCwh9LG0-97edIvOEJ5Ob2W0ijvGcNbnwrLoP45cYNuaqBPxYr4z4w7yJux6iIfm2-FkY6A3Gyjw==', 'gAAAAABmbnCmgQfxqxuoNltY7DMQZWPwN_2U4TNbvHy1WOkfQBsxYkWNlGa7buft92xwLAQF5cyCQYEtNHcUEyXSVofj88O2xg==', 'gAAAAABmbnCm_8qhMZXBJ01MH05EnLJBL3vWV6Agcg7XLvtoVyxwLYsEsbuuuo7AYyLcCsFKkxtolfMQywXQ8kfIrVyFEqbaJjq7b3T4xLt5eb_ZzMXWxik=', 18),
('gAAAAABmbnCmILlnItTbhTmuDyRIsXBIzTuO3IHErzPJ5bMhKDZ5461uuoaMnCzufnG9an2QWgFqblyONDsBe5ip3FIH8LDiQA==', 'gAAAAABmbnCm3QKEzZwFUYWo1lr9mrqxy73ZZPGTID707lEipyaT4kFCRe6JvXow1y39BdWhK_89t2LDNvrNG0Iki8jVaU-BHw==', 'gAAAAABmbnCmso6E59J_GHkTgeqUjsI-bgQDexGLikhafCY02MXcxDPfY6DYbScbFPcHnopdCanDERG5pfZWh_6UBzUGVkA_7A==', 'gAAAAABmbnCmOgDNzKUxZoBVcKhQ1GCHjeX1-Ip8nSng6PZFalXlSe18y5jH4o9AOROJtZYv8JPvOxuLs22g69hrfDsU0cCLFUYzlHlzftyhJHlLr6VJlVg=', 21),
('gAAAAABmbnCmQtVyQc7Um1WMa1WTyg78yNRW7Ny8Hp88Wu5bk5y8sZEO-F6CCrPksk7DxE9ztqwzG-h1enUhS5FW0U2KwHKyqA==', 'gAAAAABmbnCmQWG0UigbdcX_WqzLch7oB6NEq_sojvcMswlreSroc0HAW5XJ7tSqS8MsQo1SkFNm5lrtUOSa1LvzSsqxCKS0PA==', 'gAAAAABmbnCmTMxGBLk229C_zfOMV0ZK8xE0mSK4id23HKmZtHC95JVErrt9sg4HTJ_QgfKNjvHkWZYIvrPHxn2_zRAlgGszTg==', 'gAAAAABmbnCmSGjehSPx3zcbT6dcRot5PfX8rnDuieZO9Ywq2nhYh1dH7WTp2_nKjYlc8ATLze6MFrKS1IRxBJtEUZ4s6lrOlZ4Quc3enL_jshhOTReFX0Y=', 1),
('gAAAAABmbnCmYvcn9Ww-rbh-9UmQyBsIzmy72WNQrbcQB9tO6nv_gM9fUXtP45qETiADwYivrqmHZJ9OCAGZdjbpALWFFRtKQw==', 'gAAAAABmbnCmPDfKyt_38WWS2QfcwCaXvy2VgCkJzAszeXh-9WkfmgMEix3iUQLnckGRM4PHYW-DJRKqTHq3sOB7k1pnQO8xag==', 'gAAAAABmbnCmjd8ZjzeQ903oQHSAh_3EywA5LcxYdjIZ44NKLEo3jYKWXBvvg-x9FcNfk_jGBDplBM3iaE7cCTLw0Mnms1javQ==', 'gAAAAABmbnCmB3c140591EoQEw7fCOQXj7NEua6Z1QtnTeuPm5AMMN2OIwTAY5NsrRblk0ykazY4QgSn0JHcjQiAYAwrubivyHH8rY36FiBXFmcLTRVN8G0=', 22);



INSERT INTO Solicitud (fecha, descripcion, usuario_id, usuario_labor_id, labor_id, tarjeta_id) VALUES 
('2024-01-11', 'Limpieza profunda del baño', 1, 3, 1, 1),
('2024-01-12', 'Corte de césped y plantas', 2, 4, 2, 2),
('2024-01-13', 'Pintura de la fachada', 7, 9, 3, 3),
('2024-01-14', 'Transporte de muebles a otro sitio', 8, 10, 4, 4),
('2024-01-15', 'Reparación de la tubería del fregadero', 11, 13, 5, 5),
('2024-01-16', 'Instalación de nuevas luces', 12, 14, 6, 6),
('2024-01-17', 'Reparación de una puerta', 17, 19, 7, 7),
('2024-01-18', 'Cambio de aceite del coche', 18, 20, 8, 8),
('2024-01-19', 'Desarrollo de una aplicación web', 21, 23, 9, 9),
('2024-01-20', 'Clases de matemáticas avanzadas', 22, 24, 10, 10),
('2024-01-21', 'Limpieza de ventanas', 1, 3, 1, 1),
('2024-01-22', 'Mantenimiento del jardín', 2, 4, 2, 2),
('2024-01-23', 'Pintura de la cocina', 7, 9, 3, 3),
('2024-01-24', 'Mudanza de oficina', 8, 10, 4, 4),
('2024-01-25', 'Reparación de fuga en el baño', 11, 13, 5, 5),
('2024-01-26', 'Reparación de cortocircuito', 12, 14, 6, 6),
('2024-01-27', 'Construcción de un mueble', 17, 19, 7, 7),
('2024-01-28', 'Reparación de frenos', 18, 20, 8, 8),
('2024-01-29', 'Mantenimiento de software', 21, 23, 9, 9),
('2024-01-30', 'Preparación para exámenes', 22, 24, 10, 10);

INSERT INTO Solicitud (fecha, descripcion, usuario_id, usuario_labor_id, labor_id, tarjeta_id) VALUES 
('2024-01-01', 'Limpieza general de casa', 1, 3, 1, 1),
('2024-01-02', 'Jardinería en el patio', 2, 4, 2, 2),
('2024-01-03', 'Pintura de la sala', 7, 9, 3, 3),
('2024-01-04', 'Mudanza de muebles', 8, 10, 4, 4),
('2024-01-05', 'Plomería en el baño', 11, 13, 5, 5),
('2024-01-06', 'Reparación eléctrica', 12, 14, 6, 6),
('2024-01-07', 'Carpintería en la cocina', 17, 19, 7, 7),
('2024-01-08', 'Reparación del auto', 18, 20, 8, 8),
('2024-01-09', 'Desarrollo de software', 21, 23, 9, 9),
('2024-01-10', 'Clases de matemáticas', 22, 24, 10, 10);


INSERT INTO Calificacion (estrellas, comentario, fecha_calificacion, solicitud_id) VALUES 
(5, 'Excelente servicio de limpieza', '2024-01-05', 1),
(4, 'Buen trabajo en el jardín', '2024-01-06', 2),
(5, 'Pintura impecable', '2024-01-07', 3),
(3, 'Mudanza aceptable', '2024-01-08', 4),
(4, 'Plomería bien hecha', '2024-01-09', 5),
(5, 'Reparación eléctrica rápida', '2024-01-10', 6),
(4, 'Trabajo de carpintería bueno', '2024-01-11', 7),
(5, 'Reparación del auto perfecta', '2024-01-12', 8),
(5, 'Desarrollo de software excelente', '2024-01-13', 9),
(4, 'Clases de matemáticas útiles', '2024-01-14', 10);

INSERT INTO Calificacion (estrellas, comentario, fecha_calificacion, solicitud_id) VALUES 
(4, 'Buena limpieza del baño', '2024-01-12', 11),
(5, 'Corte de césped excelente', '2024-01-13', 12),
(4, 'Pintura de fachada bien hecha', '2024-01-14', 13),
(3, 'Transporte aceptable', '2024-01-15', 14),
(5, 'Reparación rápida y efectiva', '2024-01-16', 15),
(4, 'Instalación de luces correcta', '2024-01-17', 16),
(5, 'Reparación de puerta impecable', '2024-01-18', 17),
(4, 'Cambio de aceite rápido', '2024-01-19', 18),
(5, 'Aplicación web excelente', '2024-01-20', 19),
(4, 'Clases de matemáticas útiles', '2024-01-21', 20),
(5, 'Limpieza de ventanas perfecta', '2024-01-22', 21),
(4, 'Jardín bien mantenido', '2024-01-23', 22),
(5, 'Pintura de cocina impecable', '2024-01-24', 23),
(3, 'Mudanza de oficina aceptable', '2024-01-25', 24),
(4, 'Reparación de fuga efectiva', '2024-01-26', 25),
(5, 'Cortocircuito reparado rápidamente', '2024-01-27', 26),
(4, 'Construcción de mueble buena', '2024-01-28', 27),
(5, 'Frenos reparados perfectamente', '2024-01-29', 28),
(5, 'Mantenimiento de software impecable', '2024-01-30', 29),
(4, 'Clases preparatorias útiles', '2024-01-31', 30);










