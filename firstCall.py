#!/usr/bin/python
# Written by Joshthehero91
#  Importing the nessecary modules: 
#   'datetime' for calculating yesterdays date.
#   'requests' to make the httpd request for the URL.
#   'bs4' has 'BeautifulSoup' which will be used to parse the HTML.
#
from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup

#
#  List of admin names. Following the format, additional names or alternate names can be added:
#   Currently only lists 1st shift admins.
#
names = ["White", 
"Orange", 
"Blonde", 
"Pink", 
"Blue", 
"Brown"]

#
#  Calculating yesterdays date:
#   Needs to be output in 'YYYY-MM-DD' format
#    For example: 2018-12-25
#
yesterday = date.today() - timedelta(1)
yesterday=str(yesterday.strftime('%Y-%m-%d'))

#
#  Getting the sites data:
#   This calls an internal site so this will need to be ran on Liquid Web's network.
#   BeautifulSoup is doing the bulk of the work here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
#   Relaces '\n' with ' ' so 'split' can do its thing.
#
url = "http://phones.int.company.com/phones/queuelogin.php?dstart=" + yesterday + "&qnum=1011"
html = requests.get(url)
#
#  Ensure HTTP response is 200 before proceeding:
#
if html.status_code != 200:
    raise requests.ConnectionError("Expected status code 200, but got {}".format(page.status_code))

soup = BeautifulSoup(html.text, 'html.parser')
text = soup.get_text()
text = text.replace('\n', ' ')
text = text.split()

#
#  Here's the magic:
#   Checks for each name listed in 'names' in the parsed text.
#   If the name is found, it pulls the 7th variable listed after their name (which is the start time) once.
#   Makes it pretty too <3 <3 <3:
#
print("")
print("Checking: " + url)
print("Date: " + yesterday)
print("")
for i in range(0, len(names)):
    if names[i] in text:
        admins = names[i]
        time = text.index(admins)
        time = int(int(time) + int(8))
        print("-------------------------------------------------")
        print("|\tAdmin: " + admins + "\t|\tTime: " + text[time] + "\t|")
        
print("-------------------------------------------------")
print("")

#############
#           #
# DEBUGGING #
#           #
#############

#print(url)
#print(yesterday)
