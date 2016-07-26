#!/usr/bin/python

import MySQLdb
import csv

print "deleting data"

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()

sql = """CALL remove_data();"""
create = ' '.join(sql.split())

cursor.execute(create)

db.commit()

print "data deleted"


