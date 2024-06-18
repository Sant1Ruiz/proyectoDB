import { NgModule, importProvidersFrom } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { AuthenticationPageRoutingModule } from './authentication-routing.module';

import { AuthenticationPage } from './authentication.page';
import { LoginPageComponent } from './pages/login-page/login-page.component';
import { RegisterPageComponent } from './pages/register-page/register-page.component';
import { SharedPageModule } from '../shared/shared.module';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';


@NgModule({
  providers: [
    importProvidersFrom(HttpClientModule),
    importProvidersFrom(
      HttpClientXsrfModule.withOptions({
        cookieName: 'session',
        headerName: 'X-CSRFToken'
      })
    )
  ],
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    SharedPageModule,
    HttpClientModule,
    AuthenticationPageRoutingModule,
    ReactiveFormsModule
  ],
  declarations: [
    AuthenticationPage,
    LoginPageComponent,
    RegisterPageComponent
  ]
})
export class AuthenticationPageModule {}
