from sqlalchemy import Column, String, Integer, UniqueConstraint, Identity
from sqlalchemy.orm import relationship
from orm_base import Base
from door_hook_opens import Door_Hook_Open


class Hook(Base):
    __tablename__ = "hooks"
    hook_id = Column('hook_id', Integer, Identity(start=1, cycle=True), nullable=False, primary_key=True)

    hook_door_list: [Door_Hook_Open] = relationship("door_hook_opens", back_populates="hooks", viewonly=False)

    def __init__(self):
        self.hook_door_list = []
