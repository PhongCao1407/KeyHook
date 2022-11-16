from sqlalchemy import Column, String, Integer, UniqueConstraint, Identity
#from sqlalchemy.orm import relationship
from orm_base import Base


class Hook(Base):
    __tablename__ = "hooks"
    hook_id = Column('hook_id', Integer, Identity(start=1, cycle=True), nullable=False, primary_key=True)

    def __init__(self):
        #There is nothing to initialize here right?
