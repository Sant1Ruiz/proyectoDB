import { Component, Input, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-alert',
  templateUrl: './alert.component.html',
  styleUrls: ['./alert.component.scss'],
})
export class AlertComponent  implements OnInit {


  public isAlertVisible: boolean = false;

  @Input()
  public alertMessage: string = '';

  @Input()
  public alertButtons: string[] = [];

  // Funcion que se ejecuta al hacer click en un boton del alert
  public alertButtonClicked(isOpen: boolean) {
    this.isAlertVisible = isOpen;
  }




  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }


}
