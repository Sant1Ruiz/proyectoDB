import { Component, computed, effect, inject } from '@angular/core';
import { AuthService } from './authentication/services/auth.service';
import { Router } from '@angular/router';
import { AuthStatus } from './authentication/interfaces/auth-status.enum';
import { RolesRoutes } from 'src/helpers/roles';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {

  public authService = inject( AuthService );
  public router = inject( Router );


  public finishedAuthCheck = computed<boolean>(() => {
    if ( this.authService.authStatus() === AuthStatus.checking ) return false;
    return true;
  });

  public authStatusChangedEffect = effect(() => {

    console.log( this.authService.authStatus()  );

    switch( this.authService.authStatus() ) {
      case AuthStatus.checking:
        return;
      case AuthStatus.authenticated:
        const currentRoute = this.router.url;
        const role: 'administrador' | 'trabajador' | 'cliente' = this.authService.role() as 'administrador' | 'trabajador' | 'cliente';
        if ( currentRoute === '/404' || currentRoute === '/authentication/login' || currentRoute === '/authentication/register' ) {
          this.router.navigateByUrl(`${RolesRoutes[role]}`);
        }
        return;
      case AuthStatus.notAuthenticated:
        if ( this.router.url === '/authentication/register' ) return;
        this.router.navigateByUrl('/authentication/login');
        return;
    }
  })

}
