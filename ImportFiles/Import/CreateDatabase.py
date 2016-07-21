#!/usr/bin/python

import MySQLdb
import csv

print "creating database"

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()

sql = """
	CREATE TABLE MANUFACTURER
		(
			ManuID VARCHAR(60) NOT NULL PRIMARY KEY,
			TotalSales INT,
			LeastRecentSales INT,
			RecentMonthSales INT,
			Growth DECIMAL(5,2)
		);
	CREATE TABLE RECALLS
		(
			RecallID INT PRIMARY KEY AUTO_INCREMENT,
			Year INT,
			ManuID VARCHAR(60), 
			Model VARCHAR(60),
			NumberAffected INT,
			Issue VARCHAR(60)
		);
	CREATE TABLE TOWS
		(
			TowID INT NOT NULL PRIMARY KEY,
			Firm VARCHAR(60) NULL,
			Address VARCHAR(200) NULL,
			Phone VARCHAR(60) NULL,
			Manufacturer VARCHAR(60),
			Model VARCHAR(60)			
		);
	CREATE TABLE CAR
		(
			CarID VARCHAR(60) NOT NULL PRIMARY KEY,
			Model VARCHAR(60) NOT NULL,
			Year INT NULL,
			VehicleType VARCHAR(60) NULL,
			ManuID VARCHAR(60) NULL     
		);
	CREATE TABLE ENGINE
		(
			EngineID VARCHAR(60) PRIMARY KEY,
			CarID VARCHAR(60) NULL,
			Cylinders INT NULL,
			Displacement DECIMAL(3,1) NULL,
			Horsepower INT NULL,
			FOREIGN KEY (CarID) REFERENCES CAR(CarID)
		);
	CREATE TABLE TRANSMISSION
		(
			CarID VARCHAR(60) NULL,
			Type VARCHAR(60) NULL,
			Gears INT NULL,
			Drivetrain VARCHAR(60) NULL,
			FOREIGN KEY (CarID) REFERENCES CAR(CarID) 
		);
	CREATE TABLE GAS_INFO
		(
			CarID VARCHAR(60) NOT NULL,
			CO DECIMAL(10,5) NULL,
			COO DECIMAL(10,5) NULL,
			NOX DECIMAL(10,5) NULL,
			MPG DECIMAL(10,5) NULL,
			TotalEmissions DECIMAL(10,5) NULL,
			FOREIGN KEY (CarID) REFERENCES CAR(CarID)
		);
	CREATE TRIGGER insert_growth BEFORE INSERT ON MANUFACTURER
	FOR EACH ROW SET NEW.Growth = (NEW.RecentMonthSales - NEW.LeastRecentSales)/(NEW.LeastRecentSales);
	
	CREATE TRIGGER total_emmissions BEFORE INSERT ON GAS_INFO
	FOR EACH ROW SET NEW.TotalEmissions = NEW.CO + NEW.COO + NEW.NOX;	

	CREATE TRIGGER check_mpg BEFORE INSERT ON GAS_INFO
	FOR EACH ROW SET NEW.MPG = IF(NEW.MPG < 250, NEW.MPG, 0);"""
create = ' '.join(sql.split())

cursor.execute(create)

print "create database complete"


