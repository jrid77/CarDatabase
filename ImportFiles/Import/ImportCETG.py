#!/usr/bin/python

import MySQLdb
import csv


db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")

def insertIntoTable(carid, model, year, vehicleType, manuid, engineid, cyl, displacement, hp, carbonm, carbond, nitro, miles, transtype, drivetrain, gears):

	if miles == "":
		miles = 0.0

	cursor = db.cursor()
	manuid = manuid.upper()
	drivetrain += '"'

	sql = """INSERT INTO CAR (CarID, Model, Year, VehicleType, ManuId) VALUES ({cid}, {m}, {y}, {v}, {mid});
		 INSERT INTO ENGINE (CarID, Cylinders, Displacement, Horsepower) VALUES ({cid}, {c}, {d}, {h});
		 INSERT INTO TRANSMISSION (CarID, Type, Gears, Drivetrain) VALUES({cid}, {t}, {g}, {dt});
		 INSERT INTO GAS_INFO (CarID, CO, COO, NOX, MPG) VALUES({cid}, {co}, {coo}, {nox}, {mpg});""".format(cid = carid, m = model, y = year, v = vehicleType, mid = manuid, eid = engineid, c = cyl, d = displacement, h = hp, co = float(carbonm), coo = float(carbond), nox = float(nitro), mpg = float(miles), t = transtype, dt = drivetrain, g = gears)

	insert = ' '.join(sql.split())
	print sql
	
	cursor.execute(sql)
	cursor.close()
	db.commit()


def parseFileForData(inputString, i):
	p = inputString.split(',')
	print i
	try:
		insertIntoTable(str(i), p[4],p[0], p[9], p[3], p[12], p[15], p[7], p[10], p[40], p[41], p[42], p[46], p[14], p[18], p[15])
	except:
		print i
	

def readFile():
	file = open('CarData.csv', 'r')

	file.readline()
	
	entireFile = file.read()

	lines = entireFile.split('\n')
	i=0
	#parseFileForData(lines[1], 1)
	for line in lines:
		i = i+1
		parseFileForData(line, i)

readFile()
