from pymongo import MongoClient
import urllib.parse


me = urllib.parse.quote_plus('LarryDCJ')
rd = urllib.parse.quote_plus('dismyside42')

client = MongoClient("mongodb+srv://%s:%s@cluster0.nhqsm.mongodb.net/metrics_tracker?retryWrites"
                     "=true&w=majority" % (me, rd), authSource='admin')

db = client.metrics_tracker
flights = db.flights


# get flight list from database
def get_flight_query():
    flight_list = []
    for flight in flights.find():
        flight = flight.values()
        flight = list(flight)[1:]
        flight_list.append(flight)
    return flight_list


# get flight columns from db
def get_flight_column_query():
    column_list = []
    for col in flights.find():
        col = list(col.keys())[1:]
        for column_header in col:
            column_list.append(column_header.title().replace('_', ' '))
        break
    return column_list


# find flight via user string
def find_flight(user_input):
    try:
        result = db.flights.find({'crew_position': f'{user_input}'})
    except:
        print('try again')
    return result

# #-----!!CRUD FUNCTIONS!!-----# #


# edit existing flight
def edit_flight():
    # get crew info
    # present crew info
    # allow to be changed
    # mongo update method
    pass


# add flight based on user input
def add_flight(value):
    flight_info = {
        '_id': value[0],
        'flight_number': value[0],
        'aircraft_type': value[1],
        'pilot_in_command': value[2],
        'scheduled_takeoff': value[3],
        'actual_takeoff': value[4],
        'scheduled_land': value[5],
        'actual_land': value[6]
    }
    flights.insert_one(flight_info)


# delete flight
def delete_flight(flight_number):
    flight_id = {'_id': flight_number}
    crew_members.delete_one(flight_id)
