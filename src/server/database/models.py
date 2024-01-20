import peewee
import settings

db: peewee.SqliteDatabase = peewee.SqliteDatabase(f'{settings.DATABASE_PATH}{settings.DATABASE_NAME}')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Cars (BaseModel):
    VIN: peewee.CharField = peewee.CharField(null=False, default='')


class Clients(BaseModel):
    name: peewee.CharField = peewee.CharField(null=False, default="")
    surname: peewee.CharField = peewee.CharField(null=False, default="")
    phone_number: peewee.IntegerField = peewee.IntegerField(null=False, default=0)
    email: peewee.CharField = peewee.CharField(null=False, default="")


class Services(BaseModel):
    name: peewee.CharField = peewee.CharField(null=False, default="")
    description: peewee.TextField = peewee.TextField(null=False, default="")
    count: peewee.IntegerField = peewee.IntegerField(null=False, default=0)


class Employees(BaseModel):
    name: peewee.CharField = peewee.CharField(null=False, default="")
    surname: peewee.CharField = peewee.CharField(null=False, default="")
    post: peewee.CharField = peewee.CharField(null=False, default="")
    salary: peewee.IntegerField = peewee.IntegerField(null=False, default=0)


class SpareParts(BaseModel):
    name: peewee.CharField = peewee.CharField(null=False, default="")
    description: peewee.TextField = peewee.TextField(null=False, default="")
    price: peewee.IntegerField = peewee.IntegerField(null=False, default=0)
    count: peewee.IntegerField = peewee.IntegerField(null=False, default=0)


class Orders(BaseModel):
    client_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Clients, related_name='Orders_clients_id', default=0)
    car_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Cars, related_name='Orders_car_id', default=0)
    reg_date: peewee.DateField = peewee.DateField(null=False, default="")
    status: peewee.CharField = peewee.CharField(null=False, default="")


class OrderingServices(BaseModel):
    order_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Orders, related_name='OS_order_id', default=0)
    service_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Services, related_name='OS_services_id', default=0)
    employee_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Employees, related_name='OS_employee_id', default=0)



class ServicesPerformed(BaseModel):
    order_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Orders, related_name='SP_order_id', default=0)
    service_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Services, related_name='SP_services_id', default=0)
    data: peewee.DateField = peewee.DateField(null=False, default="")
    price: peewee.IntegerField = peewee.IntegerField(null=False, default=0)


class CompletedParts(BaseModel):
    order_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Orders, related_name='CP_order_id', default=0)
    part_id: peewee.ForeignKeyField = peewee.ForeignKeyField(SpareParts, related_name='CP_part_id', default=0)
    count: peewee.IntegerField = peewee.IntegerField(null=False, default=0)
    price: peewee.IntegerField = peewee.IntegerField(null=False, default=0)


class OrderParts(BaseModel):
    order_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Orders, related_name='OP_order_id', default=0)
    part_id: peewee.ForeignKeyField = peewee.ForeignKeyField(SpareParts, related_name='OP_part_id', default=0)
    count: peewee.IntegerField = peewee.IntegerField(null=False, default=0)


db.create_tables([
    Cars,
    Clients,
    Services,
    Employees,
    SpareParts,
    Orders,
    OrderingServices,
    ServicesPerformed,
    CompletedParts,
    OrderParts
])