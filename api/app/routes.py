from fastapi import APIRouter, Depends
from fastapi_keycloak_middleware import CheckPermissions
from models import Report

api_router = APIRouter()


# CheckPermissions проверяет наличие роли "prothetic_user" и возвращает 403, если не найдено
# Валидация токена работает из коробки :)
@api_router.get(
    "/reports",
    response_model=list[Report],
    dependencies=[Depends(CheckPermissions(["prothetic_user"]))],
)
def get_reports() -> list[Report]:
    reports = [Report(data="Demo data for report-api")]
    return reports
