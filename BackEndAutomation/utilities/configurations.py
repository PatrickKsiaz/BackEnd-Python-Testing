import configparser
import mysql.connector
from mysql.connector import Error




def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

connect_config  = {
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database'],
}

 
def getPassword():
    return "ddsfere"

def getConncetion():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print(e)



