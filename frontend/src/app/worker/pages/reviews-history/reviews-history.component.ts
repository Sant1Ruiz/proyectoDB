import { HttpClient } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { AuthService } from 'src/app/authentication/services/auth.service';
import { environment } from 'src/environments/environment';
import { Calificacion } from '../../interfaces/calificacion.interface';

@Component({
  selector: 'app-reviews-history',
  templateUrl: './reviews-history.component.html',
  styleUrls: ['./reviews-history.component.scss'],
})
export class ReviewsHistoryComponent implements OnInit {

  public baseUrl = environment.baseUrl;
  private _authService = inject(AuthService);
  private http = inject(HttpClient);

  public user = this._authService.user();

  public califications: Calificacion[] = [];

  ngOnInit() {
    const token = localStorage.getItem('token');
    const headers = { Authorization: `Bearer ${token}` };


    this.http.get<Calificacion[]>(`${this.baseUrl}/calificacion/${this.user?.id}`, { headers })
      .subscribe((response: Calificacion[]) => {
        this.califications = response;
        console.log( this.califications )
      });
  }

}
