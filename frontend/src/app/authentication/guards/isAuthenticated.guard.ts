import { inject } from '@angular/core';
import { Router, type CanActivateFn } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { AuthStatus } from '../interfaces/auth-status.enum';
import { RolesRoutes } from 'src/helpers/roles';

export const isAuthenticatedGuard: CanActivateFn = (route, state) => {

  const authService = inject(AuthService);
  const router = inject(Router);

  if (authService.authStatus() === AuthStatus.authenticated) {
    const role: 'administrador' | 'trabajador' | 'cliente' = authService.role() as 'administrador' | 'trabajador' | 'cliente';

    if (!state.url.includes(RolesRoutes[role])) router.navigateByUrl(`/${RolesRoutes[role]}`);
    return true;
  };

  if (authService.authStatus() === AuthStatus.checking) { return false };

  router.navigateByUrl('/authentication/login');
  return false;
};
