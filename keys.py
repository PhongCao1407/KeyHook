from sqlalchemy import Column, Integer, Identity
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
from hooks import Hook




class Key(Base):
    __tablename__ = "keys"
    key_id = Column('key_id', Integer, Identity(start=1, cycle=True), nullable=False, primary_key=True)
    hook_id = Column(Integer, ForeignKey('hooks.hook_id'), primary_key=False, nullable=False)

    def __init__(self, hook):
        self.hook_id = hook.hook_id



