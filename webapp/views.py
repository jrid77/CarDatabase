#!/usr/bin/python
import json
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from decimal import *

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
def createListOfMPGs(tupleOfMPGs):
	print tupleOfMPGs
	listOfMPGs = [list(element) for element in tupleOfMPGs]
	print listOfMPGs
	for row in listOfMPGs:
		row[0] = str(row[0])
		row[1] = float(row[1])
	print listOfMPGs
	return listOfMPGs

def createListOfAVGMPGs(tupleOfMPGs):
	print tupleOfMPGs
	listOfMPGs = [list(element) for element in tupleOfMPGs]
	print listOfMPGs
	for row in listOfMPGs:
		row[0] = float(row[0])
		row[1] = float(row[1])
	print listOfMPGs
	return listOfMPGs

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
		html += createCarHTMLRow(line)	
		line = cursor.fetchone()
	html += "</table>"
	return html

def getMPGTable():
	db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
	cursor = db.cursor()

	sql = """SELECT GasID,MPG FROM GAS_INFO ORDER BY MPG DESC LIMIT 10;"""
	html = """<table style="width:100%">"""

	cursor.execute(sql)

	line = cursor.fetchone()
	while line is not None:	
		html += createCarHTMLRow(line)	
		line = cursor.fetchone()
	html += "</table>"
	return html

def getMPGVis():
	db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
	cursor = db.cursor()

	sql = """SELECT CarID,MPG FROM GAS_INFO ORDER BY MPG DESC LIMIT 10;"""
	cursor.execute(sql)
	tupleOfMPG = cursor.fetchall()
	listOfMPG = createListOfMPGs(tupleOfMPG)
	
	html = """<h2>Manufacturer</h2>
		<html>
  <head>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'CarID');
        data.addColumn('number', 'MPG');
        data.addRows(""" + str(listOfMPG) + """);

        // Set chart options
        var options = {'title':'Top Ten Gas Mileage Cars',
                       'width':900,
                       'height':600};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>

  <body>
    <!--Div that will hold the pie chart-->
    <div id="chart_div"></div>
  </body>
</html>"""
	return html

def getAVGMPGVis():
	db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
	cursor = db.cursor()

	sql = """SELECT Horsepower,MPG FROM GAS_INFO g, ENGINE e
			WHERE g.CarID = e.CarID;"""
	cursor.execute(sql)
	tupleOfMPG = cursor.fetchall()
	listOfMPG = createListOfAVGMPGs(tupleOfMPG)
	print listOfMPG
	html = """<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('number', 'CarID');
        data.addColumn('number', 'MPG');
        data.addRows(""" + str(listOfMPG) + """);

        var options = {
          title: 'Horsepower vs. MPG comparison',
          hAxis: {title: 'Horsepower', minValue: 0, maxValue: 800.0},
          vAxis: {title: 'MPG', minValue: 0, maxValue: 200.0},
          legend: 'none'
        };

        var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
  </body>
</html>
"""
	return html

def getRecentSalesVis():
	db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
	cursor = db.cursor()

	sql = """SELECT ManuID,RecentMonthSales FROM MANUFACTURER;"""
	cursor.execute(sql)
	tupleOfMPG = cursor.fetchall()
	listOfMPG = createListOfMPGs(tupleOfMPG)
	print listOfMPG

	html = """<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {

        var data = new google.visualization.DataTable();
        data.addColumn('string', 'CarID');
        data.addColumn('number', 'MPG');
        data.addRows(""" + str(listOfMPG) + """);

        var options = {
          title: 'My Daily Activities'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart" style="width: 900px; height: 500px;"></div>
  </body>
</html>"""
	return html



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
	return HttpResponse("""<h2>Cars</h2>""")
		
	#table = getCarTable()
	#return HttpResponse(table)

def manufacturer(request):
	
	#return HttpResponse("""<h2>Manufacturer</h2>""")
	table = getMPGVis()
	return HttpResponse(table)

def transmission(request):
	#return HttpResponse("""<h2>Transmission</h2>""")
	table = getAVGMPGVis()
	return HttpResponse(table)

def engine(request):
	#return HttpResponse("""<h>engine</h2>""")
	table = getRecentSalesVis()
	return HttpResponse(table)

def emissions(request):

	return HttpResponse("""<h2>emissions</h2>""")

	table = getCarTable()
	return HttpResponse(table)

def tows(request):
	return HttpResponse("""<h2>tows</h2>""")

	table = getCarTable()
	return HttpResponse(table)
