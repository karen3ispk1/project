from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import *


routers = (
    RouterManager(
        database_model=database_models.Cars,
        pydantic_model=pydantic_models.Cars,
        prefix='/cars',
        tags=['Cars']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Clients,
        pydantic_model=pydantic_models.Clients,
        prefix='/clients',
        tags=['Clients']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Services,
        pydantic_model=pydantic_models.Services,
        prefix='/services',
        tags=['Services']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Employees,
        pydantic_model=pydantic_models.Employees,
        prefix='/employees',
        tags=['Employees']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.SpareParts,
        pydantic_model=pydantic_models.SpareParts,
        prefix='/spare_Parts',
        tags=['SpareParts']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Orders,
        pydantic_model=pydantic_models.Orders,
        prefix='/orders',
        tags=['Orders']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.OrderingServices,
        pydantic_model=pydantic_models.OrderingServices,
        prefix='/ordering_services',
        tags=['OrderingServices']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.ServicesPerformed,
        pydantic_model=pydantic_models.ServicesPerformed,
        prefix='/services_performed',
        tags=['ServicesPerformed']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.CompletedParts,
        pydantic_model=pydantic_models.CompletedParts,
        prefix='/completed_parts',
        tags=['CompletedParts']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.OrderParts,
        pydantic_model=pydantic_models.OrderParts,
        prefix='/order_parts',
        tags=['OrderParts']
    ).fastapi_router,
)