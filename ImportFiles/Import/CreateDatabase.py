#!/usr/bin/python

import MySQLdb
import csv

db = MySQLdb.connect("localhost", "root", "D@t@b@ses333", "CarDatabase")
	
cursor = db.cursor()

sql = """CREATE TABLE MANUFACTURER
		(
			ManuID VARCHAR(60) NOT NULL PRIMARY KEY,
			TotalSales INT, 
			RecentMonthSales INT,
			Growth VARCHAR(60)
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
			EngineID INT PRIMARY KEY AUTO_INCREMENT,
			CarID VARCHAR(60) NULL,
			Cylinders INT NULL,
			Displacement DECIMAL(3,1) NULL,
			Horsepower INT NULL,
			FOREIGN KEY (CarID) REFERENCES CAR(CarID)
		);
	CREATE TABLE TRANSMISSION
		(
			TranID INT PRIMARY KEY AUTO_INCREMENT,
			CarID VARCHAR(60) NULL,
			Type VARCHAR(60) NULL,
			Gears INT NULL,
			Drivetrain VARCHAR(60) NULL,
			FOREIGN KEY (CarID) REFERENCES CAR(CarID) 
		);
	CREATE TABLE GAS_INFO
		(
			GasID INT PRIMARY KEY AUTO_INCREMENT,
			CarID VARCHAR(60) NOT NULL,
			CO DECIMAL(10,5) NULL,
			COO DECIMAL(10,5) NULL,
			NOX DECIMAL(10,5) NULL,
			MPG DECIMAL(10,5) NULL,
			CHECK (MPG<200),
			FOREIGN KEY (CarID) REFERENCES CAR(CarID)
		);"""
create = ' '.join(sql.split())

cursor.execute(create)




