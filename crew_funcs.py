import random
from datetime import timedelta, datetime
from random import randrange

import names

from upconn import *

db = client.metrics_tracker
crews = db.crews


def gen_random_crew():
    gender = random.choice(['male', 'female'])
    first_name = names.get_first_name(gender=gender)
    middle_name = names.get_first_name(gender=gender)
    last_name = names.get_last_name()

    try:
        employee_id = random.randint(13370001, 13380000)
    except IndexError:
        employee_id = random.randint(13370001, 13380000)

    crew_position = random.choices(['SO', 'P', 'ISO', 'IP', 'ESO', 'EP'], weights=(35, 30, 15, 10, 5, 5), k=1)[0]

    if gender == 'male':
        suffix = random.choices(['Jr.', 'Sr.', 'III', 'IV', None], weights=(10, 10, 5, 2, 73), k=1)[0]
    else:
        suffix = ''

    return first_name, middle_name, last_name, suffix, employee_id, crew_position

def get_crew_query(*query):
    crew_list = [list(crew.values()) for crew in crews.find(*query)]
    return crew_list

def get_crew_column_query(*query):
    column_list = [key.title().replace('_', ' ') for key in crews.find_one(*query)]
    return column_list

def find_crew(employee_ids):
    crew_on_flight = [crews.find({'employee_id': employee_id})[0].values() for employee_id in employee_ids]
    return crew_on_flight

def find__single_crew(employee_ids):
    crew_on_flight = [crews.find_one({'employee_id': employee_id})[0].values() for employee_id in employee_ids]
    return crew_on_flight

def edit_crew_member():
    # get crew info
    # present crew info
    # allow to be changed
    # mongo update method
    pass

def add_crew_members(value):

    def gen_date():
        def random_date(start, end):
            delta = end - start
            int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
            random_second = randrange(int_delta)
            return start + timedelta(seconds=random_second)

        d1 = datetime.strptime('1/1/2020', '%m/%d/%Y')
        d2 = datetime.strptime('12/1/2020', '%m/%d/%Y')
        return random_date(d1, d2)

    evaluation = gen_date()
    laupro = gen_date()
    takeoff = gen_date()
    sortie = gen_date()
    instrument_approach = gen_date()
    noseir = gen_date()
    mts = gen_date()
    landing = gen_date()

    currencies = {'Evaluation': {'Last': evaluation, 'Due': evaluation+timedelta(510)},
                  'Launch Procedures': {'Last': laupro, 'Due': laupro+timedelta(60)},
                  'Takeoff': {'Last': takeoff, 'Due': takeoff+timedelta(45)},
                  'Sortie': {'Last': sortie, 'Due': sortie+timedelta(45)},
                  'Instrument Approach': {'Last': instrument_approach, 'Due': instrument_approach+timedelta(45)},
                  'Nose IR': {'Last': noseir, 'Due': noseir+timedelta(90)},
                  'MTS IR': {'Last': mts, 'Due': mts+timedelta(90)},
                  'Landing': {'Last': landing, 'Due': landing+timedelta(45)}}

    crew_member_info = {
        'employee_id': value[4],
        'last_name': value[2],
        'suffix': value[3],
        'first_name': value[0],
        'middle_name': value[1],
        'crew_position': value[5],
        'currencies': currencies
    }
    try:
        crews.insert_one(crew_member_info)
    except IndexError:
        print('try again')

def delete_crew(_id):
    result = {'_id': _id}
    del_crew = crews.delete_one(result)
    return del_crew
