from sqlalchemy import Column, String, Identity, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from orm_base import Base

class Employees(Base):
    __tablename__ = "employees"
    employee_id = Column('employee_id', Integer, Identity(start=1, cycle=True),nullable=False, primary_key=True)
    name = Column('name', String, nullable=False)
    balance = Column('balance', Integer, nullable=False)




    def __init__(self, employee_id: Integer, balance: Integer, name: String):
        self.employee_id = employee_id
        self.balance = balance
        self.name = name

