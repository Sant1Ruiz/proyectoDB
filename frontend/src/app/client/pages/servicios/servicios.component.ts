import { HttpClient } from '@angular/common/http';
import { Component, OnInit, inject } from '@angular/core';
import { Labor } from 'src/app/shared/interfaces/labor-response.interface';
import { LaborService } from 'src/app/shared/services/labor.service';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-servicios',
  templateUrl: './servicios.component.html',
  styleUrls: ['./servicios.component.scss'],
})
export class ServiciosComponent implements OnInit {

  public baseUrl: string = environment.baseUrl;

  private laborService = inject(LaborService);

  public laboresList: Labor[] = [];

  ngOnInit() {
    this.laborService.getLaboresDetails()
      .subscribe(
        (labores: Labor[]) => {
          this.laboresList = labores;
        }
      )
  }


}
