#!/usr/bin/python

import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()


def insertIntoTable(array):

	sql = """
INSERT INTO MANUFACTURER (ManuID, TotalSales, LeastRecentSales, RecentMonthSales) VALUES ("{id}", {s}, {l}, {m});
""".format(id = array[0].upper(),l = array[1], s = array[15], m = array[13])
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
	print "importing manus"
	file = open('informationonmanu.csv', 'r')
	
	entireFile = file.read()

	lines = entireFile.split('\n')
	i=0
	for line in lines:
		parseFileForData(line, i)
		i = i + 1

readFile()
