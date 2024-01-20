from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Cars(BaseModelModify):
    VIN: str


class Clients(BaseModelModify):
    name: str
    surname: str
    phone_number: int
    email: str


class Services(BaseModelModify):
    name: str
    description: str
    count: int


class Employees(BaseModelModify):
    name: str
    price: float


class SpareParts(BaseModelModify):
    name: str
    surname: str
    post: str
    salary: int


class Orders(BaseModelModify):
    client_id: int
    car_id: int
    reg_date: str
    status: str


class OrderingServices(BaseModelModify):
    order_id: int
    service_id: int
    employee_id: int


class ServicesPerformed(BaseModelModify):
    order_id: int
    service_id: int
    data: date
    price: int


class CompletedParts(BaseModelModify):
    order_id: int
    part_id: int
    count: int
    price: int


class OrderParts(BaseModelModify):
    order_id: int
    part_id: int
    count: int


class LoginData(BaseModel):
    login: str
    password: str