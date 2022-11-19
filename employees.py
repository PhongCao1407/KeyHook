from sqlalchemy import Column, String, Identity, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from access_requests import Access_request
from loans import Loan

class Employee(Base):
    __tablename__ = "employees"
    employee_id = Column('employee_id', Integer, Identity(start=1, cycle=True),nullable=False, primary_key=True)
    name = Column('name', String, nullable=False)
    balance = Column('balance', Integer, nullable=False)

    rooms_list: [Access_request] = relationship("access_requests", back_populates="employee", viewonly=False)
    keys_list: [Loan] = relationship("loans", back_populates="employee", viewonly=False)

    def __init__(self, balance: Integer, name: String):
        self.balance = balance
        self.name = name
        self.rooms_list = []
        self.keys_list = []

    def add_room(self, room, date):
        for next_room in self.rooms_list:
            if next_room == room:
                return

        access_request = Access_request(room, self, date)
        room.employees_list.append(access_request)
        self.rooms_list.append(access_request)

    def add_key(self, time, key):
        for next_key in self.key_list:
            if next_key == key:
                return

        loan = Loan(self, key, time)
        key.employees_list.append(loan)
        self.keys_list.append(loan)


