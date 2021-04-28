from pymongo import MongoClient
import urllib.parse
import random
import names
from connection import *


db = client.metrics_tracker
crews = db.crews


def get_crew_query(excluded_fields=None):
    if excluded_fields is None:
        crew_list = [list(crew.values()) for crew in crews.find()]
    else:
        excluded_fields_pass = dict.fromkeys(excluded_fields, False)
        crew_list = [list(crew.values()) for crew in crews.find({}, excluded_fields_pass)]
    return crew_list

def get_crew_column_query(excluded_fields=None):
    if excluded_fields is None:
        column_list = [key.title().replace('_', ' ') for key in crews.find_one()]
    else:
        excluded_fields_pass = dict.fromkeys(excluded_fields, False)
        column_list = [key.title().replace('_', ' ') for key in crews.find_one({}, excluded_fields_pass)]
    return column_list

def find_crew(user_input):
    result = db.crews.find({'crew_position': f'{user_input}'})
    return result

def edit_crew_member():
    # get crew info
    # present crew info
    # allow to be changed
    # mongo update method
    pass

def add_crew_members(value):
    crew_member_info = {
        '_id': value[4],
        'employee_id': value[4],
        'last_name': value[2],
        'suffix': value[3],
        'first_name': value[0],
        'middle_name': value[1],
        'crew_position': value[5]
    }
    try:
        crews.insert_one(crew_member_info)
    except:
        print('try again')

def delete_crew(employee_id):
    employee_id = {'employee_id': employee_id}
    crews.delete_one(employee_id)

def gen_random_crew():
    gender = random.choice(['male', 'female'])
    first_name = names.get_first_name(gender=gender)
    middle_name = names.get_first_name(gender=gender)
    last_name = names.get_last_name()

    try:
        employee_id = random.randint(13370001, 13380000)
    except:
        employee_id = random.randint(13370001, 13380000)

    crew_position = random.choices(['SO', 'P', 'ESO', 'EP'], weights=(45, 40, 10, 5), k=1)[0]

    if gender == 'male':
        suffix = random.choice(['Jr.', 'Sr.', 'III', 'IV', '', '', '', '', '', '', '', '', '', ''])
    else:
        suffix = ''

    return first_name, middle_name, last_name, suffix, employee_id, crew_position
