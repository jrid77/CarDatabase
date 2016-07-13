#!/usr/bin/python

import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()


def insertIntoTable(carid, manufacturer, vehicleType, manuid, engineid, cyl, displacement, hp, carbonm, carbond, nitro, miles):

	sql = """INSERT INTO CAR (CarId, Model, Year, VehicleType, ManuId, EngineID) VALUES ({cid}, {m}, {y}, {v}, {mid}, {eid});
		 INSERT INTO ENGINE (CarID, EngineID, Cylinders, Displacement, Horsepower) VALUES ({cid}, {eid}, {c}, {d}, {h});
		 INSERT INTO TRANSMISSION (CarID, Type, Gears, Drivetrain) VALUES({cid}, {t}, {g}, {d});
		 INSERT INTO GAS_INFO (CarID, CO, COO, NOX, MPG) VALUES({cid}, {co}, {coo}, {nox}, {mpg});""".format(cid = carid, m = manufacturer, v = vehicleType, mid = manuid, eid = engineid, c = cyl, d = displacement, h = hp, co = carbonm, coo = carbond, nox = nitro, mpg = miles)
	insert = ' '.join(sql.split())
	
	cursor.execute(sql)
	db.commit()
	


def parseFileForData(inputString, i):
	p = inputString.split(',')

	try:
		insertIntoTable()
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
