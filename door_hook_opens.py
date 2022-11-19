from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from orm_base import Base
from sqlalchemy.orm import relationship


class Door_Hook_Open(Base):
    __tablename__ = "door_hook_opens"
    hooks_hook_id = Column(Integer, ForeignKey('hooks.hook_id'), primary_key=True, nullable=False)
    doors_door_id = Column(Integer, ForeignKey('doors.door_id'), primary_key=False, nullable=False)


    hook = relationship('Hook', back_populate='doors_list')
    door = relationship('Door', back_populate='hooks_list')

    def __init__(self, hook, door):
        self.hook_id = hook.hook_id
        self.doors_door_id = door.door_id



