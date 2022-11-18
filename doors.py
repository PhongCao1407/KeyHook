from sqlalchemy import Column, String, Identity, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
from door_names import Door_Name
from door_hook_opens import Door_Hook_Open

class Door(Base):
    __tablename__ = "doors"
    door_id = Column('door_id', Integer, Identity(start=1, cycle=True),nullable=False, primary_key=True)

    door_name = Column(String(10), ForeignKey('door_names.name'), nullable=False)
    building_name = Column(String(50), ForeignKey('buildings.name'), nullable=False)
    room_number = Column(Integer, ForeignKey('rooms.number'), nullable=False)
    door_name_list: [Door_Name] = relationship("door_names", back_populates="doors", viewonly=False)
    door_hook_list: [Door_Hook_Open] = relationship("door_hook_opens", back_populates="doors", viewonly=False)

    def __init__(self, door_id: Integer, door_name: String, building_name: String, room_number: Integer):
        self.door_id = door_id
        self.door_name = door_name
        self.building_name = building_name
        self.room_number = room_number
        self.door_name_list = []
        self.door_hook_list = []

    def add_door(self, door_name):
        for next_door_name in self.door_name_list:
            if next_door_name == door_name:
                return
        self.door_name_list.append(door_name)

    def __str__(self):
        return "Building name: {building_name}, Room number: {number}, Doors: {doors}".format(
            name = self.building_name, number = self.room_number,doors = self.door_name_list)
