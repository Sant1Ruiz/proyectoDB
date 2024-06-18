import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-calificar-worker',
  templateUrl: './calificar-worker.component.html',
  styleUrls: ['./calificar-worker.component.scss'],
})
export class CalificarWorkerComponent {

  public baseUrl = environment.baseUrl;

  private http = inject(HttpClient);
  private route = inject(ActivatedRoute);
  private fb = inject(FormBuilder);
  private router = inject(Router);

  public alertMessage!: string;
  isAlertOpen = false;
  alertButtons = ['Aceptar'];


  public calificacionForm = this.fb.group({
    calificacion: ['', [Validators.required]],
    comentario: ['', [Validators.required]],
  });


  setOpenAlert(isOpen: boolean, success?: boolean) {
    this.isAlertOpen = isOpen;
    if (success) {
      // Ir a la página de solicitudes y refrescar la página
      this.router.navigate(['/client/solicitudes'], { queryParams: { refresh: new Date().getTime() } });
    }
  }

  onSubmit() {
    const body: FormData = new FormData();

    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);

    const { calificacion, comentario } = this.calificacionForm.value;

    body.append('estrellas', calificacion?.toString() as string);
    body.append('comentario', comentario as string);

    this.route.params.subscribe(params => {
      const solicitud_id = params['id'];

      this.http.post(`${this.baseUrl}/calificacion/${solicitud_id}`, body, { headers })
      .subscribe({
        next: (response) => {
          console.log(response);
          this.alertMessage = 'Calificación enviada exitosamente';
          this.setOpenAlert(true);
        },
        error: (error: any) => {
          console.log(error);
        }
      });
    });



  }

}
