(define (problem capp-pieza)
    (:domain capp)
    (:objects 
        orientacion_x_mas
        orientacion_y_mas
        orientacion_z_mas
        orientacion_x_menos
        orientacion_y_menos
        orientacion_z_menos

        arriba
        abajo

        izquierda
        derecha
        centro

        f1
        f2
        f3
        f4
        f5
        f6
        f7
        f8
        f9
        f10
        f11
        f12

        slotA
        slotB
        slotC
        through-hole
        blind-hole
        
        fresado
        taladrado
        torneado

        taladro
        torno
        fresadora

    )
    (:init 
        (orientacion orientacion_x_mas)
        (orientacion orientacion_y_mas)
        (orientacion orientacion_z_mas)
        (orientacion orientacion_x_menos)
        (orientacion orientacion_y_menos)
        (orientacion orientacion_z_menos)

        (altura arriba)
        (altura abajo)

        (lado centro)
        (lado derecha)
        (lado izquierda)

        (feature f1)
        (feature f2)
        (feature f3)
        (feature f4)
        (feature f5)
        (feature f6)
        (feature f7)
        (feature f8)
        (feature f9)
        (feature f10)
        (feature f11)
        (feature f12)
        
        (tipo slotA)
        (tipo slotB)
        (tipo slotC)
        (tipo through-hole)
        (tipo blind-hole)
        
        (operacion fresado)
        (operacion taladrado)
        (operacion torneado)

        (herramienta fresadora)
        (herramienta taladro)
        (herramienta torno)

        
        (orientacion-pieza orientacion_x_menos)
        (lado-pieza izquierda)

        (herramienta-actual fresadora)
        (herramienta-altura arriba)

        (feature-tipo f1 slotA)
        (lado-feature f1 derecha)
        (altura-feature f1 arriba)
        (orientacion-feature f1 orientacion_x_mas)
        
        (feature-tipo f2 slotA)
        (lado-feature f2 izquierda)
        (altura-feature f2 arriba)
        (orientacion-feature f2 orientacion_x_menos)
        
        (feature-tipo f3 slotA)
        (lado-feature f3 derecha)
        (altura-feature f3 abajo)
        (orientacion-feature f3 orientacion_x_mas)
        
        (feature-tipo f4 slotB)
        (lado-feature f4 centro)
        (altura-feature f4 arriba)
        (orientacion-feature f4 orientacion_z_mas)
        
        (feature-tipo f5 slotC)
        (lado-feature f5 centro)
        (altura-feature f5 arriba)
        (orientacion-feature f5 orientacion_z_mas)
        
        (feature-tipo f6 blind-hole)
        (lado-feature f6 centro)
        (altura-feature f6 arriba)
        (orientacion-feature f6 orientacion_z_mas)
        
        (feature-tipo f7 through-hole)
        (lado-feature f7 derecha)
        (altura-feature f7 arriba)
        (orientacion-feature f7 orientacion_z_mas)
        
        (feature-tipo f8 through-hole)
        (lado-feature f8 izquierda)
        (altura-feature f8 arriba)
        (orientacion-feature f8 orientacion_z_mas)
        
        (feature-tipo f9 through-hole)
        (lado-feature f9 izquierda)
        (altura-feature f9 arriba)
        (orientacion-feature f9 orientacion_x_mas)
        
        (feature-tipo f10 through-hole)
        (lado-feature f10 derecha)
        (altura-feature f10 arriba)
        (orientacion-feature f10 orientacion_x_mas)
        
        (feature-tipo f11 through-hole)
        (lado-feature f11 izquierda)
        (altura-feature f11 arriba)
        (orientacion-feature f11 orientacion_x_mas)
        
        (feature-tipo f12 through-hole)
        (lado-feature f12 derecha)
        (altura-feature f12 arriba)
        (orientacion-feature f12 orientacion_x_mas)


        (fabricable slotA fresado)
        (fabricable slotB fresado)
        (fabricable slotC fresado)

        (fabricable through-hole taladrado)
        (fabricable blind-hole taladrado)

        (herramienta-necesaria taladrado taladro)
        (herramienta-necesaria torneado torno)
        (herramienta-necesaria fresado fresadora)
    )
    (:goal 
        (and
            (fabricada f2)
            (fabricada f3)
            (fabricada f4)
            (fabricada f6)
            (fabricada f7)
            (fabricada f8)
            (fabricada f9)
            (fabricada f10)
            
        )
    )
)