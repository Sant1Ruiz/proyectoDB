import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { WorkerPage } from './worker.page';
import { SolicitudesListComponent } from './pages/solicitudes-list/solicitudes-list.component';
import { CuentaComponent } from './pages/cuenta/cuenta.component';
import { ReviewsHistoryComponent } from './pages/reviews-history/reviews-history.component';

const routes: Routes = [
  {
    path: '',
    component: WorkerPage,
    children: [
      {
        path: 'solicitudes',
        component: SolicitudesListComponent
      },
      {
        path: 'cuenta',
        component: CuentaComponent
      },
      {
        path: 'calificaciones',
        component: ReviewsHistoryComponent
      },
      {
        path: '**',
        redirectTo: 'solicitudes'
      }
    ]
  },

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class WorkerPageRoutingModule {}
