import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SAMPLEDBVERSION_MODULE_DECLARATIONS, SampleDBVersionRoutingModule} from  './SampleDBVersion-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SampleDBVersionRoutingModule
  ],
  declarations: SAMPLEDBVERSION_MODULE_DECLARATIONS,
  exports: SAMPLEDBVERSION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SampleDBVersionModule { }