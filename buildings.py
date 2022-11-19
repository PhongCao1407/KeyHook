from sqlalchemy import Column, String, Identity, Integer
from sqlalchemy.orm import relationship
from orm_base import Base
from rooms import Room

class Building(Base):
    __tablename__ = "buildings"
    name = Column("name", String(50), nullable=False, primary_key=True)
    children = relationship("Room")
    room_list: [Room] = relationship("rooms", back_populates="buildings", viewonly=False)

    def __init__(self, name: String):
        self.name = name
        self.room_list = []

    def add_room(self, room: Integer):
        for next_room in self.room_list:
            if next_room == room:
                print("Building already has room number")
                return
        self.room_list.append(room)

    def __str__(self):
        return "Building: {name}".format(name = self.name)
