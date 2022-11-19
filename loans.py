from sqlalchemy import Column, String, Identity, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from orm_base import Base

class Loan(Base):
    __tablename__ = "loans"
    loan_id = Column('loan_id', Integer, Identity(start=1, cycle=True),nullable=False, primary_key=True)
    start_time = Column('start_time', Integer, nullable=False)
    employee_id = Column('employee_id', Integer, ForeignKey("employees.employee_id"), nullable=False)
    key_id = Column('key_id', Integer, ForeignKey("keys.key_id"), nullable=False)

    children = relationship("Loan_losses", "Loan_returns")

    employee = relationship('Employee', back_populates='keys_list')
    key = relationship('Key', back_populates='employees_list')
    loan_losses = relationship("LoanLoss")
    loan_returns = relationship("LoanReturn")

    def __init__(self, employee, key, start_time):
        self.employee_id = employee.employee_id
        self.key_id = key.key_id
        self.start_time = start_time
        self.employee = employee
        self.key = key
        self.loan_losses = []
        self.loan_returns = []


class LoanLoss(Base):
    __tablename__ = "loan_losses"
    loan_id = Column('loan_id', Integer, ForeignKey("loans.loan_id"), Identity(start=1, cycle=True),nullable=False, primary_key=True)
    fine_amount = Column('fine_amount', Integer, nullable=False)
    reported_loss_date = Column('reported_loss_date', Date, nullable=False)

    loan: Loan = relationship("Loan", back_populates="loan_losses")

    def __init__(self, loan, fine_amount: Integer, reported_loss_date: Date):
        self.loan_id = loan.loan_id
        self.fine_amount = fine_amount
        self.reported_loss_date = reported_loss_date
        self.loan = loan


class LoanReturn(Base):
    __tablename__ = "loan_returns"
    loan_id = Column('loan_id', Integer, ForeignKey("loans.loan_id"), Identity(start=1, cycle=True),nullable=False, primary_key=True)
    return_date = Column('reported_loss_date', Date, nullable=False)

    loan: Loan = relationship("Loan", back_populates="loan_returns")
    def __init__(self, loan, return_date: Date):
        self.loan_id = loan.loan_id
        self.return_date = return_date
        self.loan = loan






