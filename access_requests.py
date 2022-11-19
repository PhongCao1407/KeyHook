from sqlalchemy import Column, String, Identity, Integer, ForeignKey, Date, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base


class Access_request(Base):
    __tablename__ = "access_requests"
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=False, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.room_id'), primary_key=True, nullable=False)
    requested_date = Column('requested_date', Date, nullable=False, primary_key=True)

    room = relationship('Room', back_populates='employees_list')
    employee = relationship('Employee', back_populates='rooms_list')

    def __init__(self, room, employee, requested_date=None):
        self.room_id = room.room_id
        self.employee_id = employee.employee_id
        self.requested_date = requested_date
        self.room = room
        self.employee = employee
