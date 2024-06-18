import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AdminPage } from './admin.page';
import { isAuthenticatedGuard } from '../authentication/guards/isAuthenticated.guard';
import { WorkersMapComponent } from './pages/workers-map/workers-map.component';
import { UsuariosComponent } from './pages/usuarios/usuarios.component';
import { SolicitudesComponent } from './pages/solicitudes/solicitudes.component';
import { CuentaComponent } from './pages/cuenta/cuenta.component';

const routes: Routes = [
  {
    path: '',
    component: AdminPage,
    children: [
      {
        path: 'mapa',
        canActivate: [isAuthenticatedGuard],
        component: WorkersMapComponent
      },
      {
        path: 'usuarios',
        canActivate: [isAuthenticatedGuard],
        component: UsuariosComponent
      },
      {
        path: 'solicitudes',
        canActivate: [isAuthenticatedGuard],
        component: SolicitudesComponent
      },
      {
        path: 'cuenta',
        canActivate: [isAuthenticatedGuard],
        component: CuentaComponent
      },
      {
        path: '**',
        redirectTo: 'mapa'
      }
    ]
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AdminPageRoutingModule { }
