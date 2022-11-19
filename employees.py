from sqlalchemy import Column, String, Identity, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from access_requests import Access_request

class Employees(Base):
    __tablename__ = "employees"
    employee_id = Column('employee_id', Integer, Identity(start=1, cycle=True),nullable=False, primary_key=True)
    name = Column('name', String, nullable=False)
    balance = Column('balance', Integer, nullable=False)

    rooms_list: [Access_request] = relationship("access_requests", back_populates="employee", viewonly=False)


    def __init__(self, employee_id: Integer, balance: Integer, name: String):
        self.employee_id = employee_id
        self.balance = balance
        self.name = name
        self.access_request_list = []

    def add_room(self, room, date):
        for next_room in self.rooms_list:
            if next_room == room:
                return

        access_request = Access_request(self.employee_id, room.number, room.building_name, date)
        room.employees_list.append(access_request)
        self.rooms_list.append(access_request)

