#!/usr/bin/python
import json
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
import csv

from .models import Play

def graph(request):
    return render(request,'personal/bar-graph.html',{'content':sample.JSON})

def index(request):
#    string = getData(request)
    return HttpResponse("""<h2>Index</h2>
                        <button onclick="location.href='http://127.0.0.1:8000/webapp/cars'">
							Cars</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/manufacturer'">
							Manufacturer</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/transmission'">
							Transmission</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/engine'">
							Engine</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/emissions'">
							Emissions</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/tows'">
							Tows</button>
                        """)
#    conn = MySQLdb.connect (host ="127.0.0.1",
#                        user = "alexanjs",
#                        passwd = "D@t@b@ses333",
#			db = "sampledb")

def createCarHTMLRow(line):
	rowText = "<tr>"
	for element in line:
		rowText += "<td>" + str(element) + "</td>"
	rowText += "</tr>"
	return rowText

def getCarTable():
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
	return html


def cars(request):
	HttpResponse("""<g2>Cars</h2>""")
	table = getCarTable()
	return HttpResponse(table)

def manufacturer(request):
	HttpResponse("""<g2>Cars</h2>""")
	table = getCarTable()
	return HttpResponse(table)

def transmission(request):
	HttpResponse("""<g2>Cars</h2>""")
	table = getCarTable()
	return HttpResponse(table)

def engine(request):
	HttpResponse("""<g2>Cars</h2>""")
	table = getCarTable()
	return HttpResponse(table)

def emissions(request):
	HttpResponse("""<g2>Cars</h2>""")
	table = getCarTable()
	return HttpResponse(table)

def tows(request):
	HttpResponse("""<g2>Cars</h2>""")
	table = getCarTable()
	return HttpResponse(table)
