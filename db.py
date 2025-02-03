import sqlite3
 
from sqlite3 import Error
 
def connection():
 
    try:
 
        con = sqlite3.connect('agenda.db')
 
        return con
 
    except Error:
 
        print(Error)


def sql_table(con):
 
    cursor = con.cursor()
    
    try:
        cursor.execute("CREATE TABLE contato(id_contato integer PRIMARY KEY AUTOINCREMENT, name text, tel text, cel text)")
        con.commit()
    except:
        pass

def insert_table(con,nome,tel,cel):
     
    cursor = con.cursor()

    cursor.execute("INSERT INTO contato (name,tel,cel) VALUES(?,?,?)",(nome,tel,cel))
 
    con.commit()

def select_table(con):
    
    cursor = con.cursor()

    cursor.execute("SELECT * FROM contato")
 
    rows = cursor.fetchall()
 
    for row in rows:
        print(row)
con = connection()
sql_table(con)

def sum(a=1,b=2):
 return a+b
