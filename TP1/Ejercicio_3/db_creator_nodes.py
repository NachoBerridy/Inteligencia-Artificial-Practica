import sqlite3 as sql
from path import*

conexion  = sql.connect("a_star1.db")

layout1 = Layout()
layout1.fill_mat()
path1 = Path(layout1)



conexion.execute(""" create table if not exists nodes (
                            n integer primary key,  
                            y integer,
                            x integer
                    )""")




def fill_dicts(path_1):

    racks = []
    for j in path_1.storage.mat:
        for i in j:
            if i.is_rack == False:
                racks.append((i.y,i.x))
    for j in path_1.storage.mat:
        for i in j:
            if i.is_cargo_bay == True:
                racks.append((i.y,i.x))

    for i in range(len(racks)):
                    conexion.execute("insert into nodes(n,y,x) values (?,?,?)", (i,racks[i][0],racks[i][1]))
                    
    conexion.commit()

fill_dicts(path1)

conexion.close()