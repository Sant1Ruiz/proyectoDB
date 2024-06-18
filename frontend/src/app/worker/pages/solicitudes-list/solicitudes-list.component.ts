import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { AuthService } from 'src/app/authentication/services/auth.service';
import { Solicitud } from 'src/app/client/interfaces/solicitud.interface';
import { User } from 'src/app/shared/interfaces/user-response.interface';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'worker-solicitudes-list',
  templateUrl: './solicitudes-list.component.html',
  styleUrls: ['./solicitudes-list.component.scss'],
})
export class SolicitudesListComponent implements OnInit {

  public baseUrl = environment.baseUrl;
  private _authService = inject(AuthService);
  private http = inject(HttpClient);

  public user = this._authService.user();

  public solicitudes: any[] = [];

  public alertMessage!: string;
  isAlertOpen = false;
  alertButtons = ['Aceptar'];

  private token = localStorage.getItem('token');
  public headers = new HttpHeaders().set('Authorization', `Bearer ${this.token}`);

  ngOnInit() {
    this.http.get<Solicitud[]>(`${this.baseUrl}/solicitud/${this.user?.id}`, { headers: this.headers })
      .subscribe((solicitudes: Solicitud[]) => {
        if (solicitudes.length === 0) return;
        solicitudes.map((solicitud: Solicitud) => {
          if (!solicitud.usuario_id) return;
          this.http.get<User>(`${this.baseUrl}/user/${solicitud.usuario_id}`, { headers: this.headers })
            .subscribe({
              next: (cliente: User) => {
                this.solicitudes.push({ solicitud, cliente });
              },
              error: (error: any) => {
                console.log(error);
              }
            });
        });
        console.log( this.solicitudes )
      })
  }

  completarSolicitud(solicitud_id: number) {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);

    this.http.post<{ msg: string }>(`${this.baseUrl}/solicitud/${solicitud_id}`, null, { headers })
      .subscribe({
        next: (response: { msg: string }) => {
          console.log(response);
          this.alertMessage = response.msg;
          this.setOpenAlert(true, true);
        },
        error: (error: any) => {
          this.alertMessage = 'Error al completar la solicitud';
          this.setOpenAlert(true, false);
          console.log(error);
        }
      })
  }

  setOpenAlert(isOpen: boolean, success?: boolean) {
    this.isAlertOpen = isOpen;
  }

}
