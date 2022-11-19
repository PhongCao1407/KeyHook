from sqlalchemy import Column, String, Identity, Integer, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from orm_base import Base
from rooms import Room
from door_names import Door_Name
from door_hook_opens import Door_Hook_Open

class Door(Base):
    __tablename__ = "doors"
    door_id = Column('door_id', Integer, Identity(start=1, cycle=True),nullable=False, primary_key=True)

    door_name = Column(String(10), ForeignKey('door_names.name'), nullable=False)

    room_id = Column(Integer, ForeignKey('rooms.room_id'), nullable=False)

    hooks_list: [Door_Hook_Open] = relationship("Door_Hook_Open", back_populates="door", viewonly=False)

    def __init__(self, door_name, room):
        self.door_name = door_name.name
        self.room_id = room.room_id
        self.hooks_list = []

    def add_hook(self, hook):
        for next_hook in self.hooks_list:
            if next_hook == hook:
                return

        open_door = Door_Hook_Open(hook, self)
        hook.doors_list.append(open_door)
        self.hooks_list.append(open_door)

    # def __str__(self):
    #     return "Building name: {building_name}, Room number: {number}, Doors: {doors}".format(
    #         name = self.building_name, number = self.room_number,doors = self.door_name_list)
