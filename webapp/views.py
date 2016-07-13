#!/usr/bin/python
import json
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Play

def graph(request):
    return render(request,'personal/bar-graph.html',{'content':sample.JSON})

def index(request):
#    string = getData(request)
    return HttpResponse("""<h2>HEY</h2>
                        <a href="cars" class="button">Cars</a>
                        <form action="127.0.0.1/webapp/cars">
                        <input type="submit" value="Go to Cars">
                        </form>
                        <a href="{% url 'cars' %}">Click to go to Cars</a>
                        """)
#    conn = MySQLdb.connect (host ="127.0.0.1",
#                        user = "alexanjs",
#                        passwd = "D@t@b@ses333",
#			db = "sampledb")

def cars(request):
    return HttpResponse("""<h2>YOU ARE NOW IN CARS!<h2>""")
 
    




