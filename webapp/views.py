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
    return HttpResponse("""<h2 align=center><font color=white>Index</font></h2>
    				<style>
					body {
						background-image: url("p1.jpg");
						background-color:Black;
						&nbsp;
					}
					</style>
    				<div align=center>
                        <button onclick="location.href='http://127.0.0.1:8000/webapp/recalls'">
							Recalls</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/mpg'">
							Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/gasToHP'">
							Gas Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/sales'">
							Sales</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/cylVsHP'">
							Cyliders Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/transmission'">
							Transmission Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/MostTowed'">
							Most Towed</button>
					</div>
					<hr style="width:50%"/>
					<div align=center>
						<img src="https://images7.alphacoders.com/460/460370.jpg" width="1280px" height="800px"/>
					</div>
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

	sql = """SELECT c.Model,g.MPG FROM GAS_INFO g,CAR c WHERE g.CarID = c.CarID ORDER BY MPG DESC LIMIT 10;"""
	cursor.execute(sql)
	tupleOfMPG = cursor.fetchall()
	listOfMPG = createListOfMPGs(tupleOfMPG)
	
	html = """
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
        data.addColumn('string', 'Model');
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
    <div id="chart_div" align=center></div>
  </body>
</html>"""
	return html

def getMostRecallsVis():
	db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
	cursor = db.cursor()

	sql = """SELECT ManuID, SUM(NumberAffected) FROM RECALLS GROUP BY (ManuID) ORDER BY SUM(NumberAffected) DESC LIMIT 10;"""
	cursor.execute(sql)
	tupleOfMPG = cursor.fetchall()
	listOfMPG = createListOfMPGs(tupleOfMPG)
	
	html = """
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
        data.addColumn('string', 'Manufacturer');
        data.addColumn('number', 'Number Of Recalls');
        data.addRows(""" + str(listOfMPG) + """);

        // Set chart options
        var options = {'title':'Top Ten Manufacturers with most recalls',
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
    <div id="chart_div" align=center></div>
  </body>
</html>"""
	return html

def getMPGvsDRIVETRAIN():
	db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
	cursor = db.cursor()

	sql = """SELECT t.Type, AVG(g.MPG) FROM TRANSMISSION t,GAS_INFO g WHERE t.CarID=g.CarID GROUP BY (t.Type) ORDER BY AVG(g.MPG) DESC;"""
	cursor.execute(sql)
	tupleOfMPG = cursor.fetchall()
	listOfMPG = createListOfMPGs(tupleOfMPG)
	
	html = """
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
        data.addColumn('string', 'Drivetrain');
        data.addColumn('number', 'MPG');
        data.addRows(""" + str(listOfMPG) + """);

        // Set chart options
        var options = {'title':'Drivetrain vs MPG',
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
    <div id="chart_div" align=center></div>
  </body>
</html>"""
	return html

def getMostTowedModel():
	db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
	cursor = db.cursor()

	sql = """SELECT Model,COUNT(Model) FROM TOWS GROUP BY (Model) ORDER BY COUNT(Model) DESC LIMIT 25;"""
	cursor.execute(sql)
	tupleOfMPG = cursor.fetchall()
	listOfMPG = createListOfMPGs(tupleOfMPG)
	
	html = """
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
        data.addColumn('string', 'Drivetrain');
        data.addColumn('number', 'MPG');
        data.addRows(""" + str(listOfMPG) + """);

        // Set chart options
        var options = {'title':'Most Towed Cars',
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
    <div id="chart_div" align=center></div>
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
          trendlines: {0: {
          	type:'exponential',
          	visableInLegend:true,
          } },
        };

        var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px; margin:0 auto;"></div>
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
          title: 'Manufacturer Market Share'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart" style="width: 900px; height: 500px; margin:0 auto;"></div>
  </body>
</html>"""
	return html

def getCylVsHpVis():
	db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
	cursor = db.cursor()

	sql = """SELECT Cylinders,Horsepower FROM ENGINE;"""
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
        data.addColumn('number', 'Cylinders');
        data.addColumn('number', 'Horsepower');
        data.addRows(""" + str(listOfMPG) + """);

        var options = {
          title: 'Cylinder vs. Horsepower comparison',
          hAxis: {title: 'Cylinders', minValue: 0, maxValue: 16.0},
          vAxis: {title: 'Horsepower', minValue: 0, maxValue: 800.0},
          trendlines: {0: {} },
          legend: 'none',
        };

        var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px; margin:0 auto;"></div>
  </body>
</html>
"""
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


def recalls(request):
	
		
	table = getMostRecallsVis()
	html = """
			<head>
			<style>
			body {background-color:LightSteelBlue;}
			</style>
			</head>
			<body>
				<h2 align=center>Recalls</h2>
					<div align=center>
                        <button onclick="location.href='http://127.0.0.1:8000/webapp/recalls'">
							Recalls</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/mpg'">
							Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/gasToHP'">
							Gas Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/sales'">
							Sales</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/cylVsHP'">
							Cyliders Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/transmission'">
							Transmission Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/MostTowed'">
							Most Towed</button>
					</div>
				<hr style="width:50%"/>
			</body>"""
	html = html+table
	return HttpResponse(html)

def gasMileage(request):
	
	#return HttpResponse("""<h2>Manufacturer</h2>""")
	table = getMPGVis()
	html = """
			<head>
			<style>
			body {background-color:LightSteelBlue;}
			</style>
			</head>
			<body>
				<h2 align=center>Gas Mileage</h2>
					<div align=center>
                        <button onclick="location.href='http://127.0.0.1:8000/webapp/recalls'">
							Recalls</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/mpg'">
							Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/gasToHP'">
							Gas Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/sales'">
							Sales</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/cylVsHP'">
							Cyliders Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/transmission'">
							Transmission Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/MostTowed'">
							Most Towed</button>
					</div>
				<hr style="width:50%"/>
			</body>"""
	html = html+table
	return HttpResponse(html)

def gasToHP(request):
	#return HttpResponse("""<h2>Transmission</h2>""")
	table = getAVGMPGVis()
	html = """
			<head>
			<style>
			body {background-color:LightSteelBlue;}
			</style>
			</head>
			<body>
				<h2 align=center>Gas Mileage Related To HP</h2>
					<div align=center>
                        <button onclick="location.href='http://127.0.0.1:8000/webapp/recalls'">
							Recalls</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/mpg'">
							Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/gasToHP'">
							Gas Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/sales'">
							Sales</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/cylVsHP'">
							Cyliders Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/transmission'">
							Transmission Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/MostTowed'">
							Most Towed</button>
					</div>
				<hr style="width:50%"/>
			</body>"""
	html = html+table
	return HttpResponse(html)

def sales(request):
	#return HttpResponse("""<h>engine</h2>""")
	table = getRecentSalesVis()
	html = """
			<head>
			<style>
			body {background-color:LightSteelBlue;}
			</style>
			</head>
			<body>
				<h2 align=center>Sales</h2>
					<div align=center>
                        <button onclick="location.href='http://127.0.0.1:8000/webapp/recalls'">
							Recalls</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/mpg'">
							Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/gasToHP'">
							Gas Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/sales'">
							Sales</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/cylVsHP'">
							Cyliders Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/transmission'">
							Transmission Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/MostTowed'">
							Most Towed</button>
					</div>
				<hr style="width:50%"/>
			</body>"""
	html = html+table
	return HttpResponse(html)

def cylVsHP(request):

	#return HttpResponse("""<h2>emissions</h2>""")

	table = getCylVsHpVis()
	html = """
			<head>
			<style>
			body {background-color:LightSteelBlue;}
			</style>
			</head>
			<body>
				<h2 align=center>Cylinders Vs. Horsepower</h2>
					<div align=center>
                        <button onclick="location.href='http://127.0.0.1:8000/webapp/recalls'">
							Recalls</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/mpg'">
							Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/gasToHP'">
							Gas Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/sales'">
							Sales</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/cylVsHP'">
							Cyliders Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/transmission'">
							Transmission Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/MostTowed'">
							Most Towed</button>
					</div>
				<hr style="width:50%"/>
			</body>"""
	html = html+table
	return HttpResponse(html)

def transmission(request):
	#return HttpResponse("""<h2>tows</h2>""")

	table = getMPGvsDRIVETRAIN()
	html = """
			<head>
			<style>
			body {background-color:LightSteelBlue;}
			</style>
			</head>
			<body>
				<h2 align=center>Transmisson Vs. Gas Mileage</h2>
					<div align=center>
                        <button onclick="location.href='http://127.0.0.1:8000/webapp/recalls'">
							Recalls</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/mpg'">
							Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/gasToHP'">
							Gas Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/sales'">
							Sales</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/cylVsHP'">
							Cyliders Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/transmission'">
							Transmission Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/MostTowed'">
							Most Towed</button>
					</div>
				<hr style="width:50%"/>
			</body>"""
	html = html+table
	return HttpResponse(html)

def mostTowed(request):
	table = getMostTowedModel()
	html = """
			<head>
			<style>
			body {background-color:LightSteelBlue;}
			</style>
			</head>
			<body>
				<h2 align=center>Towed Cars</h2>
					<div align=center>
                        <button onclick="location.href='http://127.0.0.1:8000/webapp/recalls'">
							Recalls</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/gas'">
							Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/gasToHP'">
							Gas Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/sales'">
							Sales</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/cylVsHP'">
							Cyliders Vs. HP</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/transmission'">
							Transmission Gas Mileage</button>
						<button onclick="location.href='http://127.0.0.1:8000/webapp/MostTowed'">
							Most Towed</button>
					</div>
				<hr style="width:50%"/>
			</body>"""
	html = html+table
	return HttpResponse(html)
