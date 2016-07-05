#!/usr/bin/python

import MySQLdb
from django.shortcuts import render
from django.http import HttpResponse

def importData():
    

def getData():
    db = MySQLdb.connect("localhost", "alexanjs", "D@t@b@ses333", "sampledb")

    cursor = db.cursor()

    sql = "SELECT * FROM person"

    cursor.execute(sql)
    returnString = ''

    for row in cursor:
	returnString = "<p>" + returnString + str(row) + "</p>"

    db.close()

    return returnString

def index(request):
    string = getData()
    return HttpResponse("<h2>" + string + "</h2>")




