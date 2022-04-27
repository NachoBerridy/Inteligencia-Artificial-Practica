import sqlite3 as sql

conexion  = sql.connect("a_star.db")

cursor = conexion.cursor()
id = '2,1->2,9'
print("%s"%id)
ids = "SELECT costo FROM astar WHERE n ='%s'"%id
print ("SELECT costo FROM astar WHERE n ='%s'"%id)
costo  = cursor.execute("SELECT costo FROM astar WHERE n ='%s'"%id).fetchone()[0]

#costo = cursor.fetchone()[0]
print (costo)