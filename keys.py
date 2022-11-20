from sqlalchemy import Column, Integer, Identity
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
from hooks import Hook
from loans import Loan


class Key(Base):
    __tablename__ = "keys"
    key_id = Column('key_id', Integer, Identity(start=1, cycle=True), nullable=False, primary_key=True)
    hook_id = Column(Integer, ForeignKey('hooks.hook_id'), primary_key=False, nullable=False)

    employees_list: [Loan] = relationship("Loan", back_populates="key")

    hook : Hook = relationship("Hook", back_populates="keys")

    def __init__(self, hook):
        self.hook_id = hook.hook_id
        self.hook = hook

    def add_employee(self, time, employee):
        for next_employee in self.employees_list:
            if next_employee == employee:
                return

        loan = Loan(employee, self, time)
        employee.keys_list.append(loan)
        self.employees_list.append(loan)



