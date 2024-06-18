import { Component, OnInit, inject } from '@angular/core';
import { AuthService } from 'src/app/authentication/services/auth.service';
import { Address } from 'src/app/shared/interfaces/address-result.interface';
import { GeolocationService } from 'src/app/shared/services/geolocation.service';

@Component({
  selector: 'app-cuenta',
  templateUrl: './cuenta.component.html',
  styleUrls: ['./cuenta.component.scss'],
})
export class CuentaComponent implements OnInit {

  private _authService = inject(AuthService);
  private _geolocationService = inject(GeolocationService);

  public user = this._authService.user();
  public fullName = this._authService.fullName();
  public role = this._authService.role();
  public addressName!: string;

  ngOnInit() {
    this._geolocationService
      .getAddressNameByCoordinates(parseFloat(this.user?.latitud as string), parseFloat(this.user?.longitud as string))
      .subscribe((address) => {
        this.addressName = (address as Address).display_name;
      });
  }


  logout() {
    this._authService.logout();
  }
}
