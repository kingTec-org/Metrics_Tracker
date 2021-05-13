import random

import countries
from upconn import *

db = client.metrics_tracker
sites = db.sites


def get_site_query(*query):
    site_list = [list(site.values()) for site in sites.find({}, *query)]
    return site_list

def get_site_column_query(*query):
    column_list = [key.title().replace('_', ' ') for key in sites.find_one({}, *query)]
    return column_list

def edit_site():
    # get site info
    # present site info
    # allow to be changed
    # mongo update method
    pass

def add_site(value):
    site_info = {
        '_id': value[0],
        'location': value[1],
        'aircraft_type': value[2],
        '# A/C': value[3],
        'present_staff': value[4],
        'assigned_crew': [],
        'required_staff': value[5]
    }
    try:
        sites.insert_one(site_info)
    except:
        print('try again')

def delete_site(site_id):
    site_id = {'_id': site_id}
    sites.delete_one(site_id)

def gen_random_site():
    try:
        site_id = f'Location {random.randint(1, 15)}'
    except:
        site_id = f'Location {random.randint(1, 15)}'

    country = random.choice(countries.name)
    aircraft_type = random.choice(['KCMQ-9', 'KCMQ-1', 'KCMQ-10'])
    aircraft_assigned = str(random.randint(1, 3))
    required_staff = str(int(aircraft_assigned) * 10)
    present_staff = str(int(aircraft_assigned) * random.choice([6, 7, 8, 9, 10]))

    return site_id, country, aircraft_type, aircraft_assigned, present_staff, required_staff
