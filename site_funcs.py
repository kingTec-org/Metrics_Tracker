import random

import countries
from upconn import *

db = client.metrics_tracker
sites = db.sites

def get_site_query(excluded_fields=None):
    if excluded_fields is None:
        site_list = [list(site.values()) for site in sites.find()]
    else:
        excluded_fields_pass = dict.fromkeys(excluded_fields, False)
        site_list = [list(site.values()) for site in sites.find({}, excluded_fields_pass)]
    return site_list

def get_site_column_query(excluded_fields=None):
    if excluded_fields is None:
        column_list = [key.title().replace('_', ' ') for key in sites.find_one()]
    else:
        excluded_fields_pass = dict.fromkeys(excluded_fields, False)
        column_list = [key.title().replace('_', ' ') for key in sites.find_one({}, excluded_fields_pass)]
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
        'site_id': value[0],
        'country': value[1],
        'aircraft_type': value[2],
        'number_aircraft_assigned': value[3],
        'present_staff': value[4],
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
        site_id = f'Location 0{random.randint(1,15)}'
    except:
        site_id = f'Location 0{random.randint(1, 15)}'

    country = random.choice(countries.name)
    aircraft_type = random.choice(['KCQ-9', 'MQ-135', 'MC-46', 'KC-1', 'RQ-42'])
    aircraft_assigned = str(random.randint(1, 5))
    required_staff = str(int(aircraft_assigned) * 10)
    present_staff = str(int(aircraft_assigned) * random.choice([7, 8, 9, 10]))


    return site_id, country, aircraft_type, aircraft_assigned, present_staff, required_staff
