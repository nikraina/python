__author__ = 'nikhil'

import json

def simple_reciever(j_str):
    j_obj = json.loads(j_str)
    print j_obj["pet"][0]["species"]

def simple_caller():
    str = ''' { "pet": [ { "species":  "Dahut", "name": "Hypatia" }, { "species":  "Felis Stultus", "name": "Billie" } ] }'''
    simple_reciever(str)

simple_caller()