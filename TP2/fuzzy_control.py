class Controller:
    def __init__(self) :

        self.thetha = 0
        self.w = 0
        self.force = 0
        self.a = 0 #aceleracion 
        self.thetha_f = "Z"
        self.w_f = "Z"
        self.force_f = "Z"
    
    def fuzzifier_ang (self, ang): #singleton 
        ang = (ang*180/3.14159)
        fuzzy = {}
        
        if - 90 <= ang <=-20 :
                u=1
                ang_f = "NG"
                fuzzy[ang_f] = round(u, 3)
        elif -20 < ang <= -10:
                u=(-1/10)*ang - 1
                ang_f = "NG"
                fuzzy[ang_f] = round(u, 3)
       
        if - 20 <= ang <=-10 :
                u=(1/10)*ang + 2
                ang_f = "NP"
                fuzzy[ang_f] = round(u, 3)

        elif -10 < ang <= 0:
                u=(-1/10)*ang
                ang_f = "NP"
                fuzzy[ang_f] = round(u, 3)
        
        if -10 <= ang <= 0:
            u=(1/10)*ang + 1
            ang_f = "Z"
            fuzzy[ang_f] = round(u, 3)

        elif 0 < ang <= 10:
            u=(-1/10)*ang + 1
            ang_f = "Z"
            fuzzy[ang_f] = round(u, 3)
        
        if 0 <= ang <= 10 :
            u=(1/10)*ang 
            ang_f = "PP"
            fuzzy[ang_f] = round(u, 3)

        elif 10 < ang <= 20:
            u=(-1/10)*ang + 2
            ang_f = "PP"
            fuzzy[ang_f] = round(u, 3)
        
        if 10 <= ang <=20 :
            u=(1/10)*ang - 1
            ang_f = "PG"
            fuzzy[ang_f] = round(u, 3)

        elif 20 < ang <= 90:
            u=1
            ang_f = "PG"
            fuzzy[ang_f] = round(u, 3)
        
        return fuzzy
        
    def fuzzifier_vel (self, vel):
        fuzzy = {}
        
        if - 10 <= vel <=-2 :
            uv=1
            vel_f="NG"
            fuzzy[vel_f] = uv
        elif -2 < vel <= -1:
            uv=(-1)*vel - (1)
            vel_f = "NG"
            fuzzy[vel_f] = uv

        if - 2 <= vel <=-1 :
            uv=(1)*vel + 2
            vel_f = "NP"
            fuzzy[vel_f] = uv
        elif -1 < vel <= 0:
            uv=(-1)*vel
            vel_f = "NP"
            fuzzy[vel_f] = uv
        
        if -1 <= vel <= 0:
            uv=(1)*vel + 1
            vel_f = "Z"
            fuzzy[vel_f] = uv
        elif 0 < vel <= 1:
            uv=(-1)*vel + 1
            vel_f = "Z"
            fuzzy[vel_f] = uv
        
        if 0 <= vel <= 1 :
            uv=(1)*vel
            vel_f = "PP" 
            fuzzy[vel_f] = uv
        elif 1 < vel <= 2:
            uv=(-1)*vel + 2 
            vel_f = "PP"
            fuzzy[vel_f] = uv
        
        if 1 <= vel <=2 :
            uv=(1)*vel - 1
            vel_f = "PG"
            fuzzy[vel_f] = uv
        elif 2 < vel <= 10:
            uv=1
            vel_f = "PG"
            fuzzy[vel_f] = uv

        return fuzzy
   
    def fuzzy_inference (self, fuzzy_ang, fuzzy_vel):
        

        force = {'PG':0, 'PP':0, 'Z':0, 'NP': 0, 'NG':0}

        for ang in fuzzy_ang:

            for vel in fuzzy_vel:

                value = min(fuzzy_ang[ang], fuzzy_vel[vel])

                if ((ang == "NG" and vel =="NG") or 
                    (ang == "NG" and vel =="NP") or
                    (ang == "NG" and vel =="Z")  or 
                    (ang == "NP" and vel =="NG") or 
                    (ang == "NP" and vel =="NP") or 
                    (ang == "Z"  and vel =="NG")):

                    if value >= force['NG']:

                        force['NG'] = value               
                    
                if ((ang == "NG" and vel =="PP") or 
                    (ang == "NP" and vel =="Z")  or 
                    (ang == "Z"  and vel =="NP") or 
                    (ang == "PP" and vel =="NG")):
                    
                    if value >= force['NP']:

                        force['NP'] = value
                
                if ((ang == "NG" and vel =="PG") or 
                    (ang == "NP" and vel =="PP") or 
                    (ang == "Z" and vel =="Z")   or 
                    (ang == "PP" and vel =="NP") or 
                    (ang == "PG" and vel =="NG")):
                    
                    if value >= force['Z']:

                        force['Z'] = value
                
                if ((ang == "NP" and vel =="PG") or 
                    (ang == "Z" and vel =="PP")  or 
                    (ang == "PP" and vel =="Z")  or 
                    (ang == "PG" and vel =="NP")):

                    if value >= force['PP']:

                        force['PP'] = value

                if ((ang == "PG" and vel =="PG") or 
                    (ang == "PG" and vel =="PP") or 
                    (ang == "PG" and vel =="Z")  or 
                    (ang == "PP" and vel =="PG") or 
                    (ang == "PP" and vel =="PP") or 
                    (ang == "Z" and vel =="PG")):
                    
                    if value >= force['PG']:

                        force['PG'] = value
        
        return force

    def desfuzzifier (self, force, p, g): #medio

        numerador = 0
        denominador = 0

        for i in force:

            if force[i] != 0:
                
                denominador = denominador + force[i] 
                
                if i == 'NG':
                    
                    numerador = numerador + force[i] * (-g)
                
                if i == 'NP':
                    
                    numerador = numerador + force[i] * (-p)
                
                if i == 'Z':
                    
                    numerador = numerador + force[i] * 0
                
                if i == 'PP':
                    
                    numerador = numerador + force[i] * (p)
                
                if i == 'PG':
                    
                    numerador = numerador + force[i] * (g)
        try:
            return (numerador/denominador)
        except:
            return 0
                    

        
        


