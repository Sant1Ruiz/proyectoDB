import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Address } from '../interfaces/address-result.interface';
import { Observable, catchError, map, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GeolocationService {

  public http = inject(HttpClient);

  public latCali: number = 3.43722;
  public lonCali: number = -76.5225;

  // Coordenadas del área de Cali
  public viewbox: string = '-76.606,3.539,-76.437,3.313';
  public bounded: number = 1; // Limitar la búsqueda a un área específica

  public getAddress(address: string, viewbox: string = this.viewbox, bounded: number = this.bounded): Observable<Address> {
    return this.http.get<Address[]>(`https://nominatim.openstreetmap.org/search?format=json&q=${address}&viewbox=${viewbox}&bounded=${bounded}`)
      .pipe(
        map((addresses) => addresses[0]), //! Obtener la primera dirección (Hay que cambiarlo)
        catchError((error) => throwError(console.error))
      );
  }

  public getAddressNameByCoordinates<Address>(lat: number, lon: number): Observable<Address> {
    return this.http.get<Address>(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`)
      .pipe(
        map((address) => address),
        catchError((error) => throwError(console.error))
      );
  }




  constructor() { }

}
