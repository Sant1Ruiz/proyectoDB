import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable, computed, inject, signal } from '@angular/core';
import { environment } from 'src/environments/environment';
import { AuthStatus } from '../interfaces/auth-status.enum';
import { CheckTokenResponse } from '../interfaces/check-token-response.interface';
import { Observable, catchError, map, of, switchMap, tap, throwError } from 'rxjs';
import { LoginResponse } from '../interfaces/login-response.interface';
import { RegisterResponse } from '../interfaces/register-response.interface';
import { AuthToken } from '../interfaces/auth-token.interface';
import { User } from 'src/app/shared/interfaces/user-response.interface';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly baseUrl = environment.baseUrl;

  // Injectable dependencies
  private http = inject(HttpClient);

  // Signals
  private _fullName = signal<string | null>(null);
  private _role = signal<string | null>(null);
  private _authStatus = signal<AuthStatus>(AuthStatus.checking);
  private _user = signal<User | null>(null);
  private _address = signal<string | null>(null);

  // Computed properties
  public fullName = computed(() => this._fullName());
  public role = computed(() => this._role());
  public authStatus = computed(() => this._authStatus());
  public user = computed(() => this._user());


  constructor() {
    this.checkAuthStatus().subscribe();
  }

  private setAuthentication(response: CheckTokenResponse | LoginResponse | User): boolean {
    this._fullName.set(response.name + ' ' + response.lastname);
    this._role.set(response.rol.toLowerCase());
    this._user.set(response as User);
    this._authStatus.set(AuthStatus.authenticated);

    return true;
  }

  login(CSRFToken: string, login: string, password: string): Observable<boolean> {

    console.log(CSRFToken);

    const url = `${this.baseUrl}/login`;
    const body = new FormData();
    body.append('username', login);
    body.append('password', password);
    body.append('X-CSRFToken', CSRFToken);

    return this.http.post<LoginResponse>(url, body, {
      withCredentials: true,
      headers: new HttpHeaders().set('X-CSRFToken', CSRFToken)
    })
      .pipe(
        map((response: LoginResponse) => {
          console.log(response);
          localStorage.setItem('token', response.access_token);
          return this.setAuthentication(response)
        }),
        catchError(error => {
          console.log('Error', error);
          return throwError(() => error);
        })
      );

  }

  getAuthToken(option: 'login' | 'register', role?: string): Observable<string> {
    let url = `${this.baseUrl}/${option}/${role}`;

    if (!role) url = `${this.baseUrl}/${option}`;

    return this.http.get<AuthToken>(url, { withCredentials: true })
      .pipe(
        map(({ csrf_token: token }) => token),
        catchError(error => throwError(() => error))
      );
  }

  //! Crear interfaz para registrar usuario
  register(user: any, role: string): Observable<boolean> {
    const url = `${this.baseUrl}/register/${role}`;
    const body = user;

    const headers = new HttpHeaders();
    this.getAuthToken(`register`, role).subscribe(
      token => {
        headers.set('x-CSRFToken', token)
        console.log(token);
      }
    );

    return this.http.post<RegisterResponse>(url, body, { headers })
      .pipe(
        // ! Cambiar esto cuando estén disponibles los endpoints de la API
        map((response: RegisterResponse) => {
          console.log(response);
          return true
        }),
        catchError(error => throwError(() => error))
      );
  }

  logout() {
    localStorage.removeItem('token');
    this._role.set(null);
    this._authStatus.set(AuthStatus.notAuthenticated);
    this._fullName.set(null);
    this._user.set(null);

    this.http.get(`${this.baseUrl}/logout`, { withCredentials: true }).subscribe(
      message => console.log(message),
    );
  }

  checkAuthStatus(): Observable<boolean> {
    const url = `${this.baseUrl}/verify/sesion`;
    const token = localStorage.getItem('token');

    if (!token) {
      this.logout();
      return of(false);
    }

    const headers = new HttpHeaders()
      .set('Authorization', `Bearer ${token}`);

    return this.http.get<CheckTokenResponse>(url, { headers })
      .pipe(
        map((response: CheckTokenResponse) => {
          console.log(response);
          return this.setAuthentication(response);
        }),
        catchError(error => {
          console.log(error);
          this._authStatus.set(AuthStatus.notAuthenticated);
          return of(false);
        })
      );
  }
}
