from pymongo import MongoClient
import urllib.parse

me = urllib.parse.quote_plus('LarryDCJ')
rd = urllib.parse.quote_plus('dismyside42')

client = MongoClient("mongodb+srv://%s:%s@cluster0.nhqsm.mongodb.net/metrics_tracker?retryWrites"
                     "=true&w=majority" % (me, rd), authSource='admin')

db = client.metrics_tracker
crew_members = db.crew_members
sites = db.sites


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


# find site via user string
def find_site(user_input):
    result = db.site.find({'site_id': f'{user_input}'})
    return result


# #-----!!CRUD FUNCTIONS!!-----# #


# edit existing site profile
def edit_site():
    # get site info
    # present site info
    # allow to be changed
    # mongo update method
    pass


# add site based on user input
def add_site(value):
    site_info = {
        '_id': value[0],
        'site_id': value[0],
        'country': value[1],
        'num_ac': value[2],
        'num_curr_staff': value[3],
        'num_full_staff': value[4]
    }
    sites.insert_one(site_info)


# delete site
def delete_site(site_id):
    site_id = {'_id': site_id}
    sites.delete_one(site_id)
