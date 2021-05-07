import random

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
        suffix = random.choices(['Jr.', 'Sr.', 'III', 'IV', None], weights=(10, 10, 5, 2, 73), k=1)
    else:
        suffix = ''

    return first_name, middle_name, last_name, suffix, employee_id, crew_position

def get_crew_query(*query):
    crew_list = [list(crew.values()) for crew in crews.find(*query)]
    print(crew_list)
    return crew_list

def get_crew_column_query(*query):
    column_list = [key.title().replace('_', ' ') for key in crews.find_one(*query)]
    print(column_list)
    return column_list

def find_crew(employee_ids):
    crew_on_flight = [crews.find({'employee_id': employee_id})[0].values() for employee_id in employee_ids]
    return crew_on_flight

def edit_crew_member():
    # get crew info
    # present crew info
    # allow to be changed
    # mongo update method
    pass

def add_crew_members(value):
    crew_member_info = {
        'employee_id': value[4],
        'last_name': value[2],
        'suffix': value[3],
        'first_name': value[0],
        'middle_name': value[1],
        'crew_position': value[5]
    }
    try:
        crews.insert_one(crew_member_info)
    except IndexError:
        print('try again')

def delete_crew(_id):
    result = {'_id': _id}
    del_crew = crews.delete_one(result)
    return del_crew
