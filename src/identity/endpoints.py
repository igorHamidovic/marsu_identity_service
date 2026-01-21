import uuid
from fastapi import APIRouter, status, Header

from src.identity.dtos import (RegistrateNewInstallationRequest, ChallengeResponse, IdentifyAppResponse,
                               IdentifyAppRequest)

router = APIRouter()

@router.post(
    "/identity/challenge",
    tags=["identity"],
    status_code=status.HTTP_201_CREATED,
    response_model=ChallengeResponse,
)
async def post_challenge(
        request_body: RegistrateNewInstallationRequest,
):
    return ChallengeResponse(
        challenge_id=str(uuid.uuid4()),
    )


@router.get(
    "/identity/challenge",
    tags=["identity"],
    response_model=ChallengeResponse,
    status_code=status.HTTP_200_OK,
)
async def get_challenge(
        authorization: str = Header(...),
):
    return ChallengeResponse(challenge_id=str(uuid.uuid4()))


@router.post(
    "/identity/identify-app",
    tags=["identity"],
    status_code=status.HTTP_201_CREATED,
    response_model=IdentifyAppResponse,
)
async def post_identify_app(
        request_body: IdentifyAppRequest,
):
    return IdentifyAppResponse(
        installation_id=str(uuid.uuid4()),
    )
