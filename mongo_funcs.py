from pymongo import MongoClient
from pprint import pprint
import names
import random
import urllib.parse
import re

me = urllib.parse.quote_plus('LarryDCJ')
rd = urllib.parse.quote_plus('dismyside42')

client = MongoClient("mongodb+srv://%s:%s@cluster0.nhqsm.mongodb.net/metrics_tracker?retryWrites"
                     "=true&w=majority" % (me, rd), authSource='admin')

db = client['metrics_tracker']
crew_members = db['crew_members']
sites = db['sites']


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


# get site list from database
def get_site_query():
    site_list = []

    for site in sites.find():
        site = site.values()
        site = list(site)[1:]
        site_list.append(site)
    return site_list


# get site columns from db
def get_site_column_query():
    site_list = []
    for site in sites.find():
        site = list(site.keys())[1:]
        for column_header in site:
            site_list.append(column_header.title().replace('_', ' '))
        break
    return site_list


#
def find_all_via_crew_pos():
    result = db.crew_members.find({'crew_position': 'SO'})
    return result


#
def add_crew_members(value):
    crew_pos_list = ['P', 'SO', 'IP', 'ISO', 'EP', 'ESO']
    crew_member_info = {
        'employee_id': value[4],
        'last_name': value[2],
        'suffix': value[3],
        'first_name': value[0],
        'middle_name': value[1],
        'crew_position': value[5],
    }
    crew_members.insert_one(crew_member_info)
    print('Done.')


# generates fake sites, just enter how many
def add_sites(value):
    site_info = {
        'site_id': value[0],
        'country': value[1],
        'num_ac': value[2],
        'num_full_staff': value[4],
        'num_curr_staff': value[3]
    }
    sites.insert_one(site_info)
    print('Done.')


# delete member
def drop_crew_member(emp_num):

    crew_member_id = {'employee_id': f'{emp_num}'}
    crew_members.delete_one(crew_member_id)
    print('Done')
