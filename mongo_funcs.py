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

db = client.metrics_tracker
crew_members = db.crew_members
sites = db.sites


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
