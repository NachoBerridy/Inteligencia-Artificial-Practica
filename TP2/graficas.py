import matplotlib.pyplot as plt

def graficar_ang():

    fuzzy = {'NG':[], 'NP':[], 'Z':[], 'PP':[], 'PG':[]}
    a = []
    for ang in range(-90, 90): 
        a.append(ang)
        if - 90 <= ang <=-20 :
                u=1
                ang_f = "NG"
                fuzzy[ang_f].append(round(u, 3))
        elif -20 < ang <= -10:
                u=(-1/10)*ang - 1
                ang_f = "NG"
                fuzzy[ang_f].append(round(u, 3))
        else:
                ang_f = "NG"
                fuzzy[ang_f].append(0)

        if - 20 <= ang <=-10 :
                u=(1/10)*ang + 2
                ang_f = "NP"
                fuzzy[ang_f].append(round(u, 3))
        elif -10 < ang <= 0:
                u=(-1/10)*ang
                ang_f = "NP"
                fuzzy[ang_f].append(round(u, 3))
        else:
                ang_f = "NP"
                fuzzy[ang_f].append(0)
        
        if -10 <= ang <= 0:
            u=(1/10)*ang + 1
            ang_f = "Z"
            fuzzy[ang_f].append(round(u, 3))
        elif 0 < ang <= 10:
            u=(-1/10)*ang + 1
            ang_f = "Z"
            fuzzy[ang_f].append(round(u, 3))
        else:
                ang_f = "Z"
                fuzzy[ang_f].append(0)
        
        if 0 <= ang <= 10 :
            u=(1/10)*ang 
            ang_f = "PP"
            fuzzy[ang_f].append(round(u, 3))
        elif 10 < ang <= 20:
            u=(-1/10)*ang + 2
            ang_f = "PP"
            fuzzy[ang_f].append(round(u, 3))
        else:
                ang_f = "PP"
                fuzzy[ang_f].append(0)
        
        if 10 <= ang <=20 :
            u=(1/10)*ang - 1
            ang_f = "PG"
            fuzzy[ang_f].append(round(u, 3))
        elif 20 < ang <= 90:
            u=1
            ang_f = "PG"
            fuzzy[ang_f].append(round(u, 3))
        else:
                ang_f = "PG"
                fuzzy[ang_f].append(0)
        
    fig , ax = plt.subplots()




    ax.plot(a, fuzzy['PG'], label = 'PG')
    ax.plot(a, fuzzy['PP'], label = 'PP')
    ax.plot(a, fuzzy['Z'] , label = 'Z')
    ax.plot(a, fuzzy['NG'], label = 'NG')
    ax.plot(a, fuzzy['NP'], label = 'NP')
    ax.set(xlabel = 'theta (°)', ylabel = 'Pertenencia al conjunto difuso')
    ax.grid()
    ax.legend()
    plt.title('Funcion de pertencia para theta')
    plt.show()

def graficar_vel():

    fuzzy = {'NG':[], 'NP':[], 'Z':[], 'PP':[], 'PG':[]}
    v = []
    for vel in range(-100, 100): 
        v.append(vel)
        if - 100 <= vel <=-20 :
                u=1
                vel_f = "NG"
                fuzzy[vel_f].append(round(u, 3))
        elif -20 < vel <= -10:
                u=(-1/10)*vel - 1
                vel_f = "NG"
                fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "NG"
                fuzzy[vel_f].append(0)

        if - 20 <= vel <=-10 :
                u=(1/10)*vel + 2
                vel_f = "NP"
                fuzzy[vel_f].append(round(u, 3))
        elif -10 < vel <= 0:
                u=(-1/10)*vel
                vel_f = "NP"
                fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "NP"
                fuzzy[vel_f].append(0)
        
        if -10 <= vel <= 0:
            u=(1/10)*vel + 1
            vel_f = "Z"
            fuzzy[vel_f].append(round(u, 3))
        elif 0 < vel <= 10:
            u=(-1/10)*vel + 1
            vel_f = "Z"
            fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "Z"
                fuzzy[vel_f].append(0)
        
        if 0 <= vel <= 10 :
            u=(1/10)*vel 
            vel_f = "PP"
            fuzzy[vel_f].append(round(u, 3))
        elif 10 < vel <= 20:
            u=(-1/10)*vel + 2
            vel_f = "PP"
            fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "PP"
                fuzzy[vel_f].append(0)
        
        if 10 <= vel <=20 :
            u=(1/10)*vel - 1
            vel_f = "PG"
            fuzzy[vel_f].append(round(u, 3))
        elif 20 < vel <= 100:
            u=1
            vel_f = "PG"
            fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "PG"
                fuzzy[vel_f].append(0)
        
    fig , ax = plt.subplots()

def graficar_vel():

    fuzzy = {'NG':[], 'NP':[], 'Z':[], 'PP':[], 'PG':[]}
    v = []
    for vel in range(-10, 10): 
        v.append(vel)
        if - 10 <= vel <=-5 :
                u=1
                vel_f = "NG"
                fuzzy[vel_f].append(round(u, 3))
        elif -5 < vel <= -1:
                u=(-1/4)*vel - (1/4)
                vel_f = "NG"
                fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "NG"
                fuzzy[vel_f].append(0)

        if - 2 <= vel <=-1 :
                u=(1)*vel + 2
                vel_f = "NP"
                fuzzy[vel_f].append(round(u, 3))
        elif -1 < vel <= 0:
                u=(-1)*vel
                vel_f = "NP"
                fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "NP"
                fuzzy[vel_f].append(0)
        
        if -1 <= vel <= 0:
            u=(1)*vel + 1
            vel_f = "Z"
            fuzzy[vel_f].append(round(u, 3))
        elif 0 < vel <= 1:
            u=(-1)*vel + 1
            vel_f = "Z"
            fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "Z"
                fuzzy[vel_f].append(0)
        
        if 0 <= vel <= 1 :
            u=(1)*vel 
            vel_f = "PP"
            fuzzy[vel_f].append(round(u, 3))
        elif 1 < vel <= 2:
            u=(-1)*vel + 2
            vel_f = "PP"
            fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "PP"
                fuzzy[vel_f].append(0)
        
        if 1 <= vel <=5 :
            u=(1/4)*vel - (1/4)
            vel_f = "PG"
            fuzzy[vel_f].append(round(u, 3))
        elif 5 < vel <= 10:
            u=1
            vel_f = "PG"
            fuzzy[vel_f].append(round(u, 3))
        else:
                vel_f = "PG"
                fuzzy[vel_f].append(0)
        
    fig , ax = plt.subplots()





    ax.plot(v, fuzzy['PG'], label = 'PG')
    ax.plot(v, fuzzy['PP'], label = 'PP')
    ax.plot(v, fuzzy['Z'] , label = 'Z')
    ax.plot(v, fuzzy['NG'], label = 'NG')
    ax.plot(v, fuzzy['NP'], label = 'NP')
    ax.set(xlabel = 'velocidad (rad/s)', ylabel = 'Pertenencia al conjunto difuso')
    ax.grid()
    ax.legend()
    plt.title('Funcion de pertencia para velocidad')
    plt.show()



graficar_ang()
graficar_vel()