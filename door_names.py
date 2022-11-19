from sqlalchemy import Column, String, Identity, Integer
from sqlalchemy.orm import relationship
from orm_base import Base

class Door_Name(Base):
    __tablename__ = "door_names"
    name = Column("name", String(10), nullable=False, primary_key=True)

    doors = relationship("Door")

    def __init__(self, name: String):
        self.name = name
        self.doors = []

    def __str__(self):
        return "Door Name: {name}".format(name = self.name)
