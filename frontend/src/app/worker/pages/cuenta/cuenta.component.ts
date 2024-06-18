import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { AuthService } from 'src/app/authentication/services/auth.service';
import { environment } from 'src/environments/environment';
import { Worker } from 'src/app/shared/interfaces/worker.interface';
import { Solicitud } from 'src/app/client/interfaces/solicitud.interface';

@Component({
  selector: 'worker-cuenta',
  templateUrl: './cuenta.component.html',
  styleUrls: ['./cuenta.component.scss'],
})
export class CuentaComponent implements OnInit {

  public baseUrl = environment.baseUrl;
  private _authService = inject(AuthService);
  private http = inject(HttpClient);

  public user = this._authService.user();
  public fullName = this._authService.fullName();
  public role = this._authService.role();

  public trabajador!: Worker;



  ngOnInit(): void {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);

    this.http.get<Worker>(`${this.baseUrl}/user/${this.user?.id}`, { headers })
      .subscribe((trabajador: Worker) => {
        this.trabajador = trabajador;
      })

  }

  logout() {
    this._authService.logout();
  }
}
