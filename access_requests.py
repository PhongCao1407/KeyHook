from sqlalchemy import Column, String, Identity, Integer, ForeignKey, Date, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

from employees import Employees
from rooms import Room

class Access_request(Base):
    __tablename__ = "access_requests"
    employee_id = Column('employee_id', Integer, nullable=False, primary_key=True)
    room_number = Column('room_number', Integer, nullable=False, primary_key=True)
    room_building_name = Column('room_building_name', String, nullable=False, primary_key=True)
    requested_date = Column('requested_date', Date, Identity(start=1, cycle=True), nullable=False, primary_key=True)

    __tableargs__ = (ForeignKeyConstraint([employee_id, room_number, room_building_name],
                                          [Employees.employee_id, Room.number, Room.building_name]), {})

    room = relationship('room', back_populate='rooms_list')
    employee = relationship('employee', back_populate='employees_list')

    def __init__(self, employee_id: Integer, room_number: Integer, room_building_name: String, requested_date: Date):
        self.room_number = room_number
        self.room_building_name = room_building_name
        self.employee_id = employee_id
        self.requested_date = requested_date