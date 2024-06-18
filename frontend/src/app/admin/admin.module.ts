import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AdminPageRoutingModule } from './admin-routing.module';

import { AdminPage } from './admin.page';
import { CuentaComponent } from './pages/cuenta/cuenta.component';
import { SolicitudesComponent } from './pages/solicitudes/solicitudes.component';
import { UsuariosComponent } from './pages/usuarios/usuarios.component';
import { WorkersMapComponent } from './pages/workers-map/workers-map.component';
import { LeafletModule } from '@asymmetrik/ngx-leaflet';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    LeafletModule,
    AdminPageRoutingModule
  ],
  declarations: [
    AdminPage,
    CuentaComponent,
    SolicitudesComponent,
    UsuariosComponent,
    WorkersMapComponent
  ]
})
export class AdminPageModule {}
