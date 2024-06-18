import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { WorkerPageRoutingModule } from './worker-routing.module';

import { WorkerPage } from './worker.page';
import { ReviewsHistoryComponent } from './pages/reviews-history/reviews-history.component';
import { CuentaComponent } from './pages/cuenta/cuenta.component';
import { SolicitudesListComponent } from './pages/solicitudes-list/solicitudes-list.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    WorkerPageRoutingModule
  ],
  declarations: [
    WorkerPage,
    ReviewsHistoryComponent,
    CuentaComponent,
    SolicitudesListComponent
  ]
})
export class WorkerPageModule {}
