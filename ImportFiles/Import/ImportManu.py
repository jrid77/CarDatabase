#!/usr/bin/python

import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()


def insertIntoTable(array):

	sql = """INSERT INTO MANUFACTURER (ManuID, TotalSales, RecentMonthSales) VALUES ("{id}", {s}, {m})""".format(id = array[0].upper(), s = array[15], m = array[13])
	
	cursor.execute(sql)
	db.commit()
	


def parseFileForData(inputString, i):
	p = inputString.split('|')
	print p
	insertIntoTable(p)

def readFile():
	file = open('informationonmanu.csv', 'r')
	
	entireFile = file.read()

	lines = entireFile.split('\n')
	i=0

	for line in lines:
		parseFileForData(line, i)
		i = i + 1

readFile()