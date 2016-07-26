#!/usr/bin/python

import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()


def insertIntoTable(array):

	sql = """
INSERT INTO TOWS (TowID, Firm, Address, Phone, Manufacturer, Model) VALUES ({id}, "{f}", "{a}", "{p}", "{ma}","{mo}");
""".format(id = array[0], f = array[1], a = array[2], p = array[3], ma = array[7].upper(), mo = array[8])
	print sql
	cursor.execute(sql)
	db.commit()
	


def parseFileForData(inputString, i):
	p = inputString.split('|')
	try:
		insertIntoTable(p)
		print i
	except:
		print 'Error in line data'

def readFile():
	print "importing tows"
	file = open('tows.csv', 'r')
	file.readline()	
	entireFile = file.read()


	lines = entireFile.split('\n')
	i=0

	for line in lines:
		parseFileForData(line, i)
		i = i + 1
		
readFile()
