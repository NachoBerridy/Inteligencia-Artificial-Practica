import sqlite3 as sql
from path import*

conexion  = sql.connect("a_star1.db")

layout1 = Layout()
layout1.fill_mat()
path1 = Path(layout1)



conexion.execute(""" create table if not exists astar (
                            n text primary key,  
                            fila_1 integer,
                            columna_1 integer,
                            fila_2 integer,
                            columna_2 integer,
                            costo integer
                    )""")




def fill_dicts(path_1):

    racks = []
    for j in path_1.storage.mat:
        for i in j:
            if i.is_rack == False:
                racks.append((i.a_y,i.a_x))
    for j in path_1.storage.mat:
        for i in j:
            if i.is_cargo_bay == True:
                racks.append((i.y,i.x))

    for i in range(len(racks)):
            for j in range(len(racks)):
                if racks[i] != racks[j]:
                    #id  = '%s,%s->%s,%s'%(racks[i][0],racks[i][1],racks[j][0],racks[j][1])
                    id = '%s->%s'%(i,j)
                    path_1.starting_point = (racks[i][0],racks[i][1])
                    path_1.target = (racks[j][0],racks[j][1])
                    conexion.execute("insert into astar(n,columna_1,fila_1,columna_2,fila_2,costo) values (?,?,?,?,?,?)",
                                    (id,racks[i][1],racks[i][0],racks[j][1],racks[j][0],len(path_1.a_star())))
    conexion.commit()

fill_dicts(path1)

conexion.close()