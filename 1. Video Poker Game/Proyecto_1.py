import pokerGUI

def tarea(poker):
    #INICIO TAREA

    #FUNCIONES

    #FUNCIÓN A: NÚMERO DE CARTA

    def numerocarta(c):
        if c==0 or c==13 or c==26 or c==39:
            numero=1
            return numero
        elif c==1 or c==14 or c==27 or c==40:
            numero=2
            return numero
        elif c==2 or c==15 or c==28 or c==41:
            numero=3
            return numero
        elif c==3 or c==16 or c==29 or c==42:
            numero=4
            return numero
        elif c==4 or c==17 or c==30 or c==43:
            numero=5
            return numero
        elif c==5 or c==18 or c==31 or c==44:
            numero=6
            return numero
        elif c==6 or c==19 or c==32 or c==45:
            numero=7
            return numero
        elif c==7 or c==20 or c==33 or c==46:
            numero=8
            return numero
        elif c==8 or c==21 or c==34 or c==47:
            numero=9
            return numero
        elif c==9 or c==22 or c==35 or c==48:
            numero=10
            return numero
        elif c==10 or c==23 or c==36 or c==49:
            numero=11
            return numero
        elif c==11 or c==24 or c==37 or c==50:
            numero=12
            return numero
        elif c==12 or c==25 or c==38 or c==51:
            numero=13
            return numero

    #FUNCIÓN B: PINTA DE LA CARTA

    def pintacarta(x): 
        if x>=0 and x<=12:    
            pinta=1
            return pinta
        elif x>=13 and x<=25:
            pinta=2
            return pinta
        elif x>=26 and x<=38:
            pinta=3
            return pinta
        elif x>=39 and x<=51:
            pinta=4
            return pinta

    #FUNCIÓN C: LETRA DE LA PINTA

    def letracarta(w):
        if w==1:
            return "c"
        elif w==2:
            return "p"
        elif w==3:
            return "t"
        elif w==4:
            return "d"

    #FUNCIONES DE COMBINACIONES GANADORAS
    
    def escala(x,y,z,w,o):
        if (x==1 or x==2 or x==3 or x==4 or x==5) and (y==1 or y==2 or y==3 or y==4 or y==5) and (z==1 or z==2 or z==3 or z==4 or z==5) and (w==1 or w==2 or w==3 or w==4 or w==5) and (o==1 or o==2 or o==3 or o==4 or o==5):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==2 or x==3 or x==4 or x==5 or x==6) and (y==2 or y==3 or y==4 or y==5 or y==6) and (z==2 or z==3 or z==4 or z==5 or z==6)and (w==2 or w==3 or w==4 or w==5 or w==6)and(o==2 or o==3 or o==4 or o==5 or o==6):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==3 or x==4 or x==5 or x==6 or x==7) and (y==3 or y==4 or y==5 or y==6 or y==7) and (z==3 or z==4 or z==5 or z==6 or z==7)and (w==3 or w==4 or w==5 or w==6 or w==7)and(o==3 or o==4 or o==5 or o==6 or o==7):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==4 or x==5 or x==6 or x==7 or x==8) and (y==4 or y==5 or y==6 or y==7 or y==8) and (z==4 or z==5 or z==6 or z==7 or z==8)and (w==4 or w==5 or w==6 or w==7 or w==8)and(o==4 or o==5 or o==6 or o==7 or o==8):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==5 or x==6 or x==7 or x==8 or x==9) and (y==5 or y==6 or y==7 or y==8 or y==9) and (z==5 or z==6 or z==7 or z==8 or z==9)and (w==5 or w==6 or w==7 or w==8 or w==9)and(o==5 or o==6 or o==7 or o==8 or o==9):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==6 or x==7 or x==8 or x==9 or x==10) and (y==6 or y==7 or y==8 or y==9 or y==10) and (z==6 or z==7 or z==8 or z==9 or z==10)and (w==6 or w==7 or w==8 or w==9 or w==10)and(o==6 or o==7 or o==8 or o==9 or o==10):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==7 or x==8 or x==9 or x==10 or x==11) and (y==7 or y==8 or y==9 or y==10 or y==11) and (z==7 or z==8 or z==9 or z==10 or z==11)and (w==7 or w==8 or w==9 or w==10 or w==11)and(o==7 or o==8 or o==9 or o==10 or o==11):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==8 or x==9 or x==10 or x==11 or x==12) and (y==8 or y==9 or y==10 or y==11 or y==12) and (z==8 or z==9 or z==10 or z==11 or z==12)and (w==8 or w==9 or w==10 or w==11 or w==12)and(o==8 or o==9 or o==10 or o==11 or o==12):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==9 or x==10 or x==11 or x==12 or x==13) and (y==9 or y==10 or y==11 or y==12 or y==13) and (z==9 or z==10 or z==11 or z==12 or z==13)and (w==9 or w==10 or w==11 or w==12 or w==13)and(o==9 or o==10 or o==11 or o==12 or o==13):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==10 or x==11 or x==12 or x==13 or x==1) and (y==10 or y==11 or y==12 or y==13 or y==1) and (z==10 or z==11 or z==12 or z==13 or z==1)and (w==10 or w==11 or w==12 or w==13 or w==1)and(o==10 or o==11 or o==12 or o==13 or o==1):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==11 or x==12 or x==13 or x==1 or x==2) and (y==11 or y==12 or y==13 or y==1 or y==2) and (z==11 or z==12 or z==13 or z==1 or z==2)and (w==11 or w==12 or w==13 or w==1 or w==2)and(o==11 or o==12 or o==13 or o==1 or o==2):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==12 or x==13 or x==1 or x==2 or x==3) and (y==12 or y==13 or y==1 or y==2 or y==3) and (z==12 or z==13 or z==1 or z==2 or z==3)and (w==12 or w==13 or w==1 or w==2 or w==3)and(o==12 or o==13 or o==1 or o==2 or o==3):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False
        elif (x==13 or x==1 or x==2 or x==3 or x==4) and (y==13 or y==1 or y==2 or y==3 or y==4) and (z==13 or z==1 or z==2 or z==3 or z==4)and (w==13 or w==1 or w==2 or w==3 or w==4)and(o==13 or o==1 or o==2 or o==3 or o==4):
            if x!=y and x!=z and x!=w and x!=o and y!=z and y!=w and y!=o and z!=w and z!=o and w!=o:
                return True
            else:
                return False

    def pokerface(x,y,z,w,o):
        if (x==y and y==z and z==w) or (x==y and y==z and z==o) or (x==y and y==w and w==o) or (x==z and z==w and w==o) or (y==z and z==w and w==o):
            return True
        else:
            return False

    def fullhouse(x,y,z,w,o):
        if x==w and w==o and y==z:
            return True
        elif x==z and z==w and y==o:
            return True
        elif x==z and z==o and y==w:
            return True
        elif x==y and y==w and z==o:
            return True
        elif x==y and y==o and z==w:
            return True
        elif x==y and y==z and w==o:
            return True
        elif z==w and w==o and x==y:
            return True
        elif y==z and z==w and x==o:
            return True
        elif y==z and z==o and w==x:
            return True
        elif y==w and w==o and x==z:
            return True
        else:
            return False

    def color(x,y,z,w,o):
        if x==y and y==z and z==w and w==o:
            return True
        else:
            return False
        
    def trio(x,y,z,w,o):
        if x==w and w==o:
            return True
        elif x==z and z==w:
            return True
        elif x==z and z==o:
            return True
        elif x==y and y==w:
            return True
        elif x==y and y==o:
            return True
        elif x==y and y==z:
            return True
        elif z==w and w==o:
            return True
        elif y==z and z==w:
            return True
        elif y==z and z==o:
            return True
        elif y==w and w==o:
            return True
        else:
            return False

    def dospares(x,y,z,w,o):
        if x==o and (z==w or y==w or y==z):
            return True
        elif x==w and(y==z or y==o or z==o):
            return True
        elif x==z and (y==w or y==o or w==o):
            return True
        elif x==y and (z==w or z==o or w==o):
            return True
        elif y==z and (x==w or x==o or w==o):
            return True
        elif y==w and (x==z or z==o or x==o):
            return True
        elif y==o and (x==z or x==w or z==w):
            return True
        elif z==w and (x==y or x==o or y==o):
            return True
        elif z==o and (x==y or x==w or y==w):
            return True
        elif w==o and (x==y or x==z or y==z):
            return True
        else:
            return False 

    def unpar(x,y,z,w,o):
        if x==o:
            return True
        elif x==w:
            return True
        elif x==z:
            return True
        elif x==y:
            return True
        elif y==z:
            return True
        elif y==w:
            return True
        elif y==o:
            return True
        elif z==w:
            return True
        elif z==o:
            return True
        elif w==o:
            return True
        else:
            return False

    #FUNCIÓN DE DUPLICAR PREMIOS DUP

    def dup(c,k,a,p,q,r,s,t,d):
        dup=1
        if c<k:
            if a==1:
                dup=p*2
                d=dup+d
                return d
            elif a==2:
                dup=q*2
                d=dup+d
                return d
            elif a==3:
                dup=r*2
                d=dup+d
                return d
            elif a==4:
                dup=s*2
                d=dup+d
                return d
            elif a==5:
                dup=t*2
                d=d+dup
                return d
        elif c==k:
            if a==1:
                d=d+p
                return d
            elif a==2:
                d=d+q
                return d
            elif a==3:
                d=d+r
                return d
            elif a==4:
                d=d+s
                return d
            elif a==5:
                d=d+t
                return d
        elif c>k:
            d=d-a
            return d

    #FUNCIÓN DE NO DUP (OPCIÓN NO DUPLICAR PREMIO)

    def dupfalse(a,d,p,q,r,s,t):
        if a==1:
            d=d+p
            return d
        elif a==2:
            d=d+q
            return d
        elif a==3:
            d=d+r
            return d
        elif a==4:
            d=d+s
            return d
        elif a==5:
            d=d+t
            return d

    credito=1000

    while credito>0:
        
        poker.llenarMazo()

        if credito==0:
            poker.alerta('¡Adiós! Juego terminado')
            poker.terminar()

        poker.cambiarCarta(0,'base')
        poker.cambiarCarta(1,'base')
        poker.cambiarCarta(2,'base')
        poker.cambiarCarta(3,'base')
        poker.cambiarCarta(4,'base')
        
        c1=poker.sacarCarta() 
        c2=poker.sacarCarta()
        c3=poker.sacarCarta()
        c4=poker.sacarCarta()
        c5=poker.sacarCarta()

        apuesta=1
        poker.cambiarApuesta(1)

        a=10 
        b=20
        c=30
        d=40
        e=50

        #PARTE 1: BIENVENIDA Y APUESTAS

        poker.alerta('¡Bienvenido a Video Poker! :)')

        poker.alerta('Selecciona apostar uno o apuesta máxima para apostar fichas y deal para continuar')

        poker.cambiarCredito(credito)

        poker.mensaje('Video Poker')

        juego=poker.esperarClick()

        while juego!=7:
            if juego==6:
                apuesta=5
                poker.cambiarApuesta(apuesta)
            if juego==5:
                apuesta=apuesta+1
                poker.cambiarApuesta(apuesta)
                if apuesta>5:
                    apuesta=5
                    poker.cambiarApuesta(apuesta)
            juego=poker.esperarClick()

        if juego==7:
            poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))
            poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
            poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
            poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
            poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
        apuesta1=apuesta

        #PARTE 2: SELECCIÓN DE CARTAS E INTERCAMBIO

        poker.alerta('Selecciona tus cartas con cuidado. Una vez que lo hagas, la decisión será definitiva.')
    
        juego=poker.esperarClick()
    
        while juego!=7 or juego!=6 or juego!=5:
            if juego==0:
                a=0
                poker.cambiarTextoEnCarta(0,"Cambiar")
                juego=poker.esperarClick()
            elif juego==1:
                b=1
                poker.cambiarTextoEnCarta(1,"Cambiar")
                juego=poker.esperarClick()
            elif juego==2:
                c=2
                poker.cambiarTextoEnCarta(2,"Cambiar")
                juego=poker.esperarClick()
            elif juego==3:
                d=3
                poker.cambiarTextoEnCarta(3,"Cambiar")
                juego=poker.esperarClick()
            elif juego==4:
                e=4
                poker.cambiarTextoEnCarta(4,"Cambiar")
                juego=poker.esperarClick()
            if juego==7:
                break

        if juego==7:
            poker.alerta('Tus cartas serán cambiadas.')
            if a==0:
                c1=poker.sacarCarta() 
                poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))                
                poker.cambiarTextoEnCarta(a,"")
            if b==1:
                c2=poker.sacarCarta() 
                poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
                poker.cambiarTextoEnCarta(b,"")
            if c==2:
                c3=poker.sacarCarta() 
                poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
                poker.cambiarTextoEnCarta(c,"")
            if d==3:
                c4=poker.sacarCarta() 
                poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
                poker.cambiarTextoEnCarta(d,"")
            if e==4:
                c5=poker.sacarCarta() 
                poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
                poker.cambiarTextoEnCarta(e,"")

        # PARTE 3: PREMIOS

        # CHEQUIAR SI HAY COMBINACIONES GANADORAS
	
        credito2=credito

        itdup=0

        itsum=0

        pozo=0

        if (pintacarta(c1)==pintacarta(c2)) and (pintacarta(c2)==pintacarta(c3)) and (pintacarta(c3)==pintacarta(c4)) and (pintacarta(c4)==pintacarta(c5)) and (escala(numerocarta(c1),numerocarta(c2),numerocarta(c3),numerocarta(c4),numerocarta(c5))==True):
            poker.alerta('Tienes una escala a color!')
            jota=False
            while jota==False:
                credito1=credito
                preg=poker.preguntar('Te gustaría duplicar tu premio?')
                if preg==True:
                    c1=poker.sacarCarta()
                    c2=poker.sacarCarta()
                    c3=poker.sacarCarta()
                    c4=poker.sacarCarta()
                    c5=poker.sacarCarta()
                    poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))
                    poker.cambiarCarta(1,'base')
                    poker.cambiarCarta(2,'base')
                    poker.cambiarCarta(3,'base')
                    poker.cambiarCarta(4,'base')
                    poker.alerta('Selecciona solo una de las cartas cubiertas')
                    juego=poker.esperarClick()
                    if juego==1:
                        poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c2)),apuesta,50,100,150,200,350,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c2)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c2)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(50*itdup*2)+(50*itsum)
                        elif apuesta1==2:
                            pozo=(100*itdup*2)+(100*itsum)
                        elif apuesta1==3:
                            pozo=(150*itdup*2)+(150*itsum)
                        elif apuesta1==4:
                            pozo=(200*itdup*2)+(200*itsum)
                        elif apuesta1==5:
                            pozo=(350*itdup*2)+(350*itsum)
                    elif juego==2:
                        poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c3)),apuesta,50,100,150,200,350,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c3)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c3)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(50*itdup*2)+(50*itsum)
                        elif apuesta1==2:
                            pozo=(100*itdup*2)+(100*itsum)
                        elif apuesta1==3:
                            pozo=(150*itdup*2)+(150*itsum)
                        elif apuesta1==4:
                            pozo=(200*itdup*2)+(200*itsum)
                        elif apuesta1==5:
                            pozo=(350*itdup*2)+(350*itsum)
                    elif juego==3:
                        poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c4)),apuesta,50,100,150,200,350,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c4)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c4)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(50*itdup*2)+(50*itsum)
                        elif apuesta1==2:
                            pozo=(100*itdup*2)+(100*itsum)
                        elif apuesta1==3:
                            pozo=(150*itdup*2)+(150*itsum)
                        elif apuesta1==4:
                            pozo=(200*itdup*2)+(200*itsum)
                        elif apuesta1==5:
                            pozo=(350*itdup*2)+(350*itsum)
                    elif juego==4:
                        poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c5)),apuesta,50,100,150,200,350,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c5)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c5)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(50*itdup*2)+(50*itsum)
                        elif apuesta1==2:
                            pozo=(100*itdup*2)+(100*itsum)
                        elif apuesta1==3:
                            pozo=(150*itdup*2)+(150*itsum)
                        elif apuesta1==4:
                            pozo=(200*itdup*2)+(200*itsum)
                        elif apuesta1==5:
                            pozo=(350*itdup*2)+(350*itsum)
                elif preg==False:
                    if pozo==0:
                        credito=(dupfalse(apuesta,credito,50,100,150,200,350))
                        poker.cambiarCredito(credito)
                    elif pozo!=0:
                        credito=credito1
                        poker.cambiarCredito(credito)
                    jota=True
                if (credito+apuesta1)==credito1:
                        jota=True
                        poker.alerta('Has perdido el doble o nada')
                        if pozo!=0:
                            credito=credito-pozo
                            poker.cambiarCredito(credito)       
        elif pokerface(numerocarta(c1), numerocarta(c2),numerocarta(c3),numerocarta(c4),numerocarta(c5))==True:
            poker.alerta('Tienes una combinación de Poker!')
            jota=False
            while jota==False:
                credito1=credito
                preg2=poker.preguntar('Te gustaría duplicar tu premio?')
                if preg2==True:
                    c1=poker.sacarCarta()
                    c2=poker.sacarCarta()
                    c3=poker.sacarCarta()
                    c4=poker.sacarCarta()
                    c5=poker.sacarCarta()
                    poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))
                    poker.cambiarCarta(1,'base')
                    poker.cambiarCarta(2,'base')
                    poker.cambiarCarta(3,'base')
                    poker.cambiarCarta(4,'base')
                    poker.alerta('Selecciona solo una de las cartas cubiertas')
                    juego=poker.esperarClick()
                    if juego==1:
                        poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c2)),apuesta,25,50,75,100,125,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c2)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c2)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(25*itdup*2)+(25*itsum)
                        elif apuesta1==2:
                            pozo=(50*itdup*2)+(50*itsum)
                        elif apuesta1==3:
                            pozo=(75*itdup*2)+(75*itsum)
                        elif apuesta1==4:
                            pozo=(100*itdup*2)+(100*itsum)
                        elif apuesta1==5:
                            pozo=(125*itdup*2)+(125*itsum)
                    elif juego==2:
                        poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c3)),apuesta,25,50,75,100,125,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c3)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c3)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(25*itdup*2)+(25*itsum)
                        elif apuesta1==2:
                            pozo=(50*itdup*2)+(50*itsum)
                        elif apuesta1==3:
                            pozo=(75*itdup*2)+(75*itsum)
                        elif apuesta1==4:
                            pozo=(100*itdup*2)+(100*itsum)
                        elif apuesta1==5:
                            pozo=(125*itdup*2)+(125*itsum)
                    elif juego==3:
                        poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c4)),apuesta,25,50,75,100,125,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c4)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c4)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(25*itdup*2)+(25*itsum)
                        elif apuesta1==2:
                            pozo=(50*itdup*2)+(50*itsum)
                        elif apuesta1==3:
                            pozo=(75*itdup*2)+(75*itsum)
                        elif apuesta1==4:
                            pozo=(100*itdup*2)+(100*itsum)
                        elif apuesta1==5:
                            pozo=(125*itdup*2)+(125*itsum)
                    elif juego==4:
                        poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c5)),apuesta,25,50,75,100,125,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c5)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c5)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(25*itdup*2)+(25*itsum)
                        elif apuesta1==2:
                            pozo=(50*itdup*2)+(50*itsum)
                        elif apuesta1==3:
                            pozo=(75*itdup*2)+(75*itsum)
                        elif apuesta1==4:
                            pozo=(100*itdup*2)+(100*itsum)
                        elif apuesta1==5:
                            pozo=(125*itdup*2)+(125*itsum)
                elif preg2==False:
                    if pozo==0:
                        credito=(dupfalse(apuesta,credito,25,50,75,100,125))
                        poker.cambiarCredito(credito)
                    elif pozo!=0:
                        credito=credito1
                        poker.cambiarCredito(credito)
                    jota=True
                if (credito+apuesta1)==credito1:
                        jota=True
                        poker.alerta('Has perdido el doble o nada')
                        if pozo!=0:
                            credito=credito-pozo
                            poker.cambiarCredito(credito)    
        elif fullhouse(numerocarta(c1), numerocarta(c2),numerocarta(c3),numerocarta(c4),numerocarta(c5))==True:
            poker.alerta('Tienes una combinación Full House!')
            jota=False
            while jota==False:
                credito1=credito
                preg3=poker.preguntar('Te gustaría duplicar tu premio?')
                if preg3==True:
                    c1=poker.sacarCarta()
                    c2=poker.sacarCarta()
                    c3=poker.sacarCarta()
                    c4=poker.sacarCarta()
                    c5=poker.sacarCarta()
                    poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))
                    poker.cambiarCarta(1,'base')
                    poker.cambiarCarta(2,'base')
                    poker.cambiarCarta(3,'base')
                    poker.cambiarCarta(4,'base')
                    poker.alerta('Selecciona solo una de las cartas cubiertas')
                    juego=poker.esperarClick()
                    if juego==1:
                        poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c2)),apuesta,9,18,27,36,45,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c2)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c2)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(9*itdup*2)+(9*itsum)
                        elif apuesta1==2:
                            pozo=(18*itdup*2)+(18*itsum)
                        elif apuesta1==3:
                            pozo=(27*itdup*2)+(27*itsum)
                        elif apuesta1==4:
                            pozo=(36*itdup*2)+(36*itsum)
                        elif apuesta1==5:
                            pozo=(45*itdup*2)+(45*itsum)
                    elif juego==2:
                        poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c3)),apuesta,9,18,27,36,45,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c3)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c3)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(9*itdup*2)+(9*itsum)
                        elif apuesta1==2:
                            pozo=(18*itdup*2)+(18*itsum)
                        elif apuesta1==3:
                            pozo=(27*itdup*2)+(27*itsum)
                        elif apuesta1==4:
                            pozo=(36*itdup*2)+(36*itsum)
                        elif apuesta1==5:
                            pozo=(45*itdup*2)+(45*itsum)
                    elif juego==3:
                        poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c4)),apuesta,9,18,27,36,45,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c4)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c4)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(9*itdup*2)+(9*itsum)
                        elif apuesta1==2:
                            pozo=(18*itdup*2)+(18*itsum)
                        elif apuesta1==3:
                            pozo=(27*itdup*2)+(27*itsum)
                        elif apuesta1==4:
                            pozo=(36*itdup*2)+(36*itsum)
                        elif apuesta1==5:
                            pozo=(45*itdup*2)+(45*itsum)
                    elif juego==4:
                        poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c5)),apuesta,9,18,27,36,45,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c5)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c5)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(9*itdup*2)+(9*itsum)
                        elif apuesta1==2:
                            pozo=(18*itdup*2)+(18*itsum)
                        elif apuesta1==3:
                            pozo=(27*itdup*2)+(27*itsum)
                        elif apuesta1==4:
                            pozo=(36*itdup*2)+(36*itsum)
                        elif apuesta1==5:
                            pozo=(45*itdup*2)+(45*itsum)
                elif preg3==False:
                    if pozo==0:
                        credito=(dupfalse(apuesta,credito,9,18,27,36,45))
                        poker.cambiarCredito(credito)
                    elif pozo!=0:
                        credito=credito1
                        poker.cambiarCredito(credito)
                    jota=True
                if (credito+apuesta1)==credito1:
                        jota=True
                        poker.alerta('Has perdido el doble o nada')
                        if pozo!=0:
                            credito=credito-pozo
                            poker.cambiarCredito(credito)
        elif color(pintacarta(c1),pintacarta(c2),pintacarta(c3),pintacarta(c4),pintacarta(c5))==True:
            poker.alerta('Tienes una combinación de color!')
            jota=False
            while jota==False:
                credito1=credito
                preg4=poker.preguntar('Te gustaría duplicar tu premio?')
                if preg4==True:
                    c1=poker.sacarCarta()
                    c2=poker.sacarCarta()
                    c3=poker.sacarCarta()
                    c4=poker.sacarCarta()
                    c5=poker.sacarCarta()
                    poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))
                    poker.cambiarCarta(1,'base')
                    poker.cambiarCarta(2,'base')
                    poker.cambiarCarta(3,'base')
                    poker.cambiarCarta(4,'base')
                    poker.alerta('Selecciona solo una de las cartas cubiertas')
                    juego=poker.esperarClick()
                    if juego==1:
                        poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c2)),apuesta,6,12,18,24,30,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c2)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c2)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==2:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==3:
                            pozo=(18*itdup*2)+(18*itsum)
                        elif apuesta1==4:
                            pozo=(24*itdup*2)+(24*itsum)
                        elif apuesta1==5:
                            pozo=(30*itdup*2)+(30*itsum)
                    elif juego==2:
                        poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c3)),apuesta,6,12,18,24,30,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c3)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c3)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==2:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==3:
                            pozo=(18*itdup*2)+(18*itsum)
                        elif apuesta1==4:
                            pozo=(24*itdup*2)+(24*itsum)
                        elif apuesta1==5:
                            pozo=(30*itdup*2)+(30*itsum)
                    elif juego==3:
                        poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c4)),apuesta,6,12,18,24,30,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c4)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c4)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==2:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==3:
                            pozo=(18*itdup*2)+(18*itsum)
                        elif apuesta1==4:
                            pozo=(24*itdup*2)+(24*itsum)
                        elif apuesta1==5:
                            pozo=(30*itdup*2)+(30*itsum)
                    elif juego==4:
                        poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c5)),apuesta,6,12,18,24,30,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c5)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c5)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==2:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==3:
                            pozo=(18*itdup*2)+(18*itsum)
                        elif apuesta1==4:
                            pozo=(24*itdup*2)+(24*itsum)
                        elif apuesta1==5:
                            pozo=(30*itdup*2)+(30*itsum)
                elif preg4==False:
                    if pozo==0:
                        credito=(dupfalse(apuesta,credito,6,12,18,24,30))
                        poker.cambiarCredito(credito)
                    elif pozo!=0:
                        credito=credito1
                        poker.cambiarCredito(credito)
                    jota=True
                if (credito+apuesta1)==credito1:
                        jota=True
                        poker.alerta('Has perdido el doble o nada')
                        if pozo!=0:
                            credito=credito-pozo
                            poker.cambiarCredito(credito)
        elif escala(numerocarta(c1),numerocarta(c2),numerocarta(c3),numerocarta(c4),numerocarta(c5))==True:
            poker.alerta('Tienes una escala!')
            jota=False
            while jota==False:
                credito1=credito
                preg5=poker.preguntar('Te gustaría duplicar tu premio?')
                if preg5==True:
                    c1=poker.sacarCarta()
                    c2=poker.sacarCarta()
                    c3=poker.sacarCarta()
                    c4=poker.sacarCarta()
                    c5=poker.sacarCarta()
                    poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))
                    poker.cambiarCarta(1,'base')
                    poker.cambiarCarta(2,'base')
                    poker.cambiarCarta(3,'base')
                    poker.cambiarCarta(4,'base')
                    poker.alerta('Selecciona solo una de las cartas cubiertas')
                    juego=poker.esperarClick()
                    if juego==1:
                        poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c2)),apuesta,4,8,12,16,20,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c2)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c2)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==2:
                            pozo=(8*itdup*2)+(8*itsum)
                        elif apuesta1==3:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==4:
                            pozo=(16*itdup*2)+(16*itsum)
                        elif apuesta1==5:
                            pozo=(20*itdup*2)+(20*itsum)
                    elif juego==2:
                        poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c3)),apuesta,4,8,12,16,20,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c3)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c3)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==2:
                            pozo=(8*itdup*2)+(8*itsum)
                        elif apuesta1==3:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==4:
                            pozo=(16*itdup*2)+(16*itsum)
                        elif apuesta1==5:
                            pozo=(20*itdup*2)+(20*itsum)
                    elif juego==3:
                        poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c4)),apuesta,4,8,12,16,20,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c4)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c4)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==2:
                            pozo=(8*itdup*2)+(8*itsum)
                        elif apuesta1==3:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==4:
                            pozo=(16*itdup*2)+(16*itsum)
                        elif apuesta1==5:
                            pozo=(20*itdup*2)+(20*itsum)
                    elif juego==4:
                        poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c5)),apuesta,4,8,12,16,20,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c5)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c5)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==2:
                            pozo=(8*itdup*2)+(8*itsum)
                        elif apuesta1==3:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==4:
                            pozo=(16*itdup*2)+(16*itsum)
                        elif apuesta1==5:
                            pozo=(20*itdup*2)+(20*itsum)
                elif preg5==False:
                    if pozo==0:
                        credito=(dupfalse(apuesta,credito,4,8,12,16,20))
                        poker.cambiarCredito(credito)
                    elif pozo!=0:
                        credito=credito1
                        poker.cambiarCredito(credito)
                    jota=True
                if (credito+apuesta1)==credito1:
                        jota=True
                        poker.alerta('Has perdido el doble o nada')
                        if pozo!=0:
                            credito=credito-pozo
                            poker.cambiarCredito(credito)
        elif trio(numerocarta(c1),numerocarta(c2),numerocarta(c3),numerocarta(c4),numerocarta(c5))==True:
            poker.alerta('Tienes un trío!')
            jota=False
            while jota==False:
                credito1=credito
                preg6=poker.preguntar('Te gustaría duplicar tu premio?')
                if preg6==True:
                    c1=poker.sacarCarta()
                    c2=poker.sacarCarta()
                    c3=poker.sacarCarta()
                    c4=poker.sacarCarta()
                    c5=poker.sacarCarta()
                    poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))
                    poker.cambiarCarta(1,'base')
                    poker.cambiarCarta(2,'base')
                    poker.cambiarCarta(3,'base')
                    poker.cambiarCarta(4,'base')
                    poker.alerta('Selecciona solo una de las cartas cubiertas')
                    juego=poker.esperarClick()
                    if juego==1:
                        poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c2)),apuesta,3,6,9,12,15,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c2)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c2)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(3*itdup*2)+(3*itsum)
                        elif apuesta1==2:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==3:
                            pozo=(9*itdup*2)+(9*itsum)
                        elif apuesta1==4:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==5:
                            pozo=(15*itdup*2)+(15*itsum)
                    elif juego==2:
                        poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c3)),apuesta,3,6,9,12,15,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c3)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c3)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(3*itdup*2)+(3*itsum)
                        elif apuesta1==2:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==3:
                            pozo=(9*itdup*2)+(9*itsum)
                        elif apuesta1==4:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==5:
                            pozo=(15*itdup*2)+(15*itsum)
                    elif juego==3:
                        poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c4)),apuesta,3,6,9,12,15,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c4)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c4)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(3*itdup*2)+(3*itsum)
                        elif apuesta1==2:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==3:
                            pozo=(9*itdup*2)+(9*itsum)
                        elif apuesta1==4:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==5:
                            pozo=(15*itdup*2)+(15*itsum)
                    elif juego==4:
                        poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c5)),apuesta,3,6,9,12,15,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c5)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c5)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(3*itdup*2)+(3*itsum)
                        elif apuesta1==2:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==3:
                            pozo=(9*itdup*2)+(9*itsum)
                        elif apuesta1==4:
                            pozo=(12*itdup*2)+(12*itsum)
                        elif apuesta1==5:
                            pozo=(15*itdup*2)+(15*itsum)
                elif preg6==False:
                    if pozo==0:
                        credito=(dupfalse(apuesta,credito,3,6,9,12,15))
                        poker.cambiarCredito(credito)
                    elif pozo!=0:
                        credito=credito1
                        poker.cambiarCredito(credito)
                    jota=True
                if (credito+apuesta1)==credito1:
                        jota=True
                        poker.alerta('Has perdido el doble o nada')
                        if pozo!=0:
                            credito=credito-pozo
                            poker.cambiarCredito(credito)
        elif dospares(numerocarta(c1),numerocarta(c2),numerocarta(c3),numerocarta(c4),numerocarta(c5))==True:
            poker.alerta('Tienes dos pares!')
            jota=False
            while jota==False:
                credito1=credito
                preg7=poker.preguntar('Te gustaría duplicar tu premio?')
                if preg7==True:
                    c1=poker.sacarCarta()
                    c2=poker.sacarCarta()
                    c3=poker.sacarCarta()
                    c4=poker.sacarCarta()
                    c5=poker.sacarCarta()
                    poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))
                    poker.cambiarCarta(1,'base')
                    poker.cambiarCarta(2,'base')
                    poker.cambiarCarta(3,'base')
                    poker.cambiarCarta(4,'base')
                    poker.alerta('Selecciona solo una de las cartas cubiertas')
                    juego=poker.esperarClick()
                    if juego==1:
                        poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c2)),apuesta,2,4,6,8,10,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c2)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c2)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(2*itdup*2)+(2*itsum)
                        elif apuesta1==2:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==3:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==4:
                            pozo=(8*itdup*2)+(8*itsum)
                        elif apuesta1==5:
                            pozo=(10*itdup*2)+(10*itsum)
                    elif juego==2:
                        poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c3)),apuesta,2,4,6,8,10,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c3)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c3)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(2*itdup*2)+(2*itsum)
                        elif apuesta1==2:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==3:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==4:
                            pozo=(8*itdup*2)+(8*itsum)
                        elif apuesta1==5:
                            pozo=(10*itdup*2)+(10*itsum)
                    elif juego==3:
                        poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c4)),apuesta,2,4,6,8,10,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c4)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c4)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(2*itdup*2)+(2*itsum)
                        elif apuesta1==2:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==3:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==4:
                            pozo=(8*itdup*2)+(8*itsum)
                        elif apuesta1==5:
                            pozo=(10*itdup*2)+(10*itsum)
                    elif juego==4:
                        poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c5)),apuesta,2,4,6,8,10,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c5)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c5)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(2*itdup*2)+(2*itsum)
                        elif apuesta1==2:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==3:
                            pozo=(6*itdup*2)+(6*itsum)
                        elif apuesta1==4:
                            pozo=(8*itdup*2)+(8*itsum)
                        elif apuesta1==5:
                            pozo=(10*itdup*2)+(10*itsum)
                elif preg7==False:
                    if pozo==0:
                        credito=(dupfalse(apuesta,credito,2,4,6,8,10))
                        poker.cambiarCredito(credito)
                    elif pozo!=0:
                        credito=credito1
                        poker.cambiarCredito(credito)
                    jota=True
                if (credito+apuesta1)==credito1:
                        jota=True
                        poker.alerta('Has perdido el doble o nada')
                        if pozo!=0:
                            credito=credito-pozo
                            poker.cambiarCredito(credito)
        elif unpar(numerocarta(c1),numerocarta(c2),numerocarta(c3),numerocarta(c4),numerocarta(c5))==True:
            poker.alerta('Tienes un par!')
            jota=False
            while jota==False:
                credito1=credito
                preg8=poker.preguntar('Te gustaría duplicar tu premio?')
                if preg8==True:
                    c1=poker.sacarCarta()
                    c2=poker.sacarCarta()
                    c3=poker.sacarCarta()
                    c4=poker.sacarCarta()
                    c5=poker.sacarCarta()
                    poker.cambiarCarta(0,str(numerocarta(c1))+letracarta(pintacarta(c1)))
                    poker.cambiarCarta(1,'base')
                    poker.cambiarCarta(2,'base')
                    poker.cambiarCarta(3,'base')
                    poker.cambiarCarta(4,'base')
                    poker.alerta('Selecciona solo una de las cartas cubiertas')
                    juego=poker.esperarClick()
                    if juego==1:
                        poker.cambiarCarta(1,str(numerocarta(c2))+letracarta(pintacarta(c2)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c2)),apuesta,1,2,3,4,5,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c2)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c2)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(1*itdup*2)+(1*itsum)
                        elif apuesta1==2:
                            pozo=(2*itdup*2)+(2*itsum)
                        elif apuesta1==3:
                            pozo=(3*itdup*2)+(3*itsum)
                        elif apuesta1==4:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==5:
                            pozo=(5*itdup*2)+(5*itsum)
                    elif juego==2:
                        poker.cambiarCarta(2,str(numerocarta(c3))+letracarta(pintacarta(c3)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c3)),apuesta,1,2,3,4,5,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c3)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c3)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(1*itdup*2)+(1*itsum)
                        elif apuesta1==2:
                            pozo=(2*itdup*2)+(2*itsum)
                        elif apuesta1==3:
                            pozo=(3*itdup*2)+(3*itsum)
                        elif apuesta1==4:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==5:
                            pozo=(5*itdup*2)+(5*itsum)
                    elif juego==3:
                        poker.cambiarCarta(3,str(numerocarta(c4))+letracarta(pintacarta(c4)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c4)),apuesta,1,2,3,4,5,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c4)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c4)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(1*itdup*2)+(1*itsum)
                        elif apuesta1==2:
                            pozo=(2*itdup*2)+(2*itsum)
                        elif apuesta1==3:
                            pozo=(3*itdup*2)+(3*itsum)
                        elif apuesta1==4:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==5:
                            pozo=(5*itdup*2)+(5*itsum)
                    elif juego==4:
                        poker.cambiarCarta(4,str(numerocarta(c5))+letracarta(pintacarta(c5)))
                        credito=(dup((numerocarta(c1)),(numerocarta(c5)),apuesta,1,2,3,4,5,credito))
                        poker.cambiarCredito(credito)
                        if numerocarta(c5)>numerocarta(c1):
                            itdup=itdup+1
                        elif numerocarta(c5)==numerocarta(c1):
                            itsum=1+itsum
                        if apuesta1==1:
                            pozo=(1*itdup*2)+(1*itsum)
                        elif apuesta1==2:
                            pozo=(2*itdup*2)+(2*itsum)
                        elif apuesta1==3:
                            pozo=(3*itdup*2)+(3*itsum)
                        elif apuesta1==4:
                            pozo=(4*itdup*2)+(4*itsum)
                        elif apuesta1==5:
                            pozo=(5*itdup*2)+(5*itsum)
                elif preg8==False:
                    if pozo==0:
                        credito=(dupfalse(apuesta,credito,1,2,3,4,5))
                        poker.cambiarCredito(credito)
                    elif pozo!=0:
                        credito=credito1
                        poker.cambiarCredito(credito)
                    jota=True
                if (credito+apuesta1)==credito1:
                        jota=True
                        poker.alerta('Has perdido el doble o nada')
                        if pozo!=0:
                            credito=credito-pozo
                            poker.cambiarCredito(credito)
        else:
            poker.alerta('Has perdido :(')
            apuesta=1
            if pozo==0:
                credito=credito-apuesta1
                poker.cambiarCredito(credito)

    #FIN TAREA

app = pokerGUI.Application(None)
app.title('Video Poker')
app.loadProgram(tarea)
app.start()
