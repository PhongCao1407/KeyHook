from sqlalchemy import Column, String, Identity, Integer
from sqlalchemy.orm import relationship
from orm_base import Base
from rooms import Room

class Door_Name(Base):
    __tablename__ = "door_names"
    name = Column("name", String(10), nullable=False, primary_key=True)

    def __init__(self, name: String):
        self.name = name

    def __str__(self):
        return "Door Name: {name}".format(name = self.name)
