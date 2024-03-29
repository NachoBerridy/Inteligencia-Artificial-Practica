(define (problem carga-aerea)
    (:domain aviones)
    (:objects 
        LA01
        LA02
        LA03
        AA01
        AA02
        AA03
        AA04
        AA05
        FB01
        FB02
        FB03
        MDZ
        AEP
        COR
        SFN




        FERTILIZANTE
        TELA-GRANIZO
        COSECHADORA
        AUTOPARTES

    )
    (:init 

        (avion LA01)
        (avion LA02)
        (avion LA03)
        (avion AA01)
        (avion AA02)
        (avion AA03)
        (avion AA04)
        (avion AA05)

        (avion FB01)
        (avion FB02)
        (avion FB03)

        (aeropuerto MDZ)
        (aeropuerto AEP)
        (aeropuerto COR)
        (aeropuerto SFN)


        (carga FERTILIZANTE)
        (carga TELA-GRANIZO)
        (carga COSECHADORA)
        (carga AUTOPARTES)



        (en LA01 MDZ)
        (en LA02 AEP)
        (en LA03 MDZ)
        (en AA01 SFN)
        (en AA02 MDZ)
        (en AA03 AEP)
        (en AA04 MDZ)
        (en AA05 AEP)
        (en FB01 COR)
        (en FB02 AEP)
        (en FB03 SFN)

        (en FERTILIZANTE AEP)
        (en TELA-GRANIZO SFN)
        (en COSECHADORA MDZ)
        (en AUTOPARTES COR)
  
    )
    (:goal 
        (and
            (en FERTILIZANTE SFN)
            (en TELA-GRANIZO MDZ)
            (en COSECHADORA COR)
            (en AUTOPARTES AEP)

        )
    )
)