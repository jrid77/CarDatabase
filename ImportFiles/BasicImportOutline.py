#!/usr/bin/python

import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()


def insertIntoTable(name, marketShare):

	sql = """INSERT INTO MANUFACTURER (name, marketShare) 
			 VALUES ({n}, {m});""".format(n=name, m=marketShare) 
	cursor.execute(sql)
	db.commit()
	


def parseFileForData(inputString, i):
	p = inputString.split(',')

	try:
		insertIntoTable(p[0], p[16])
	except:
		print "Line " + str(i) + " is a repeat."

def readFile():
	file = open('data.csv', 'r')

	file.readline()
	
	entireFile = file.read()

	lines = entireFile.split('\n')
	i=0

	for line in lines:
		i = i+1
		parseFileForData(line, i)


readFile()
