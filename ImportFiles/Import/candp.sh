#!/bin/bash
python dropTables
python CreateDatabase.py
python ImportCETG.py
python ImportManu.py
python ImportTows.py
python ImportRecalls.py
echo "done with imports"
