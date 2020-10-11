import time, logging,
from datetime import datetime
import os ,sys,traceback
import pandas as pd
import pypyodbc as pyodbc
from helper import FileDetails, tableName_insert,Dbdetails ,move_file
################################################################################
file_path = os.path.dirname(os.path.realpath(__file__))
################################################################################

current_time  = datetime.today().strftime('%Y%m%d')
log_name = file_path +'\\' + 'loader.log'
files = os.listdir(FileDetails.file_location)
#DB connection
db= pyodbc.connect(Dbdetails.conn_string)
cur_db = db.cursor()

for file_item in files:
    file_path = FileDetails.file_location + '\\' + file_item
    loader(file_path)

db.close()

def loader(file2load):
    
    result = {'isok':-1, 'error_message':''}
    #open the file 
    with open(file2load,'r') as f:
        reader = csv.reader(f)#create reader object 
        colums = next(reader)#first row is columns, make sure this is correct
        for row in reader:
            #store row in DB
            sql = tableName_insert(row )#refactor this based on your data, colums vs row
            cur_db.execute(sql)
            cur_db.commit()
            inserted = True
        if inserted:   
            logging.info('{file2load} inserted into database ')
            move_file(file2load)

    result['isok'] = 1
    return result
  

