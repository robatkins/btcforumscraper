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


#The range is arbitrary. We scrape the first 10,000 users.
for i in xrange(0,10000):
	cursor = db.cursor()
	page = requests.get("https://bitcointalk.org/index.php?action=profile;u={}".format(i))
	tree = html.fromstring(page.text)

	#We assign variables to import data into the db.
	#In case of future problems it should be noted that tbody must be removed if you are using xpath.

	bitcointalkname = tree.xpath('//*[@id="bodyarea"]/table/tr/td/table/tr[2]/td[1]/table/tr[1]/td[2]/text()')
	bitcointalkemail = tree.xpath('//*[@id="bodyarea"]/table/tr/td/table/tr[2]/td[1]/table/tr[13]/td[2]/text()')
	bitcoinregistered = tree.xpath('//*[@id="bodyarea"]/table/tr/td/table/tr[2]/td[1]/table/tr[6]/td[2]/text()')
	bitcoinsignature = tree.xpath('//*[@id="bodyarea"]/table/tr/td/table/tr[2]/td[1]/table/tr[23]/td/table/tr[2]/td/div/text()')

	#We clean the data pulled from xpath by removing certain characters

	bitcointalknamed = str(bitcointalkname).replace('[','').replace(']','').replace("'",'')
	bitcointalkemaild = str(bitcointalkemail).replace('[','').replace(']','').replace("'",'')

	#We need to output our information in the terminal so that we know it's working.
	output = 'Inserting information from user with the following  username and email of (%s, %s)' % (bitcointalknamed or None, bitcointalkemaild or None)

	print output
 
	#Insert the information into the database.

	cursor.execute('INSERT INTO bitcointalkdb (username, email) VALUES ("%s", "%s")' % (bitcointalknamed or None, bitcointalkemaild or None))

	#Commit the changes to the database.
	db.commit()
