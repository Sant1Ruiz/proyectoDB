import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ClientPageRoutingModule } from './client-routing.module';

import { ClientPage } from './client.page';
import { SharedPageModule } from '../shared/shared.module';
import { BuscarServiciosComponent } from './pages/buscar-servicios/buscar-servicios.component';
import { CuentaComponent } from './pages/cuenta/cuenta.component';
import { ServiciosComponent } from './pages/servicios/servicios.component';
import { SolicitudesComponent } from './pages/solicitudes/solicitudes.component';
import { SolicitarWorkerComponent } from './pages/solicitar-worker/solicitar-worker.component';
import { WorkersListComponent } from './pages/workers-list/workers-list.component';
import { CalificarWorkerComponent } from './pages/calificar-worker/calificar-worker.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    SharedPageModule,
    ClientPageRoutingModule,
    ReactiveFormsModule
  ],
  declarations: [
    ClientPage,
    BuscarServiciosComponent,
    CuentaComponent,
    ServiciosComponent,
    SolicitudesComponent,
    SolicitarWorkerComponent,
    WorkersListComponent,
    CalificarWorkerComponent
  ]
})
export class ClientPageModule {}
