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
        AA06
        AA07
        FB01
        FB02
        FB03
        MDZ
        AEP
        COR
        SFN
        SGO
        LMA
        AFA
        AOL
        BRC
        CLX
        CNQ

        FERTILIZANTE
        TELA-GRANIZO
        COSECHADORA
        AUTOPARTES
        CACAO
        HARINA
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
        (avion AA06)
        (avion AA07)
        (avion FB01)
        (avion FB02)
        (avion FB03)

        (aeropuerto MDZ)
        (aeropuerto AEP)
        (aeropuerto COR)
        (aeropuerto SFN)
        (aeropuerto SGO)
        (aeropuerto LMA)
        (aeropuerto AFA)
        (aeropuerto AOL)
        (aeropuerto BRC)
        (aeropuerto CLX)
        (aeropuerto CNQ)

        (carga FERTILIZANTE)
        (carga TELA-GRANIZO)
        (carga COSECHADORA)
        (carga AUTOPARTES)
        (carga CACAO)
        (carga HARINA)


        (en LA01 MDZ)
        (en LA02 AEP)
        (en LA03 AOL)
        (en AA01 SFN)
        (en AA02 MDZ)
        (en AA03 AEP)
        (en AA04 CNQ)
        (en AA05 CLX)
        (en AA06 SGO)
        (en AA07 AEP)
        (en FB01 COR)
        (en FB02 AFA)
        (en FB03 BRC)

        (en FERTILIZANTE AEP)
        (en TELA-GRANIZO SFN)
        (en COSECHADORA MDZ)
        (en AUTOPARTES COR)
        (en CACAO AOL)
        (en HARINA BRC)   
    )
    (:goal 
        (and
            (en FERTILIZANTE SFN)
            (en TELA-GRANIZO MDZ)
            (en COSECHADORA COR)
            (en AUTOPARTES AEP)
            (en CACAO CLX)
            (en HARINA SGO)
        )
    )
)