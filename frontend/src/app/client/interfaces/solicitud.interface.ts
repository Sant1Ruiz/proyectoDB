import { Worker } from "src/app/shared/interfaces/worker.interface";

export interface Solicitud {
  descripcion:      string;
  fecha:            string;
  labor_id:         number;
  numero_tarjeta:   string;
  solicitud_id:     number;
  tarjeta_id:       number;
  tipo_tarjeta:     string;
  usuario_id:       number;
  usuario_labor_id: number;
  trabajador?:      Worker;
  calificacion?:    number;
  isCalificado?:    boolean;
}
