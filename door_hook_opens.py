from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from orm_base import Base
from sqlalchemy.orm import relationship

class Door_Hook_Open(Base):
    __tablename__ = "door_hook_opens"
    hook_id = Column(Integer, ForeignKey('hooks.hook_id'), primary_key=True, nullable=False)
    door_id = Column(Integer, ForeignKey('doors.door_id'), primary_key=True, nullable=False)

    hook = relationship('Hook', back_populates='doors_list')
    door = relationship('Door', back_populates='hooks_list')

    def __init__(self, hook, door):
        self.hook_id = hook.hook_id
        self.door_id = door.door_id
        self.hook = hook
        self.door = door



