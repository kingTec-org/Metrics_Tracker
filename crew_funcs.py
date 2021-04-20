from pymongo import MongoClient
import urllib.parse


me = urllib.parse.quote_plus('LarryDCJ')
rd = urllib.parse.quote_plus('dismyside42')

client = MongoClient("mongodb+srv://%s:%s@cluster0.nhqsm.mongodb.net/metrics_tracker?retryWrites"
                     "=true&w=majority" % (me, rd), authSource='admin')

db = client.metrics_tracker
crew_members = db.crew_members
sites = db.sites


# get crew member list from database
def get_crew_query():
    crew_list = []
    for crew in crew_members.find():
        crew = crew.values()
        crew = list(crew)[1:]
        crew_list.append(crew)
    return crew_list


# get crew member columns from db
def get_crew_column_query():
    column_list = []
    for col in crew_members.find():
        col = list(col.keys())[1:]
        for column_header in col:
            column_list.append(column_header.title().replace('_', ' '))
        break
    return column_list


# find crew via user string
def find_crew(user_input):
    result = db.crew_members.find({'crew_position': f'{user_input}'})
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
    crew_members.insert_one(crew_member_info)


# delete member
def delete_crew_member(emp_num):
    crew_member_id = {'_id': emp_num}
    crew_members.delete_one(crew_member_id)
