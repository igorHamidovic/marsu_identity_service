from src.common.dtos import BasicApiModel
from typing import Optional

class RegistrateNewInstallationRequest(BasicApiModel):
    email: str
    installation_id: str


class ChallengeResponse(BasicApiModel):
    challenge_id: str


class IdentifyAppRequest(BasicApiModel):
    device_name: Optional[str] = None
    device_type: Optional[str] = None
    brand: Optional[str] = None
    manufacturer: Optional[str] = None
    model_name: Optional[str] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None
    platform_api_level: Optional[str] = None
    app_version: Optional[str] = None
    build_number: Optional[str] = None
    platform: Optional[str] = None

class IdentifyAppResponse(BasicApiModel):
    installation_id: str
