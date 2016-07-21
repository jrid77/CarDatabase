#!/usr/bin/python

import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()


def insertIntoTable(array):

	sql = """INSERT INTO RECALLS (Year, ManuID, Model, NumberAffected, Issue) VALUES ({y}, "{ma}", "{mi}", {n}, "{i}");""".format(y = array[1], ma = array[5].upper(), mi = array[6], n = array[7], i = array[8])
	cursor.execute(sql)
	db.commit()
	


def parseFileForData(inputString, i):
	p = inputString.split('|')
	if len(p) is 15:
		print i
		insertIntoTable(p)

def readFile():
	print "import recalls"
	file = open('recalls.csv', 'r')
	file.readline()	
	entireFile = file.read()


	lines = entireFile.split('\n')
	i=1
	for line in lines:
		parseFileForData(line, i)
		i = i + 1

readFile()
