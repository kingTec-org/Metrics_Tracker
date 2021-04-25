from pymongo import MongoClient
import urllib.parse
import random
import names

me = urllib.parse.quote_plus('LarryDCJ')
rd = urllib.parse.quote_plus('dismyside42')

client = MongoClient("mongodb+srv://%s:%s@cluster0.nhqsm.mongodb.net/metrics_tracker?retryWrites"
                     "=true&w=majority" % (me, rd), authSource='admin')

db = client.metrics_tracker

crews = db.crews

# get crew member list from database
def get_crew_query(excluded_fields=['_id']):
    crew_list = [list(crew.values())
                 for crew in crews.find({}, {f'{excluded_fields[0]}': False})]
    return crew_list

# get crew member columns from db
def get_crew_column_query(excluded_fields=['_id']):
    column_list = [key.title().replace('_', ' ')
                   for key in crews.find_one({}, {f'{excluded_fields[0]}': False})]
    return column_list


# find crew via user string
def find_crew(user_input):
    result = db.crews.find({'crew_position': f'{user_input}'})
    return result

# #-----!!CRUD FUNCTIONS!!-----# #


# edit existing crew profile
def edit_crew_member():
    # get crew info
    # present crew info
    # allow to be changed
    # mongo update method
    pass


# add crew member based on user input
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

# delete member
def delete_crew_member(emp_num):
    crew_member_id = {'_id': emp_num}
    crews.delete_one(crew_member_id)

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
