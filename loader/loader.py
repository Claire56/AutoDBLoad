import time, logging,
from datetime import datetime
import os ,sys,traceback
import pandas as pd
import pypyodbc as pyodbc
from helper import FileDetails, tableName_insert,Dbdetails
################################################################################
python_file_path = os.path.dirname(os.path.realpath(__file__))
################################################################################


def loader(file2load):
    log_name = "loader.log"#edit that 
    result = {'isok':-1, 'error_message':'', 'uuid':0}
    #open DB if its only one file
    #connect to the database 
    db= pyodbc.connect(Dbdetails.conn_string)
    cur_db = db.cursor()

    #open the file 
    with open(file2load,'r') as f:
        reader = csv.reader(f)#create reader object 
        colums = next(reader)#first row is columns, make sure this is correct
        for row in reader:
            #store row in DB
            sql = tableName_insert(row )#refactor this based on your data, colums vs row
            cur_db.execute(sql)
            cur_db.commit()
            
        logging.info('{file2load} inserted into database ')

    db.close()
        
    result['isok'] = 1
    return result
  

if __name__ == "__main__":
    
    for item in os.listdir(FileDetails.file_location):
        load = loader(item)















    # with open('datafiles.txt', 'r') as f:
    #     for line in f:
    #         line = line.strip()
    #         load = watcher(line)

