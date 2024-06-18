import { Component, OnInit, inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { RolesRoutes, rolesArray } from 'src/helpers/roles';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss'],
})
export class LoginPageComponent  implements OnInit {

  private fb = inject(FormBuilder);
  private authService = inject(AuthService);
  private router = inject(Router);

  isAlertOpen = false;
  alertButtons = ['Aceptar'];

  private CSRFToken: string = '';

  public roles = rolesArray;

  public loginForm: FormGroup = this.fb.group({
    role: ['', [Validators.required]],
    login: ['', [Validators.required, Validators.minLength(3)]],
    password: ['', [Validators.required, Validators.minLength(4)]],
  });

  ngOnInit() {
    this.authService.getAuthToken('login')
      .subscribe(token => this.CSRFToken = token);
  }

  setOpenAlert(isOpen: boolean) {
    this.isAlertOpen = isOpen;
  }

  onSubmit() {
    const role: 'administrador' | 'trabajador' | 'cliente' = this.loginForm.get('role')?.value;
    const { login, password } = this.loginForm.value;

    if (!this.loginForm.valid) {
      this.setOpenAlert(true);
      this.loginForm.markAllAsTouched();
      return;
    }

    this.authService.login(this.CSRFToken, login, password)
      .subscribe({
        next: () => this.router.navigateByUrl(`/${RolesRoutes[role]}`),
        error: (error) => {
          this.setOpenAlert(true)
        }
      });
  }


}
