from src.common.dtos import BasicApiModel
from typing import Optional

class RegistrateNewInstallationRequest(BasicApiModel):
    email: str
    installation_id: str


class ChallengeResponse(BasicApiModel):
    challenge_id: str


class IdentifyAppRequest(BasicApiModel):
    device_name: Optional[str]
    device_type: Optional[str]
    brand: Optional[str]
    manufacturer: Optional[str]
    model_name: Optional[str]
    os_name: Optional[str]
    os_version: Optional[str]
    platform_api_level: Optional[str]
    app_version: Optional[str]
    build_number: Optional[str]
    platform: Optional[str]

class IdentifyAppResponse(BasicApiModel):
    installation_id: str
