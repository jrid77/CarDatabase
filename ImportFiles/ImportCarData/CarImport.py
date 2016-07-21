#!/usr/bin/python

import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()


def insertIntoTable(manufacturer, model, displacement, hp, cylinders, transmissionType, gears, avgMpg):

	sql = """INSERT INTO CAR (manufacturer, model, displacement, hp, cylinders, transmission, gears, avgMpg) 
			 VALUES ({ma}, {mo}, {d}, {h}, {c}, {t}, {g}, {a});""".format(ma=manufacturer, mo=model, d=displacement, h=hp, c=cylinders, t=transmissionType, g=gears, a=avgMpg) 
	cursor.execute(sql)
	db.commit()
	


def parseFileForData(inputString, i):
	p = inputString.split(',')

	try:
		insertIntoTable(p[1], p[4], p[7], p[10], p[11], p[14], p[15], p[46])
	except:
		print "Line " + str(i) + " is a repeat."

def readFile():
	file = open('CarData.csv', 'r')

	file.readline()
	
	entireFile = file.read()

	lines = entireFile.split('\n')
	i=0

	for line in lines:
		i = i+1
		parseFileForData(line, i)


readFile()
