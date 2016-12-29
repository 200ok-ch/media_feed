#!/usr/bin/python3

import os
import sys
import shutil
import urllib3

urllib3.disable_warnings()

DOWNLOADS_DIR = '/tmp'

# 33c3 specific:

fahrplan_location = "https://fahrplan.events.ccc.de/congress/2016/Fahrplan/schedule.xml"
event_pattern_head = "https://fahrplan.events.ccc.de/congress/2016/Fahrplan/events/"
event_pattern_tail = ".html"

from xml.dom.minidom import parse, parseString

def usage(name): 
    print('Usage: ')
    print("%s <input xml> <name of the talk> <media url>" % (str(name)))
    exit()

def find_talk(file_name, talk_name, media_url, response): 
    xml = parse(file_name)

    for node in xml.getElementsByTagName("title"):
        if str.upper(talk_name) in str.upper(node.childNodes[0].data):
            title = node.childNodes[0].data

            #  Event
            par = node.parentNode

            try: 
                sub = par.getElementsByTagName("subtitle")[0].childNodes[0].data
            except: 
                sub = ""
                print("Element has no subtitle")

            try: 
                desc = par.getElementsByTagName("description")[0].childNodes[0].data
            except: 
                desc = None
                print("Element has no description")


            # Notes about the talk
            headers = response.getheaders()
            try: 
                media_type =   headers["Content-Type"]
            except: 
                media_type = ""
                print("Media had no Content-Type")

            try: 
                media_length = headers["Content-Length"]
            except: 
                media_length = ""
                print("Media had no Content-Length")

            event_id = par.getAttribute('id')
            
            print('')
            print("  - title: '%s'" % (title))
            print("    published: %s" % (headers["Date"]))
            print("    subtitle: '%s'" % (sub))
            print("    media_url: %s" % (media_url))
            print("    media_type: %s" % (media_type))
            print("    media_length: %s" % (media_length))
            print("    web_url: %s%s%s " % (event_pattern_head, event_id, event_pattern_tail))
            if desc: 
                print("    description: >-")
                print("       %s " % (str.replace(desc, "\n", "\n       ")))
            else: 
                print("    description: ")

################################################################################

args = sys.argv
http = urllib3.PoolManager()

if not len(args) == 3:
    print('Not enough arguments')
    print('')
    usage(args[0])

try: 
    response = http.request('HEAD', args[2])
except: 
    print("URL was not valid")
    print('')
    usage(args[0])

if not response.status == 200:
    print("HTTP status was not 200 - OK")
    print('')
    usage(args[0])

name = fahrplan_location.rsplit('/', 1)[-1]

# Combine the name and the downloads directory to get the local filename
filename = os.path.join(DOWNLOADS_DIR, name)

# Download the file if it does not exist
if not os.path.isfile(filename):
    print("Fahrplan not there - downloading")
    with http.request('GET', fahrplan_location, preload_content=False) as r, open(filename, 'wb') as out_file:       
       shutil.copyfileobj(r, out_file)
else:
    print("Fahrplan was there - not downloading")

find_talk(filename, args[1], args[2], response)
