from sqlalchemy import Column, String, Identity, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from orm_base import Base
from access_requests import Access_request

class Employees(Base):
    __tablename__ = "employees"
    employee_id = Column('employee_id', Integer, Identity(start=1, cycle=True),nullable=False, primary_key=True)
    name = Column('name', String, nullable=False)
    balance = Column('balance', Integer, nullable=False)

    access_request_list: [Access_request] = relationship("access_requests", back_populates="Employees", viewonly=False)


    def __init__(self, employee_id: Integer, balance: Integer, name: String):
        self.employee_id = employee_id
        self.balance = balance
        self.name = name
        self.access_request_list = []

