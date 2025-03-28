import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SupplierHomeComponent } from './home/Supplier-home.component';
import { SupplierNewComponent } from './new/Supplier-new.component';
import { SupplierDetailComponent } from './detail/Supplier-detail.component';

const routes: Routes = [
  {path: '', component: SupplierHomeComponent},
  { path: 'new', component: SupplierNewComponent },
  { path: ':Id', component: SupplierDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Supplier-detail-permissions'
      }
    }
  }
];

export const SUPPLIER_MODULE_DECLARATIONS = [
    SupplierHomeComponent,
    SupplierNewComponent,
    SupplierDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SupplierRoutingModule { }