import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';
import { IconComponent } from './components/icon/icon.component';
import { IconoNotificacionComponent } from './components/icono-notificacion/icono-notificacion.component';
import { HeaderComponent } from './components/header/header.component';
import { CardComponent } from './components/card/card.component';
import { AlertComponent } from './components/alert/alert.component';



@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
  ],
  declarations: [
    IconComponent,
    IconoNotificacionComponent,
    HeaderComponent,
    CardComponent,
    AlertComponent
  ],
  exports: [
    IconComponent,
    IconoNotificacionComponent,
    HeaderComponent,
    CardComponent,
    AlertComponent
  ]

})
export class SharedPageModule { }
