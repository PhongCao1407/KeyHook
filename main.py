"""This "application" is a demonstration using SQLAlchemy to create a small number of tables and populate
them.  Not evey possible use case for SQLAlchemy is explored in this demonstration, only those which are
required for this particular demonstration.

Technical Note: Be sure to have psycopg2 or whichever package you need to support whichever
relational dialect that you are using installed.  No imports call attention to the database
connectivity library, that is referenced when you run your entine."""

# Think of Session and engine like global variables.  A little ghetto, but the only
# other alternative would have been a singleton design pattern.

# the db_connection.py code sets up some connection objects for us, almost like Java class variables
# that get loaded up at run time.  This statement builds the Session class and the engine object
# that we will use for interacting with the database.
from db_connection import Session, engine
# orm_base defines the Base class on which we build all of our Python classes and in so doing,
# stipulates that the schema that we're using is 'demo'.  Once that's established, any class
# that uses Base as its supertype will show up in the postgres.demo schema.
from orm_base import metadata
import logging

# custom imports
from buildings import Building
from rooms import Room
from employees import Employee
from access_requests import Access_request
from door_hook_opens import Door_Hook_Open
from door_names import Door_Name
from doors import Door
from hooks import Hook
from keys import Key
from loans import *

from datetime import datetime
from random import randint

