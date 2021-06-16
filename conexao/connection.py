#-*- encoding: utf-8
import psycopg2

db = None
def get_connection():
    global db
    if(db == None):
        db = psycopg2.connect("dbname=mercado user=postgres password=212133")
        
    return db

def close_connection():
    global db
    db.close()