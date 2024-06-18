import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Worker } from 'src/app/shared/interfaces/worker.interface';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-workers-list',
  templateUrl: './workers-list.component.html',
  styleUrls: ['./workers-list.component.scss'],
})
export class WorkersListComponent  implements OnInit {

  public baseUrl: string = environment.baseUrl;

  private http = inject(HttpClient);
  private route = inject(ActivatedRoute);

  public workerName: string = '';


  public workersList: Worker[] = [];

  public isClicked: boolean = false;

  ngOnInit() {
    this.route.params.subscribe(
      (params) => {
        this.workerName = params['nombre'];

        const token = localStorage.getItem('token');
        const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);

        this.http.get<Worker[]>(`${this.baseUrl}/labor/${params['nombre']}`, { headers })
          .subscribe(
            (workers: Worker[]) => {
              this.workersList = workers;
              console.log( workers );
            }
          )
      }
    )
  }

}
