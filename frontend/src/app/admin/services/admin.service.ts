import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Injectable, inject } from "@angular/core";
import { catchError, map, throwError } from "rxjs";
import { environment } from "src/environments/environment";
import { Worker } from "../../shared/interfaces/worker.interface";


@Injectable({
  providedIn: 'root'
})
export class AdminService {

  private baseUrl = environment.baseUrl;

  private http = inject(HttpClient);

  public getWorkers() {
    const headers: HttpHeaders = new HttpHeaders()
    .set('Authorization', `Bearer ${localStorage.getItem('token')}`);

    return this.http.get<Worker[]>(`${this.baseUrl}/users/trabajador`, { headers })
      .pipe(
        map( response => response ),
        catchError((error) => {
          console.error(error)
          return throwError(console.error)
        })
      )
  }


}
