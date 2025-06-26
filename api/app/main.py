import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_keycloak_middleware import AuthorizationMethod, KeycloakConfiguration, setup

from config import settings
from routes import api_router

app = FastAPI(
    title=settings.APP_NAME,
)

keycloak_config = KeycloakConfiguration(
    url=settings.KEYCLOAK_URL,
    realm=settings.KEYCLOAK_REALM,
    client_id=settings.KEYCLOAK_CLIENT_ID,
    client_secret=settings.KEYCLOAK_CLIENT_SECRET,
    authorization_method=AuthorizationMethod.CLAIM,
    authorization_claim="realm_access"
)

async def scope_mapper(claim_auth: dict) -> list[str]:
    permissions = []
    try:
        permissions = claim_auth["roles"]
    except KeyError:
        logging.warning("Unknown roles")
    return permissions

setup.setup_keycloak_middleware(
    app,
    keycloak_configuration=keycloak_config,
    scope_mapper=scope_mapper,
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.APIVersion)
