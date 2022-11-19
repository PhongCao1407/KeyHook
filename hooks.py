from sqlalchemy import Column, String, Integer, UniqueConstraint, Identity
from sqlalchemy.orm import relationship
from orm_base import Base
from door_hook_opens import Door_Hook_Open


class Hook(Base):
    __tablename__ = "hooks"
    hook_id = Column(Integer, Identity(start=1, cycle=True), nullable=False, primary_key=True)

    doors_list: [Door_Hook_Open] = relationship("Door_Hook_Open", back_populates="hook", viewonly=False)

    keys = relationship("Key")

    def __init__(self):
        self.doors_list = []
        self.keys = []

    def add_door(self, door):
        for next_door in self.doors_list:
            if next_door == door:
                return

        open_door = Door_Hook_Open(self, door)
        door.hooks_list.append(open_door)
        self.doors_list.append(open_door)
