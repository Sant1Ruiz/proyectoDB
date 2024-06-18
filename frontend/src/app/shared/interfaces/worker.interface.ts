export interface Worker {
  apellido:         string;
  disponibilidad:   boolean;
  email:            string;
  estrellas:        number;
  foto_perfil:      string;
  imagen_documento: string;
  latitud:          string;
  longitud:         string;
  nombre:           string;
  password:         string;
  recibo_publico?:   null;
  nombre_labor?:     string;
  telefono:         string;
  usuario_id:       number;
  precio_hora:      string;
  labor?:          string;
}
