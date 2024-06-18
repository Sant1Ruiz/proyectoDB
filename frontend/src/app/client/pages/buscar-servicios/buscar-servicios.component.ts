import { Component, OnInit, inject } from '@angular/core';
import { LaboresResponse } from 'src/app/shared/interfaces/labores-response.interface';
import { LaborService } from 'src/app/shared/services/labor.service';

@Component({
  selector: 'client-buscar-servicios',
  templateUrl: './buscar-servicios.component.html',
  styleUrls: ['./buscar-servicios.component.scss'],
})
export class BuscarServiciosComponent  implements OnInit {

  private laborService = inject(LaborService);

  private servicios: string[] = [];
  public results: string[] = [];

  ngOnInit() {
    this.laborService.getLabores().subscribe((response) => {
      this.servicios = response.labores;
      this.results = [...this.servicios];
    });
  }

  handleInput(event: any) {
    const query = event.target.value.toLowerCase();
    this.results = this.servicios.filter((d) => d.toLowerCase().indexOf(query) > -1);
  }

}
