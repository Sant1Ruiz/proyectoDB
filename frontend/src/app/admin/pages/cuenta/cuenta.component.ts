import { Component, OnInit, inject } from '@angular/core';
import { AuthService } from 'src/app/authentication/services/auth.service';

@Component({
  selector: 'admin-cuenta',
  templateUrl: './cuenta.component.html',
  styleUrls: ['./cuenta.component.scss'],
})
export class CuentaComponent  implements OnInit {

  private _authService = inject(AuthService);

  public user = this._authService.user();
  public fullName = this._authService.fullName();
  public role = this._authService.role();

  ngOnInit() {}


  logout() {
    this._authService.logout();
  }

}
