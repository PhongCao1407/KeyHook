from sqlalchemy import Column, String, Identity, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
from doors import Door
from access_requests import Access_request
from buildings import Building

class Room(Base):
    __tablename__ = "rooms"
    number = Column(Integer, primary_key=True, nullable=False)
    building_name = Column(String(50), ForeignKey('buildings.name'), primary_key=True, nullable=False)

    door_list: [Door] = relationship("doors", back_populates="rooms", viewonly=False)
    room_access_request_list: [Access_request] = relationship("access_requests", back_populates="rooms", viewonly=False)

    def __init__(self, number: Integer, building_name: String):
        self.number = number
        self.room_list = []
        self.room_access_request_list = []

    def add_door(self, door):
        for next_door in self.door_list:
            if next_door == door:
                return
        self.room_list.append(door)

    def __str__(self):
        return "Building name: {building_name}, Room number: {number}".format(name = self.building_name,
                                                                              number = self.number)
