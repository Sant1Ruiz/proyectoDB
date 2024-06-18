import { Component, OnInit, inject } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { Roles, rolesArray } from 'src/helpers/roles';
import { Observable, catchError, retry, tap, throwError } from 'rxjs';
import { GeolocationService } from 'src/app/shared/services/geolocation.service';
import { LaborService } from 'src/app/shared/services/labor.service';

@Component({
  selector: 'app-register-page',
  templateUrl: './register-page.component.html',
  styleUrls: ['./register-page.component.scss'],
})
export class RegisterPageComponent implements OnInit {

  private fb = inject(FormBuilder);
  private authService = inject(AuthService);
  private router = inject(Router);
  private geolocationService = inject(GeolocationService);
  private laborService = inject(LaborService);

  public today: string = new Date().toISOString();

  private CSRFToken: string = '';

  public alertMessage!: string;
  isAlertOpen = false;
  alertButtons = ['Aceptar'];

  public thereIsDirection: boolean = false;

  // Excluir el rol de administrador

  public roles = rolesArray.filter((role) => role !== Roles.Administrador);

  // Images for the register form
  public reciboPublico: File | null = null;
  public imagenDocumento: File | null = null;
  public fotoPerfil: File | null = null;

  // Location parameters
  public latitud: number = 0;
  public longitud: number = 0;

  // Lista de labores
  public laboresList: string[] = [];

  public isClient: boolean = false;
  public isWorker: boolean = false;

  public tiposTarjeta = ['Crédito', 'Débito'];

  ngOnInit() {
    // this.authService.getAuthToken('register')
    //   .subscribe(token => this.CSRFToken = token);


    this.laborService.getLabores().subscribe((response) => { this.laboresList = response.labores });

    this.registerForm.valueChanges.subscribe((value) => {
      if (value.role === Roles.Cliente) {
        this.isClient = true;
        this.isWorker = false;
        this.registerForm.get('labor')?.clearValidators();
        this.registerForm.get('precio_hora')?.clearValidators();
        this.registerForm.get('tipo_tarjeta')?.setValidators([Validators.required]);
        this.registerForm.get('codigo_seguridad')?.setValidators([Validators.required]);
        this.registerForm.get('fecha_expiracion')?.setValidators([Validators.required]);
        this.registerForm.get('numero_tarjeta')?.setValidators([Validators.required]);
      }
      else if (value.role === Roles.Trabajador) {
        this.isClient = false;
        this.isWorker = true;
        this.registerForm.get('labor')?.setValidators([Validators.required]);
        this.registerForm.get('precio_hora')?.setValidators([Validators.required]);
      }

      if (value.direccion!.length >= 5 && this.registerForm.valid) {
        this.getLatLong();
      }

    });
  }


  getLatLong() {
    // Verificar si la dirección ya fue ingresada y que sea válida
    if (this.registerForm.get('direccion')?.value
      && this.registerForm.get('direccion')?.valid && !this.thereIsDirection) {
      const address = this.registerForm.get('direccion')?.value as string;
      this.geolocationService.getAddress(address)
        .subscribe((address) => {
          if (address) {
            this.registerForm.patchValue({
              latitud: parseFloat(address.lat),
              longitud: parseFloat(address.lon)
            }, { emitEvent: false });
            this.thereIsDirection = true;
          } else {
            console.log('Dirección no encontrada')
          }
        });
    }
  }

  public registerForm = this.fb.group({

    role: ['', [Validators.required]],
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(4)]],
    name: ['', [Validators.required, Validators.minLength(3)]],
    lastname: ['', [Validators.required, Validators.minLength(3)]],
    direccion: ['', [Validators.required, Validators.minLength(5)]],
    latitud: [this.latitud, [Validators.required]],
    longitud: [this.latitud, [Validators.required]],
    labor: ['', [Validators.minLength(3)]],
    precio_hora: ['', [Validators.minLength(2)]],
    telefono: ['', [Validators.required, Validators.minLength(3)]],
    tipo_tarjeta: ['', []],
    codigo_seguridad: ['', [Validators.minLength(3)]],
    fecha_expiracion: [this.today, []],
    numero_tarjeta: ['', [Validators.minLength(16)]],
    disponibilidad: [true],
  });



  serviciosPublicos(event: any) {
    this.reciboPublico = event.target.files[0];
  }

  documentoIdentidad(event: any) {
    this.imagenDocumento = event.target.files[0];
  }

  fotoPerfilImage(event: any) {
    this.fotoPerfil = event.target.files[0];
  }

  setOpenAlert(isOpen: boolean, success?: boolean) {
    this.isAlertOpen = isOpen;
    if (success)
      this.router.navigateByUrl(`/authentication/login`)
  }

  onSubmit() {

    this.getLatLong();

    if (!this.registerForm.valid) {
      console.log(this.registerForm.value);
      this.alertMessage = 'Datos incorrectos o sin rellenar. Revisa nuevamente.'
      this.setOpenAlert(true);
      this.registerForm.markAllAsTouched();
      return;
    }

    if (this.isClient) {
      if (!this.reciboPublico) {
        this.alertMessage = 'Debes adjuntar el recibo público para poder registrarte como cliente.'
        this.setOpenAlert(true);
        return;
      }
    }

    if (this.isWorker) {
      if (!this.fotoPerfil) {
        this.alertMessage = 'Debes adjuntar una foto de perfil para poder registrarte como trabajador.'
        this.setOpenAlert(true);
        return;
      }

      if (!this.imagenDocumento) {
        this.alertMessage = 'Debes adjuntar una imagen de tu documento de identidad para poder registrarte como trabajador.'
        this.setOpenAlert(true);
        return;
      }
    }

    const formdata = new FormData();
    const registerData = this.registerForm.value;

    formdata.append('name', registerData.name as string);
    formdata.append('lastname', registerData.lastname as string);
    formdata.append('email', registerData.email as string);
    formdata.append('password', registerData.password as string);
    formdata.append('latitud', registerData.latitud?.toString() as string);
    formdata.append('longitud', registerData.longitud?.toString() as string);
    formdata.append('telefono', registerData.telefono as string);

    if (registerData.role === Roles.Cliente) {
      //! Falta la implementación de añadir la tarjeta de crédito a la cuenta
      formdata.append('recibo_publico', this.reciboPublico as Blob);
      formdata.append('tipo_tarjeta', registerData.tipo_tarjeta as string);
      formdata.append('codigo_seguridad', registerData.codigo_seguridad as string);
      formdata.append('numero_tarjeta', registerData.numero_tarjeta as string);
      // La fecha de expiración se debe enviar en un formato que el atributo DATE en postgresql pueda entender
      formdata.append('fecha_expiracion', registerData.fecha_expiracion as string);
    }

    if (registerData.role === Roles.Trabajador) {
      formdata.append('labor', registerData.labor as string);
      formdata.append('precio_hora', registerData.precio_hora as string);
      formdata.append('foto_perfil', this.fotoPerfil as Blob);
      formdata.append('imagen_documento', this.imagenDocumento as Blob);
    }
    if (this.thereIsDirection) {
      this.authService.register(formdata, registerData.role as string)
        .subscribe({
          next: () => {
            //! Arreglar esto para que se muestre un mensaje de éxito
            this.alertMessage = 'Registro exitoso. Ahora puedes iniciar sesión.'
            this.setOpenAlert(true);
          },
          error: (error) => {
            console.error('Error en el registro: ', error);
            this.alertMessage = 'Error al registrarse. Por favor, inténtalo nuevamente.';
            this.setOpenAlert(true);
          }
        })
    }
  }
}
