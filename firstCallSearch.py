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
# Get's the admin name to search and the date:
#
print("")
name = input("Admin name?: ")
name = name.title()
date = input("Date to check? (YYYY-MM-DD format):" )

#
#  Getting the sites data:
#   This calls an internal site so this will need to be ran on Liquid Web's network.
#   BeautifulSoup is doing the bulk of the work here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
#   Relaces '\n' with ' ' so 'split' can do its thing.
#
url = "http://phones.int.company.com/phones/queuelogin.php?dstart=" + date + "&qnum=1011"
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
#   Checks for providfed name on the date provided.
#   If the name is found, it pulls the 7th variable listed after their name (which is the start time) once.
#   Makes it pretty too <3 <3 <3:
#
print("")
print("Checking: " + url)
print("Date: " + date)
print("")
if name in text:
    time = text.index(name)
    time = int(int(time) + int(8))
    print("-------------------------------------------------")
    print("|\tAdmin: " + name + "\t|\tTime: " + text[time] + "\t|")
    print("-------------------------------------------------")
elif text[0] == "dstart":
    print("Start date is not a valid date. Please try again.")
else:
    print("Name not found for that date.")

print("")

#############
#           #
# DEBUGGING #
#           #
#############

#print(url)
#print(date)
#print(name)
