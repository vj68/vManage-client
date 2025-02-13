from vmngclient.primitives import APIPrimitiveBase, View
from vmngclient.session import ProviderAsTenantView, TenantView


class TenantBackupRestoreApi(APIPrimitiveBase):
    @View({ProviderAsTenantView})
    def delete_tenant_backup(self):
        # DELETE /tenantbackup/delete
        ...

    @View({ProviderAsTenantView, TenantView})
    def download_existing_backup_file(self):
        # GET /tenantbackup/download/{path}
        ...

    @View({ProviderAsTenantView, TenantView})
    def export_tenant_backup(self):
        # GET /tenantbackup/export
        ...

    @View({ProviderAsTenantView})
    def import_tenant_backup(self):
        # POST /tenantbackup/import
        ...

    @View({ProviderAsTenantView, TenantView})
    def list_tenant_backup(self):
        # GET /tenantbackup/list
        ...
