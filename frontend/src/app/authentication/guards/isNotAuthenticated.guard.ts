import { inject } from '@angular/core';
import { Router, type CanActivateFn } from '@angular/router';
import { AuthStatus } from '../interfaces/auth-status.enum';
import { AuthService } from '../services/auth.service';
import { RolesRoutes } from 'src/helpers/roles';

export const isNotAuthenticatedGuard: CanActivateFn = (route, state) => {
  const authService = inject(AuthService);
  const router = inject(Router);

  if (authService.authStatus() === AuthStatus.authenticated) {
    const role: 'administrador' | 'trabajador' | 'cliente' = authService.role() as 'administrador' | 'trabajador' | 'cliente';

    if (!state.url.includes(RolesRoutes[role])) {
      console.log(`Redirigiendo a ${RolesRoutes[role]}`);
      router.navigateByUrl(`/${RolesRoutes[role]}`);
    }

    return false;
  };

  return true;
};
