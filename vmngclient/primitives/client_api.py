from datetime import datetime
from typing import Any, List, Optional

from packaging.version import Version  # type: ignore
from pydantic import BaseModel, Field

from vmngclient.primitives import APIPrimitiveBase


class VersionField(Version):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        return Version(value)


class ServerInfo(BaseModel):
    server: Optional[str]
    tenancy_mode: Optional[str] = Field(alias="tenancyMode")
    user_mode: Optional[str] = Field(alias="userMode")
    vsession_id: Optional[str] = Field(alias="VSessionId")
    is_saml_user: Optional[bool] = Field(alias="isSamlUser")
    is_rbac_vpn_user: Optional[bool] = Field(alias="isRbacVpnUser")
    vpns: List[Any]
    csrf_token: Optional[str] = Field(alias="CSRFToken")
    provider_domain: Optional[str] = Field(alias="providerDomain")
    tenant_id: Optional[str] = Field(alias="tenantId")
    provider_id: Optional[str] = Field(alias="providerId")
    view_mode: Optional[str] = Field(alias="viewMode")
    capabilities: List[str] = []
    user: Optional[str]
    description: Optional[str]
    locale: Optional[str]
    roles: List[str] = []
    external_user: Optional[bool] = Field(alias="externalUser")
    platform_version: VersionField = Field(alias="platformVersion")
    general_template: Optional[bool] = Field(alias="generalTemplate")
    disable_full_config_push: Optional[bool] = Field(alias="disableFullConfigPush")
    enable_server_events: Optional[bool] = Field(alias="enableServerEvents")
    cloudx: Optional[str]
    reverseproxy: Optional[str]
    vmanage_mode: Optional[str] = Field(alias="vmanageMode")


class AboutInfo(BaseModel):
    title: Optional[str]
    version: VersionField
    application_version: Optional[str] = Field(alias="applicationVersion")
    application_server: Optional[str] = Field(alias="applicationServer")
    copyright: Optional[str]
    time: Optional[datetime]
    time_zone: Optional[str] = Field(alias="timeZone")
    logo: Optional[str]


class ClientAPI(APIPrimitiveBase):
    def server(self) -> ServerInfo:
        return self.get("/client/server").dataobj(ServerInfo)

    def about(self) -> AboutInfo:
        return self.get("/client/about").dataobj(AboutInfo)
