import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { Error404Component } from './shared/pages/error404/error404.component';
import { isNotAuthenticatedGuard } from './authentication/guards/isNotAuthenticated.guard';
import { isAuthenticatedGuard } from './authentication/guards/isAuthenticated.guard';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'authentication',
    pathMatch: 'full'
  },
  {
    path: 'authentication',
    canActivate: [ isNotAuthenticatedGuard ],
    loadChildren: () => import('./authentication/authentication.module').then( m => m.AuthenticationPageModule)
  },
  {
    path: 'client',
    canActivate: [ isAuthenticatedGuard ],
    loadChildren: () => import('./client/client.module').then( m => m.ClientPageModule)
  },
  {
    path: 'admin',
    canActivate: [ isAuthenticatedGuard ],
    loadChildren: () => import('./admin/admin.module').then( m => m.AdminPageModule)
  },
  {
    path: 'worker',
    canActivate: [ isAuthenticatedGuard ],
    loadChildren: () => import('./worker/worker.module').then( m => m.WorkerPageModule)
  },
  {
    path: '404',
    component: Error404Component
  },
  // {
  //   path: '**',
  //   redirectTo: '404'
  // }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
