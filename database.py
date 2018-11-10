from peewee import *


db = SqliteDatabase('bikes.db')


class BaseModel(Model):
    class Meta:
        database = db


class Bike(BaseModel):
    onzo_bike_id = CharField()
    battery = IntegerField(null=True)
    charge_voltage = IntegerField(null=True)
    create_time = DateTimeField(null=True)
    icc_id = TextField(null=True)
    lock_id = IntegerField(null=True)
    is_lock = IntegerField(null=True)
    lock_type = IntegerField(null=True)
    l_status = IntegerField(null=True)
    mac = CharField(null=True)
    model_num = TextField(null=True)
    p_signal = IntegerField(null=True)
    p_status = IntegerField(null=True)
    speed = IntegerField(null=True)
    unlock_times = IntegerField(null=True)
    update_time = DateTimeField(null=True)
    voltage = IntegerField(null=True)


class Location(BaseModel):
    bike = ForeignKeyField(Bike, backref='locations')
    location_mode = IntegerField()
    latitude = DoubleField()
    longitude = DoubleField()
    direction = IntegerField()
    height = IntegerField()
    update = DateTimeField()


db.connect()
db.create_tables([Bike, Location])
