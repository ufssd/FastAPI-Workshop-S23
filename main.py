from fastapi import FastAPI 
from pydantic import BaseModel

from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

app = FastAPI()

class Device(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50, unique=True)
    ip = fields.CharField(50, unique=True)
    vendor = fields.CharField(50)
    os = fields.CharField(50)

Device_Pydantic = pydantic_model_creator(Device, name='Device')
DeviceIn_Pydantic = pydantic_model_creator(Device, name='DeviceIn', exclude_readonly=True)

@app.get('/devices')
async def get_devices():
    return await Device_Pydantic.from_queryset(Device.all())

@app.get('/devices/{device_id}')
async def get_device(device_id: int):
    return await Device_Pydantic.from_queryset_single(Device.get(id=device_id))

@app.post('/devices')
async def create_city(device: DeviceIn_Pydantic):
    city_obj = await Device.create(**device.dict(exclude_unset=True))
    return await DeviceIn_Pydantic.from_tortoise_orm(city_obj)

@app.delete('/devices/{device_id}')
async def delete_city(device_id: int):
    await Device.filter(id=device_id).delete()
    return {}

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)