import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Worker } from 'src/app/shared/interfaces/worker.interface';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-solicitar-worker',
  templateUrl: './solicitar-worker.component.html',
  styleUrls: ['./solicitar-worker.component.scss'],
})
export class SolicitarWorkerComponent implements OnInit {

  public baseUrl = environment.baseUrl;

  private http = inject(HttpClient);
  private route = inject(ActivatedRoute);
  private fb = inject(FormBuilder);
  private router = inject(Router);

  public worker!: Worker;
  public nombreLabor: string = '';
  private trabajador_id!: number;

  public alertMessage!: string;
  isAlertOpen = false;
  alertButtons = ['Aceptar'];

  /*
    /solicitud/add POST
    Este endpoint espera un DATAFORM(descripcion, trabajador_id), y este endpoint solo funciona si el usuario es un Cliente
  */
  public solicitudForm = this.fb.group({
    descripcion: ['', [Validators.required]],
    trabajador_id: [{ value: this.trabajador_id }, [Validators.required]],
  });

  setOpenAlert(isOpen: boolean, success?: boolean) {
    this.isAlertOpen = isOpen;
    if (success) {
      // Ir a la página de solicitudes y refrescar la página
      this.router.navigate(['/client/solicitudes'], { queryParams: { refresh: new Date().getTime() } });
    }


  }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.nombreLabor = decodeURIComponent(params['nombre']);
      this.trabajador_id = params['id'];

      const token = localStorage.getItem('token');
      const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);

      this.http.get<Worker>(`${this.baseUrl}/user/${params['id']}`, { headers })
        .subscribe(
          (worker: Worker) => {
            this.worker = worker;
          }
        )
    });
  }

  onSubmit() {
    if (this.solicitudForm.invalid) {
      console.log(this.solicitudForm.value);
      this.alertMessage = 'Datos sin rellenar. Revisa nuevamente.'
      this.setOpenAlert(true);
      this.solicitudForm.markAllAsTouched();
      return;
    }

    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);

    const formdata = new FormData();
    const solitudData = this.solicitudForm.value;
    formdata.append('descripcion', solitudData.descripcion as string);
    formdata.append('trabajador_id', this.trabajador_id.toString());


    this.http.post(`${this.baseUrl}/solicitud/add`, formdata, { headers })
      .subscribe({
        next: (result) => {
          this.alertMessage = 'Solicitud enviada con éxito.';
          this.setOpenAlert(true);
          console.log(result);
        },
        error: (error) => {
          this.alertMessage = 'Error al enviar la solicitud. Intente nuevamente.';
          this.setOpenAlert(true);
        }
      });
  }



}
