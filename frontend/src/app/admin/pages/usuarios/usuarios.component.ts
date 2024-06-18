import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { User } from 'src/app/shared/interfaces/user-response.interface';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-usuarios',
  templateUrl: './usuarios.component.html',
  styleUrls: ['./usuarios.component.scss'],
})
export class UsuariosComponent  implements OnInit {

  public baseUrl: string = environment.baseUrl;

  private http: HttpClient = inject(HttpClient);

  private token = localStorage.getItem('token');
  private headers = new HttpHeaders().set('Authorization', `Bearer ${this.token}`);

  public users: any[] = [];

  ngOnInit(): void {
    this.http.get<User[]>(`${this.baseUrl}/users/administrador`, { headers: this.headers, withCredentials: true })
      .subscribe({
        next: (users: User[]) => {
          this.users.push(...users);
        },
        error: (error) => {
          console.log(error);
        }
      });

      console.log( this.users )

  }
}
