import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable, catchError, map, tap, throwError } from 'rxjs';
import { environment } from 'src/environments/environment';
import { LaboresResponse } from '../interfaces/labores-response.interface';
import { Labor } from '../interfaces/labor-response.interface';

@Injectable({
  providedIn: 'root'
})
export class LaborService {

  public http = inject(HttpClient);

  private url = environment.baseUrl

  private token = localStorage.getItem('token');
  private headers = new HttpHeaders().set('Authorization', `Bearer ${this.token}`);

  public getLabores(): Observable<LaboresResponse> {
    return this.http.get<LaboresResponse>(`${this.url}/register/trabajador`, { headers: this.headers })
      .pipe(
        map( response => response ),
        catchError((error) => throwError(console.error))
      )
  }

  public getLaboresDetails(): Observable<Labor[]> {
    return this.http.get<Labor[]>(`${this.url}/jobs/details`, { headers: this.headers })
      .pipe(
        map( response => response ),
        catchError((error) => throwError(console.error))
      )
  }




}
