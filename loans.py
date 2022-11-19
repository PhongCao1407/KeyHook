from sqlalchemy import Column, String, Identity, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from orm_base import Base

class Loans(Base):
    __tablename__ = "loans"
    loan_id = Column('loan_id', Integer, Identity(start=1, cycle=True),nullable=False, primary_key=True)
    start_time = Column('start_time', Integer, nullable=False)
    employee_id = Column('employee_id', Integer, ForeignKey("employees.employee_id"), nullable=False)
    key_id = Column('key_id', Integer, ForeignKey("keys.key_id"), nullable=False)

    children = relationship("Loan_losses")

    employee = relationship('employees', back_populate='keys_list')
    key = relationship('keys', back_populate='employees_list')

    def __init__(self, loan_id: Integer, start_time: Integer, employee_id: Integer, key_id: Integer):
        self.start_time = start_time
        self.employee_id = employee_id
        self.key_id = key_id


class Loan_losses(Base):
    __tablename__ = "loan_losses"
    loan_id = Column('loan_id', Integer, ForeignKey("loans.loan_id"), Identity(start=1, cycle=True),nullable=False, primary_key=True)
    fine_amount = Column('fine_amount', Integer, nullable=False)
    reported_loss_date = Column('reported_loss_date', Date, nullable=False)

    def __init__(self, loan_id: Integer, fine_amount: Integer, reported_loss_date: Date):
        self.loan_id = loan_id
        self.fine_amount = fine_amount
        self.reported_loss_date = reported_loss_date


class Loan_returns(Base):
    __tablename__ = "loan_returns"
    loan_id = Column('loan_id', Integer, ForeignKey("loans.loan_id"), Identity(start=1, cycle=True),nullable=False, primary_key=True)
    return_date = Column('reported_loss_date', Date, nullable=False)

    def __init__(self, loan_id: Integer, return_date: Date):
        self.loan_id = loan_id
        self.return_date = return_date






