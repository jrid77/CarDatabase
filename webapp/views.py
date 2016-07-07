#!/usr/bin/python

import MySQLdb
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Play

def graph(request):
    return render(request,'personal/bar-graph.html',{'content':#insertJsonhere)

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

def showData():
    conn = MySQLdb.connect (host ="127.0.0.1",
                        user = "alexanjs",
                        passwd = "D@t@b@ses333",
			db = "sampledb")
 
    




