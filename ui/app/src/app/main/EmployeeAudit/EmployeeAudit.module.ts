import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {EMPLOYEEAUDIT_MODULE_DECLARATIONS, EmployeeAuditRoutingModule} from  './EmployeeAudit-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    EmployeeAuditRoutingModule
  ],
  declarations: EMPLOYEEAUDIT_MODULE_DECLARATIONS,
  exports: EMPLOYEEAUDIT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class EmployeeAuditModule { }