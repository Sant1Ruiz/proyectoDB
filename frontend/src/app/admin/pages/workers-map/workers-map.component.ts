import { Component, OnInit, inject } from '@angular/core';
import { Icon, Map, Marker, latLng, marker, tileLayer } from 'leaflet';
import { GeolocationService } from 'src/app/shared/services/geolocation.service';
import { AdminService } from '../../services/admin.service';
import { delay } from 'rxjs';

@Component({
  selector: 'app-workers-map',
  templateUrl: './workers-map.component.html',
  styleUrls: ['./workers-map.component.scss'],
})
export class WorkersMapComponent implements OnInit {

  public geoLocation = inject(GeolocationService);
  public adminService = inject(AdminService);

  public options = {
    layers: [
      tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      })
    ],
    zoom: 14,
    center: latLng(this.geoLocation.latCali, this.geoLocation.lonCali)
  }

  public layers: Marker[] = [];

  ngOnInit() {
    this.adminService.getWorkers().subscribe(
      workers => {
        workers.forEach(worker => {
          this.layers.push(
            marker([ parseFloat(worker.latitud), parseFloat(worker.longitud)])
              .bindPopup(`<b>${worker.nombre} ${worker.apellido}</b><center>Labor: <i>${worker.nombre_labor}</i></center>`)
              .setIcon( new Icon({
                iconSize: [ 25, 41 ],
                iconAnchor: [ 13, 41 ],
                iconUrl: '../../../../assets/icon/map-pin.svg',
                shadowUrl: '../../../../assets/icon/map-pin.svg'
              }) )
              .openPopup()
          );
        });
        console.log( this.layers )
      }
    );

  }

  async onMapReady( map: Map ) {
    await this.delay(10);
    map.invalidateSize(false);
  }

  delay(ms: number) {
    return new Promise( resolve => setTimeout(resolve, ms) );
  }




}