if __name__ == '__main__':
    # IMPORTANT: May need to uncomment
    # logging.basicConfig()
    # # use the logging factory to create our first logger.
    # logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # # use the logging factory to create our second logger.
    # logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    # metadata.drop_all(bind=engine)  # start with a clean slate while in development

    # Create whatever tables are called for by our "Entity" classes.  The simple fact that
    # your classes that are subtypes of Base have been loaded by Python has populated
    # the metadata object with their definition.  So now we tell SQLAlchemy to create
    # those tables for us.
    # metadata.create_all(bind=engine)

    # Do our database work within a context.  This makes sure that the session gets closed
    # at the end of the with, much like what it would be like if you used a with to open a file.
    # This way, we do not have memory leaks.


    with Session() as sess:
        print ("Inside the session, woo hoo.")

        # print('Building')
        #
        # buildings = sess.query(Building)
        # for building in buildings:
        #     print(building.name)
        #
        # print('Room')
        #
        # rooms = sess.query(Room)
        # for room in rooms:
        #     print(room.building_name)
        #
        # print('Employee')
        #
        # employees = sess.query(Employee)
        # for employee in employees:
        #     print(employee.employee_id)
        #
        # print('Access Request')
        #
        # access_requests = sess.query(Access_request)
        # for access_request in access_requests:
        #     print(access_request.room_id)
        #
        # print('Door')
        #
        # doors = sess.query(Door)
        # for door in doors:
        #     print(door.door_id)
        #
        # print('Door Names')
        # door_names = sess.query(Door_Name)
        # for door_name in door_names:
        #     print(door_name.name)
        #
        # print('Door Hook Open')
        # door_hook_opens = sess.query(Door_Hook_Open)
        # for door_hook_open in door_hook_opens:
        #     print(door_hook_open.hook_id)
        #
        # print('Hook')
        # hooks = sess.query(Hook)
        # for hook in hooks:
        #     print(hook.hook_id)
        #
        # print('Key')
        # keys = sess.query(Key)
        # for key in keys:
        #     print(key.key_id)
        #
        # print('Loan')
        # loans = sess.query(Loan)
        # for loan in loans:
        #     print(loan.start_time)
        #
        # print('Loan losses')
        # loan_losses = sess.query(LoanLoss)
        # for loan_loss in loan_losses:
        #     print(loan_loss.reported_loss_date)
        #
        # print('Loan return')
        # loan_returns = sess.query(LoanReturn)
        # for loan_return in loan_returns:
        #     print(loan_return.return_date)

        #Menu
        user_in = 1
        while user_in in set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
            print("1. Create new key")
            print("2. Request access to a given room by given Employee")
            print("3. Issuing a key to an employee")
            print("4. Losing a key")
            print("5. Rooms an employee can enter")
            print("6. Delete a key")
            print("7. Delete an employee")
            print("8. Add new door")
            print("9. Update an access request for new employee")
            print("10. Show Employees who can get into a room")

            user_in = int(input())

            if user_in == 1:
                # List out the hook
                print('Please choose a hook to make the key from')
                hooks = sess.query(Hook)
                for hook in hooks:
                    print(hook.hook_id)

                # Get hook input
                hook_id_input = int(input())
                hook_input = None

                for hook in hooks:
                    # print(type(hook_id_input) , type(hook.hook_id))
                    if hook.hook_id == hook_id_input:
                        hook_input = hook

                if hook_input is None:
                    print("Please choose a valid hook")
                else:
                    newKey = Key(hook_input)
                    sess.add(newKey)
                    print('You have added a key')
                    sess.commit()
            elif user_in == 2:
                print('Please enter your employee id')
                emp_id_input = int(input())
                emp = None

                employees = sess.query(Employee)

                for employee in employees:
                    if employee.employee_id == emp_id_input:
                        emp = employee

                if emp is None:
                    print('You are not an employee')
                else:

                    print('Here are the rooms')
                    rooms = sess.query(Room)
                    for room in rooms:
                        print(room.building_name, room.number, room.room_id)

                    print('Please choose the room that you want access to by providing the room ID')
                    room_input = int(input())
                    requested_room = None

                    print('Please enter the date of when you want to acccess the room')
                    date_input = str(input())

                    for room in rooms:
                        if room.room_id == room_input:
                            requested_room = room

                    if requested_room is None:
                        print("This is not a valid room number")
                    else:
                        newRequest = Access_request(requested_room, emp, date_input)
                        sess.add(newRequest)
                        sess.commit()
                        print('Request created')


            elif user_in == 3:
                print('Please enter your employee id')
                emp_id_input = int(input())
                emp = None

                employees = sess.query(Employee)

                for employee in employees:
                    if employee.employee_id == emp_id_input:
                        emp = employee

                if emp is None:
                    print('You are not an employee')
                else:
                    print('Please choose a key ID')

                    keys = sess.query(Key)
                    for key in keys:
                        print(key.key_id)

                    key_id_input = int(input())
                    key_requested = None

                    for key in keys:
                        if key_id_input == key.key_id:
                            key_requested = key

                    if key_requested is None:
                        print('That is not a valid key')
                    else:
                        date = datetime.today().strftime('%Y-%m-%d')
                        loan = Loan(emp, key_requested, date)
                        sess.add(loan)
                        sess.commit()
                        print('Here is your key')

            elif user_in == 4:
                print('What is your key loan ID?')
                loans = sess.query(Loan)
                for loan in loans:
                    print(loan.loan_id)

                loan_id_input = int(input())
                lost_loan = None

                for loan in loans:
                    if loan_id_input == loan.loan_id:
                        lost_loan = loan

                # Make sure the loan is not already return
                loan_returns = sess.query(LoanReturn)
                for loan_return in loan_returns:
                    if loan_id_input == loan_return.loan_id:
                        print('This key loan has already been returned')
                        continue

                if lost_loan is None:
                    print('That is not a valid loan ID')
                else:
                    charge = randint(1, 1000)
                    date = datetime.today().strftime('%Y-%m-%d')
                    lost = LoanLoss(lost_loan, charge, date)
                    sess.add(lost)
                    sess.commit()
                    print('Thank you for reporting. You are charged $' + str(charge) + '.')

            elif user_in == 5:
                print('Please enter your employee id')
                emp_id_input = int(input())
                emp = None

                employees = sess.query(Employee)

                for employee in employees:
                    if employee.employee_id == emp_id_input:
                        emp = employee

                if emp is None:
                    print('You are not an employee')
                else:
                    employee_loans = []
                    loans = sess.query(Loan)
                    for loan in loans:
                        if loan.employee_id == emp.employee_id:
                            employee_loans.append(loan)

                    if not employee_loans: # If employee_loan is empty
                        print('You dont have any keys loan')
                        continue

                    keys = sess.query(Key)
                    employee_keys = []
                    for employee_loan in employee_loans:
                        for key in keys:
                            if employee_loan.key_id == key.key_id:
                                employee_keys.append(key)

                    if not employee_keys:
                        print('You do not have any keys')
                        continue

                    hooks = sess.query(Hook)
                    employee_hooks = []
                    for employee_key in employee_keys:
                        for hook in hooks:
                            if employee_key.hook_id == hook.hook_id:
                                employee_hooks.append(hook)

                    door_hook_opens = sess.query(Door_Hook_Open)
                    employee_door_hook_opens = []
                    for employee_hook in employee_hooks:
                        for door_hook_open in door_hook_opens:
                            if employee_hook.hook_id == door_hook_open.hook_id:
                                employee_door_hook_opens.append(door_hook_open)

                    doors = sess.query(Door)
                    employee_doors = []
                    for employee_door_hook_open in employee_door_hook_opens:
                        for door in doors:
                            if employee_door_hook_open.door_id == door.door_id:
                                employee_doors.append(door)

                    rooms = sess.query(Room)
                    employee_rooms = []
                    for employee_door in employee_doors:
                        for room in rooms:
                            if employee_door.room_id == room.room_id:
                                employee_rooms.append(room)

                    print('Here are the rooms that you can open')
                    for employee_room in employee_rooms:
                        print('Room number:', employee_room.number, '; Building:', employee_room.building_name, '; Room ID:', employee_room.room_id)



            elif user_in == 6:
                print('Please enter the key ID of the key that you want to delete')
                keys = sess.query(Key)
                for key in keys:
                    print(key.key_id)
                delete_key_id = int(input())
                delete_key = None

                keys = sess.query(Key)
                for key in keys:
                    if key.key_id == delete_key_id:
                        delete_key = key

                if delete_key is None:
                    print('That is not a valid key')
                    continue

                delete_loans = []
                loans = sess.query(Loan)
                for loan in loans:
                    if loan.key_id == delete_key_id:
                        delete_loans.append(loan)

                delete_losses_or_returns = []
                losses = sess.query(LoanLoss)
                for delete_loan in delete_loans:
                    for loss in losses:
                        if delete_loan.loan_id == loss.loan_id:
                            delete_losses_or_returns.append(loss)

                returns = sess.query(LoanReturn)
                for delete_loan in delete_loans:
                    for ret in returns:
                        if ret.loan_id == delete_loan.loan_id:
                            delete_losses_or_returns.append(ret)

                for loss_or_return in delete_losses_or_returns:
                    sess.delete(loss_or_return)

                for delete_loan in delete_loans:
                    sess.delete(delete_loan)

                sess.delete(delete_key)

                sess.commit()

                print('Delete successful')

            elif user_in == 7:
                print('Please enter the employee ID of the employee that you want to delete')
                employees = sess.query(Employee)
                for employee in employees:
                    print(employee.employee_id)
                delete_employee_id = int(input())
                delete_employee = None

                for employee in employees:
                    if employee.employee_id == delete_employee_id:
                        delete_employee = employee

                if delete_employee is None:
                    print('That is not a valid employee')
                    continue

                delete_loans = []
                loans = sess.query(Loan)
                for loan in loans:
                    if loan.key_id == delete_employee_id:
                        delete_loans.append(loan)

                delete_losses_or_returns = []
                losses = sess.query(LoanLoss)
                for delete_loan in delete_loans:
                    for loss in losses:
                        if delete_loan.loan_id == loss.loan_id:
                            delete_losses_or_returns.append(loss)

                returns = sess.query(LoanReturn)
                for delete_loan in delete_loans:
                    for ret in returns:
                        if ret.loan_id == delete_loan.loan_id:
                            delete_losses_or_returns.append(ret)

                access_requests = sess.query(Access_request)
                delete_access_requests = []
                for access_request in access_requests:
                    if access_request.employee_id == delete_employee_id:
                        delete_access_requests.append(access_request)

                for delete_access_request in delete_access_requests:
                    sess.delete(delete_access_request)

                for loss_or_return in delete_losses_or_returns:
                    sess.delete(loss_or_return)

                for delete_loan in delete_loans:
                    sess.delete(delete_loan)

                sess.delete(delete_employee)

                sess.commit()

                print('Delete successful')
            elif user_in == 8:
                print('Please choose one of the following room to add a door to')
                rooms = sess.query(Room)
                for room in rooms:
                    print(room.room_id)

                room_id_input = int(input())
                add_room = None

                for room in rooms:
                    if room.room_id == room_id_input:
                        add_room = room

                print('Which type of door do you want to add')
                door_names = sess.query(Door_Name)
                for door_name in door_names:
                    print(door_name.name)

                door_name_input = str(input())
                add_door_name = None

                for door_name in door_names:
                    if door_name.name == door_name_input:
                        add_door_name = door_name

                print('Please choose a hook to make this door from')
                hooks = sess.query(Hook)
                for hook in hooks:
                    print(hook.hook_id)

                hook_id_input = int(input())
                add_hook = None

                for hook in hooks:
                    if hook.hook_id == hook_id_input:
                        add_hook = hook

                newDoor = Door(add_door_name, add_room)
                sess.add(newDoor)
                newDoorHookOpens = Door_Hook_Open(add_hook, newDoor)
                sess.add(newDoorHookOpens)
                sess.commit()

                print('Door added successfully')

            elif user_in == 9:
                print('Please enter the employee_id of the access requests that you want to update')
                access_requests = sess.query(Access_request)
                for access_request in access_requests:
                    print(access_request.employee_id)

                access_request_id_input = int(input())
                update_access_request_emp = None

                for access_request in access_requests:
                    if access_request.employee_id == access_request_id_input:
                        update_access_request_emp = access_request

                if update_access_request_emp is None:
                    print('That is not a valid ID')
                    continue

                print('Please enter the new employee_id')
                for access_request in access_requests:
                    if access_request.employee_id != access_request_id_input:
                        print(access_request.employee_id)

                new_access_request_id_input = int(input())
                new_access_request_emp = None

                for access_request in access_requests:
                    if access_request.employee_id == new_access_request_id_input:
                        new_access_request_emp = access_request

                if new_access_request_emp is None:
                    print('That is not a valid ID')
                    continue

                update_access_request_emp.employee_id = new_access_request_emp.employee_id

                sess.commit()

                print('Update successful')


            elif user_in == 10:
                print('Please enter the room ID that you want to know about')
                rooms = sess.query(Room)
                for room in rooms:
                    print(room.room_id)

                room_id_input = int(input())
                enter_room = None

                for room in rooms:
                    if room.room_id == room_id_input:
                        enter_room = room

                if enter_room is None:
                    print('That is not a valid room')
                    continue

                enter_doors = []
                doors = sess.query(Door)
                for door in doors:
                    if door.room_id == enter_room.room_id:
                        enter_doors.append(door)

                enter_door_hook_opens = []
                door_hook_opens = sess.query(Door_Hook_Open)
                for enter_door in enter_doors:
                    for door_hook_open in door_hook_opens:
                        if door_hook_open.door_id == enter_door.door_id:
                            enter_door_hook_opens.append(door_hook_open)

                enter_hooks = []
                hooks = sess.query(Hook)
                for enter_door_hook_open in enter_door_hook_opens:
                    for hook in hooks:
                        if hook.hook_id == enter_door_hook_open.hook_id:
                            enter_hooks.append(hook)

                enter_keys = []
                keys = sess.query(Key)
                for enter_hook in enter_hooks:
                    for key in keys:
                        if key.hook_id == enter_hook.hook_id:
                            enter_keys.append(key)

                enter_loans = []
                loans = sess.query(Loan)
                for enter_key in enter_keys:
                    for loan in loans:
                        if loan.key_id == enter_key.key_id:
                            enter_loans.append(loan)

                print('The employees are:')
                employees = sess.query(Employee)
                for enter_loan in enter_loans:
                    for employee in employees:
                        if employee.employee_id == enter_loan.employee_id:
                            print('Employee name:', employee.name, '; Employee ID:', employee.employee_id)


    print("Exiting normally.")



