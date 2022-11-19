from sqlalchemy import Column, String, Identity, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
from access_requests import Access_request
from buildings import Building

class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, Identity(start=1, cycle=True), nullable=False, primary_key=True)
    number = Column(Integer, nullable=False)
    building_name = Column(String(50), ForeignKey('buildings.name'), nullable=False)

    employees_list: [Access_request] = relationship("access_requests", back_populates="room", viewonly=False)

    building: Building = relationship("Building", back_populates="rooms")

    doors = relationship("Door")

    def __init__(self, number: Integer, building):
        self.number = number
        self.building_name = building.name
        self.employees_list = []
        self.building = building
        self.doors = []

    def add_employee(self, employee, date):
        for next_employee in self.employees_list:
            if next_employee == employee:
                return

        access_request = Access_request(self, employee, date)
        employee.rooms_list.append(access_request)
        self.employees_list.append(access_request)

    def __str__(self):
        return "Building name: {building_name}, Room number: {number}".format(name = self.building_name,
                                                                              number = self.number)
