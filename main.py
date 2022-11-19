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
from keys import Key
from hooks import Hook
from buildings import Building

if __name__ == '__main__':
    logging.basicConfig()
    # use the logging factory to create our first logger.
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    # use the logging factory to create our second logger.
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

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
        sess.begin()

        buildings = sess.query(Building)
        for building in buildings:
            print(building.name)
        #populate tables

        #Menu
        # user_in = 1
        # while user_in in set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
            # print("1. Create new key")
            # print("2. Request access to a given room by given Employee")
            # print("3. Issuing a key to an employee")
            # print("4. Losing a key")
            # print("5. Rooms an employee can enter")
            # print("6. Delete a key")
            # print("7. Delete an employee")
            # print("8. Add new door")
            # print("9. Update an access request for new employee")
            # print("10. Show Employees who can get into a room")

            # user_in = int(input())
            #
            # if user_in == 1:
            #     pass
            # elif user_in == 2:
            #     pass
            # elif user_in == 3:
            #     pass
            # elif user_in == 4:
            #     pass
            # elif user_in == 5:
            #     pass
            # elif user_in == 6:
            #     pass
            # elif user_in == 7:
            #     pass
            # elif user_in == 8:
            #     pass
            # elif user_in == 9:
            #     pass
            # elif user_in == 10:
            #     pass



    print("Exiting normally.")

