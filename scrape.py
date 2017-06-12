#!/usr/bin/env python

import request
import urllib2
import csv
import re
from lxml import html
import MySQLdb
import string

#
# Scraper to gather user information from the bitcointalk forum.
#



#Connect to the MySQL database
db = MySQLdb.connect("localhost","username","password","database")

for i in xrange(0,10000):
	cursor = db.cursor()
	page = requests.get("https://bitcointalk.org/index.php?action=profile;u={}".format(i))
	tree = html.fromstring(page.text)

	#We assign variables to import data into the db.

	bitcointalkname = tree.xpath('//*[@id="bodyarea"]/table/tr/td/table/tr[2]/td[1]/table/tr[1]/td[2]/text()')
	
