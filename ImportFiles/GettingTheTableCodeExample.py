#!/usr/bin/python

import MySQLdb
import csv

def createHTMLRow(line):
	rowText = "<tr>"
	for element in line:
		rowText += "<td>" + str(element) + "</td>"
	rowText += "</tr>"
	return rowText
		

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()

sql = """SELECT * FROM CAR WHERE ManuID = "FORD";"""
html = """<table style="width:100%">"""

cursor.execute(sql)

line = cursor.fetchone()
while line is not None:	
	html += createHTMLRow(line)	
	
	line = cursor.fetchone()
html += "</table>"
print html
