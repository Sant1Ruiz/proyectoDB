import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { Solicitud } from 'src/app/client/interfaces/solicitud.interface';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-solicitudes',
  templateUrl: './solicitudes.component.html',
  styleUrls: ['./solicitudes.component.scss'],
})
export class SolicitudesComponent  implements OnInit {

  public baseUrl: string = environment.baseUrl;

  private http: HttpClient = inject(HttpClient);

  private token = localStorage.getItem('token');
  private headers = new HttpHeaders().set('Authorization', `Bearer ${this.token}`);

  public history: Solicitud[] = [];

  ngOnInit() {
    this.http.get<Solicitud[]>(`${this.baseUrl}/history`, { headers: this.headers })
      .subscribe({
        next: (history: Solicitud[]) => {
          this.history = history;
        },
        error: (error) => {
          console.log(error);
        }
      });
  }


}
