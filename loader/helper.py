
import os,sys,time,shutil,smtplib,datetime,subprocess,traceback
import pandas as pd
import pypyodbc as pyodbc
from itertools import repeat
from multiprocessing import Pool
import distutils.dir_util as dutils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Dbdetails:
    server=""
    Db=""
    User_name=""
    user_PW = ""
    conn_string= 'Driver={SQL Server};Server=%s;Database=%s;UID=%s;PWD=%s;' %(server, Db,User_name, user_PW)


class FileDetails:
    file_location =''
    archieve_loc =''


def tableName_insert(FileFullPath, EquipmentID, result, comment):
    return ("INSERT INTO Datatablename "
    "(FileFullPath,EquipmentID,DateCopied,Result,Comment) "
    "VALUES ('" + FileFullPath + "','"
    + EquipmentID + "',"
    + "SYSDATETIME(),"
    + str(result) + ",'"
    + comment + "')" )

def move_file(myfile):
    source = FileDetails.file_location + "\\" + myfile
    destination =FileDetails.archieve_loc + "\\" + myfile
    shutil.move(source,destination)