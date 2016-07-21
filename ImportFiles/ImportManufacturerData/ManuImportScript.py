#!/usr/bin/python

import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()


def insertIntoTable(mname, mmarketShare):
	
	sql = """INSERT INTO MANUFACTURER (name, marketShare) 
			 VALUES ("{m}", "{s}");""".format(m=mname, s=mmarketShare)
	

	cursor.execute(sql)
	db.commit()
	


def parseFileForData(inputString, i):
	p = inputString.split(',')
	
	
	insertIntoTable(p[0], str(p[16]))
	

def readFile():
	file = open('data.csv', 'r')
	
	entireFile = file.read()

	lines = entireFile.split('\n')
	i=0

	for line in lines:
		i = i+1
		parseFileForData(line, i)


readFile()
