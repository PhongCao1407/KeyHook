from sqlalchemy import Column, String, Identity, Integer
from sqlalchemy.orm import relationship
from orm_base import Base


class Building(Base):
    __tablename__ = "buildings"
    name = Column("name", String(50), nullable=False, primary_key=True)
    children = relationship("Room")

    def __init__(self, name: String):
        self.name = name

    def __str__(self):
        return "Building: {name}".format(name = self.name)
