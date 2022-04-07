from lib.escenario import Escenario
import random

# ··· ··· ··· ETAPA 1: Definición de clases adicionales ··· ··· ···

# CLASE A : HEROE

class Heroe(object): 
    """ atributos: self.heroe_x, con las coordenadas "x" en pixeles """
    """ // self.heroe_y, con las coordenadas "y" en pixeles """
    """ // self.heroe_x_cuadro y self.heroe_y_cuadro son las coordenadas "x" e "y" en cuadros"""
    def __init__(self,heroe_x,heroe_y):
        self.heroe_x = heroe_x
        self.heroe_y = heroe_y
        

# CLASE B: SERPIENTES
        
class Serpiente(object): # Clase para las serpientes
    """ atributos: como el heroe, self.serpiente_x con coordenadas "x" en pixeles, y lo mismo para "y" (serpiente_y)"""
    """ self.marca se usa para marcar los puntos de dominación. Identifica a la serpiente que esta esperando para dominar """
    """ un PD del heroe . """
    """ // self.id describe el id personal de la serpiente """
    def __init__(self,serpiente_x,serpiente_y):
        self.serpiente_x = serpiente_x 
        self.serpiente_y = serpiente_y 
        self.marca = 0 # esta variable se usa para marcar los PD

    def identificar(self,id):
        self.id = id
        

# CLASE C: PUNTOS DE DOMINACION O PD EN ESTE CODIGO

class Punto(object): # Clase para los puntos de dominación (PD). 
    """ atributos: self.punto_x y self.punto_y, describen coordenadas "x" e "y" en cuadros """
    """ // Además, self.estado describe el estado en que se encuentra el PD. Si es 0, no ha sido dominado. """
    """ Si es 1, es dominado por el heroe. Si es 2, es dominado por la serpiente. """
    """ // Por último, self.id refleja el id del punto. """
    def __init__(self,punto_x,punto_y):
        self.punto_x = punto_x
        self.punto_y = punto_y
        self.estado = 0
        self.marca = 0

    def identificar(self,id):
        self.id = id

# CLASE D: MUROS

class Muro(object):
    """ atributos: self.muro_x y self.muro_y describen las coordinadas "x" e "y" en cuadros. """
    def __init__(self,muro_x,muro_y):
        self.muro_x = muro_x
        self.muro_y = muro_y
        

# CLASE E: TIMER INTERNO

# Este timer, interno, se utiliza para contar los segundos transcurridos cuando el heroe se queda en un PD de las serpientes o
# viceversa.  

class Timer(object):
    """ atributos: tiene un timer_heroe para contar los segundos cuando el heroe se posiciona en un PD de una serpiente. """
    """ // timer_serpiente es lo mismo, aplicado a las serpientes."""
    """ // self.timer_aparicion_item es un atributo aleatorio que indica el tiempo al que se debe llegar para crear un """
    """ item aleatorio, en una posición aleatoria """
    """ // self.llegando_a_timer_item es un atributo que va aumentando en función de la variable segundos, hasta alcanzar"""
    """ el valor de self.timer_aparicion_item. """
    def __init__(self):
        self.timer_heroe = 0
        self.timer_serpiente = 0
        self.timer_aparicion_item = random.randint(0,20)
        self.llegando_a_timer_item = 0

# CLASE F: ITEM PATITA (0)

class Item_Patita(object):
    """ atributos: esta clase describe el item o premio de la patita. tiene un atributo self.creado, que es -1 si el """
    """ item o power-up no ha sido creado. Cambia a 10 cuando se crea. """
    """ // self. id, el segundo atributo, describe el id que identifica al objeto. """
    """ // por ultimo, self.coordenada es un atributo que es una lista, que describe el set [x,y] donde esta el item, si ha sido creado"""
    def __init__(self):
        self.creado = -1 # -1 es que no ha sido creado el item. 10 es que se ha creado
        self.coordenada = []

    def identificar(self,id):
        self.id = id

# NOTA: la clase G y la H se comportan de la misma manera que la anterior. 

# CLASE G: ITEM SSC (1)

class Item_SSC(object):
    """ atributos: el item ssc tiene algunos atributos que lo distinguen de la clase Item_Patita."""
    """ /// self.timer y self.timer2 marcan el tiempo desde que el heroe o la serpiente tocaron el premio hasta que"""
    """ el premio desaparece. self.timer es del heroe y self.timer2 es de la serpiente."""
    """ /// self.marca indica por quien fue tomado el premio ssc. 1 es del heroe y 2 es de la serpiente."""
    def __init__(self):
        self.creado = -1 # -1 es que no ha sido creado el item
        self.coordenada = []
        self.timer = 0
        self.timer2 = 0
        self.marca = 0

    def identificar(self,id):
        self.id = id

# CLASE H: ITEM BANDERA (2)

class Item_Bandera(object):
    """ atributos: como esta clase lidia con velocidades al igual que Item_SSC, los atributos y sus descripciones son idénticas """
    """ en concepto, porque hay una sutil diferencia."""
    """ self.timer describe el efecto del heroe sobre las serpientes (no se usará para el propio heroe como en el item SSC). """
    """ Así mismo, self.timer2 describirá el efecto de las serpientes sobre el heroe. """
    """ En cuanto a self.marca, sigue siendo igual - 1 para el heroe, y 2 para la serpiente. """
    def __init__(self):
        self.creado = -1 # -1 es que no ha sido creado el item
        self.coordenada = []
        self.timer = 0
        self.timer2 = 0
        self.marca = 0

    def identificar(self,id):
        self.id = id

# CLASE I: CONTADOR DE PUNTOS

class Cuenta_Puntos():
    """ atributos: esta clase se usa como un contador de los puntos acumulados por el heroe (self.gana_heroe)"""
    """ y las serpientes (self.gana_serpiente) """
    def __init__(self):
        self.gana_serpiente = 0
        self.gana_heroe = 0

# ··· ··· ··· ETAPA 2: La clase Juego ··· ··· ···

class Juego():
    """ atributos: self.escario es el atributo que vincula la librería escenario al objeto juego"""
    """ // self.ancho_mapa guarda el ancho de mapa en INT y self.alto_mapa el alto en INT, respectivamente """
    """ // los personajes del juego se tratan como objetos en listas multidimensionales. Las listas respectivas """
    """ son self.objetos_muro, self.objetos_pd, self.objetos_serpiente. En el caso del heroe como solo interesa sus """
    """ coordenadas "x" e "y", los atributos del objeto JUEGO son self.hero_x y self.hero_y respectivamente """
    """ /// self.timer es el atributo de timer interno de un objeto de la clase juego. Se usará para la dominación de PD del heroe """
    """ /// self.contador_serpiente y self.contador_heroe son los que variaran con el tiempo para los PDs. Estos son """
    """ distinto al timer, porque estos modifican sus atributos. Los contadores toman valores. """
    """ /// self.patita, self.ssc y self.bandera son los atributos que reflejan los items del juego"""
    """ // self.posiciones, es una lista con las posiciones activas que persigue la serpiente. Incluye items, Pds y el heroe"""
    """ /// self.item es una lista con las posiciones donde se puede crear un item, ya sea patita, ssc o bandera. """
    """ /// self. item_creado es un indicador general de si hay items creados o no. 0 = creado, -1 = no creado."""
    """ /// self.gana es un atributo interno que va contando los puntos acumulados por las serpientes y el heroe """
    """ /// en "despierta" se define un nuevo atributo variable, self.intento_dominacion, para que el heroe, si quiere """
    """ dominar un PD que ya es de una serpiente, tenga obligadamente que quedarse en el casillero 3 segundos. Si se sale,"""
    """ la cantidad de tiempo que llevaba ahi se vuelve 0. """
    """ /// la ultima variable creada fue self.coordenadas_pd, para almacenar las coordendas [x,y] de los pd. Esto es """
    """ importante para los ciclos en cuanto a dominación de PDs."""
    def __init__(self): 

        #***************** PARTE 0: CREAR EL OBJETO JUEGO COMO UN ESCENARIO Y CONTADORES *************
        
        escenario = Escenario(self)
        self.escenario = escenario #guardo el escenario como atributo
        
        self.contador_serpiente = 0
        self.contador_heroe = 0
        self.item_creado = -1 # -1, porque no se ha creado items

        #***************** PARTE 1: LEER LOS ARCHIVOS DE MAPAS **************************

        # Fase 1: buscar el mapa  ···················

        mapas_para_jugar = ['mapas\mapa1.txt','mapas\mapa2.txt','mapas\mapa3.txt']
        i = random.randint(0,2)
        nombre_mapa = mapas_para_jugar[i]
        mapa = open(nombre_mapa) # Aqui se abre el mapa, ya se puede leer. 
        
        lineas_mapa = mapa.readlines() # Se guardan las lineas en una lista, viene en formato string.
        mapa.close() # Se cierra el archivo

        # Fase 2: atributos de medida ················

        medidas = lineas_mapa[0].split(',') # Aqui genero una sublista con la coordenada "x" e "y"
        
        ancho_mapa = medidas[0]
        alto_mapa = medidas[1]

        ancho_mapa = ancho_mapa.split() # Esto es para sacar los \n
        alto_mapa = alto_mapa.split()

        self.ancho_mapa = int(ancho_mapa[0]) #Aqui se guardan como atributos
        self.alto_mapa = int(alto_mapa[0])

        # Fase 3: posiciones iniciales EN CUADROS ·····

        cuenta_fila = -1 
        cuenta_columna = -1 # estos dos son contadores que permiten hacer el ciclo para extraer las coordenadas iniciales 

        coordenadas_iniciales_heroe = []
        coordenadas_iniciales_serpientes = []
        coordenadas_iniciales_pd = []
        coordenadas_iniciales_muros = []
        
        for linea in lineas_mapa: # esto seria cada linea (es decir, columna)
            cuenta_fila = -1 # lo reseteo para cada fila
            for car in linea: # cada linea es un string
                cuenta_fila = cuenta_fila+1
                if car == 'e': # hay solo 1 heroe
                    posicion_heroe_x_inicial = cuenta_fila
                    posicion_heroe_y_inicial = cuenta_columna
                    lista_heroe = []
                    lista_heroe.append(int(posicion_heroe_x_inicial))
                    lista_heroe.append(int(posicion_heroe_y_inicial))
                    coordenadas_iniciales_heroe.append(lista_heroe)
                if car == 's':
                    posicion_serpiente_x = cuenta_fila
                    posicion_serpiente_y = cuenta_columna
                    lista_serpiente = []
                    lista_serpiente.append(int(posicion_serpiente_x))
                    lista_serpiente.append(int(posicion_serpiente_y))
                    coordenadas_iniciales_serpientes.append(lista_serpiente)
                if car == 'd':
                    posicion_pd_x = cuenta_fila
                    posicion_pd_y = cuenta_columna
                    lista_pd = []
                    lista_pd.append(int(posicion_pd_x))
                    lista_pd.append(int(posicion_pd_y))
                    coordenadas_iniciales_pd.append(lista_pd)
                if car == 'x':
                    posicion_muro_x = cuenta_fila
                    posicion_muro_y = cuenta_columna
                    lista_muro = []
                    lista_muro.append(int(posicion_muro_x))
                    lista_muro.append(int(posicion_muro_y))
                    coordenadas_iniciales_muros.append(lista_muro)
            cuenta_columna = cuenta_columna+1

        escenario.configura_tamanio(self.ancho_mapa,self.alto_mapa)
        self.coordenadas_muro = coordenadas_iniciales_muros
        self.coordenadas_pd = coordenadas_iniciales_pd

        #******************* PARTE 2: CREANDO LOS PERSONAJES ************************

        # OBJETIVO: formar listas de objetos o, para el heroe, crear el objeto heroe

        #Fase 1: muros ································

        objetos_muro = []

        for muro in coordenadas_iniciales_muros: # una sublista de la forma [x,y] EN CUADROS
            coordenada_x = muro[0]
            coordenada_y = muro[1]
            muro_creado = Muro(coordenada_x,coordenada_y)
            objetos_muro.append(muro_creado)
            escenario.construye_muro(muro_creado.muro_x,muro_creado.muro_y)

        self.objetos_muro = objetos_muro # lista de objetos muro

        # Fase 2: heroe ·······························

        # hacemos conversion a coordenadas en pixeles

        heroe = Heroe(((coordenadas_iniciales_heroe[0][0])*32),((coordenadas_iniciales_heroe[0][1])*32))
        escenario.crea_heroe(heroe.heroe_x,heroe.heroe_y,"male")
        self.hero_x = heroe.heroe_x
        self.hero_y = heroe.heroe_y
        self.intento_dominacion = 0

        # Fase 3: puntos de dominacion ·················

        objetos_pd = []

        for pd in coordenadas_iniciales_pd: # una sublista de la forma [x,y] EN CUADROS
            coordenada_x = pd[0]
            coordenada_y = pd[1]
            pd = Punto(coordenada_x,coordenada_y)
            id = escenario.crea_punto_dominacion(pd.punto_x,pd.punto_y)
            pd.identificar(id)
            objetos_pd.append(pd)
            
        self.objetos_pd = objetos_pd

        # Fase 4: serpientes ····························

        objetos_serpiente = []

        for serpiente in coordenadas_iniciales_serpientes: # sublista de la forma [x,y] EN CUADROS
            coordenada_x = serpiente[0]
            coordenada_y = serpiente[1]
            baby_serpiente = Serpiente(coordenada_x*32,coordenada_y*32) # coordenadas en cuadros
            id = escenario.crea_serpiente((baby_serpiente.serpiente_x),(baby_serpiente.serpiente_y))
            baby_serpiente.identificar(id)
            objetos_serpiente.append(baby_serpiente)

        self.objetos_serpiente = objetos_serpiente

        # Fase 5: Construccion del timer interno ········

        self.timer = Timer() # un identificador de contador de tiempo para el heroe

        # Fase 6: Construccion de los objetos de item ··········

        self.patita = Item_Patita()
        self.ssc = Item_SSC()
        self.bandera = Item_Bandera ()

        # Fase 7: Construccion de los contadores de puntos ········

        self.gana = Cuenta_Puntos()

        #******************* PARTE 3: BANNERS ************************

        escenario.set_etapa(i+1)
        escenario.set_puntos_enemigo(0)
        escenario.set_puntos_jugador(0)
        escenario.set_mensaje(" Serpientes: Hey, cabezón naranjo! Ni se te ocurra tocar los círculos D ni nuestros tesoros!\n Héroe: Tengo que tener cuidado ... sólo así podré salir!! ")
        
    def despierta(self,segundos):

        # ********************** PARTE 1: MOVIENDO AL HEROE *************************************

        y_antiguo_heroe = self.hero_y #en pixeles, no cuadritos
        x_antiguo_heroe = self.hero_x #en pixeles, no cuadritos
        
        if self.escenario.esta_presionada("Up"):
            if self.ssc.timer!=0 and self.ssc.timer<=12: #piso el premio
                self.hero_y = self.hero_y - 360*segundos
            if self.bandera.timer2 !=0:
                self.hero_y = self.hero_y - 90*segundos
            else:
                self.hero_y = self.hero_y - 200*segundos
            
        if self.escenario.esta_presionada("Down"):
            if self.ssc.timer!=0 and self.ssc.timer<=12: #piso el premio
                self.hero_y = self.hero_y + 360*segundos
            if self.bandera.timer2 != 0:
                self.hero_y = self.hero_y + 90*segundos
            else:
                self.hero_y = self.hero_y + 200*segundos

        if self.escenario.esta_presionada("Right"):
            if self.ssc.timer!=0 and self.ssc.timer<=12: #piso el premio
                self.hero_x = self.hero_x + 360*segundos
            if self.bandera.timer2 !=0:
                self.hero_x = self.hero_x + 90*segundos
            else:
                self.hero_x = self.hero_x + 200*segundos
            
        if self.escenario.esta_presionada("Left"):
            if self.ssc.timer != 0 and self.ssc.timer<=12:
                self.hero_x = self.hero_x - 360*segundos
            if self.bandera.timer2 !=0:
                self.hero_x = self.hero_x - 90*segundos
            else:
                self.hero_x = self.hero_x - 200*segundos

        cuadro_x = int((self.hero_x+15.4)//32)
        cuadro_y = int((self.hero_y+28)//32)
        coordenada_heroe_cuadros = [cuadro_x, cuadro_y]
                                
        if coordenada_heroe_cuadros not in self.coordenadas_muro:
            self.escenario.mueve_heroe(self.hero_x,self.hero_y)
        else:
            self.hero_x = x_antiguo_heroe
            self.hero_y = y_antiguo_heroe

        # ********************** PARTE 2: MOVIENDO SERPIENTES **********************************

        # Fase 1: lista de posiciones pd ················

        lista_posiciones = []

        for pd in self.objetos_pd: #aqui cada PD va a representarse por un par [x,y]
            if pd.estado == 0 or (pd.estado == 1 and self.contador_serpiente == 0):
                x = (pd.punto_x)*32
                y = (pd.punto_y)*32
                coordenada = []
                coordenada.append(x)
                coordenada.append(y)
                lista_posiciones.append(coordenada)

        # Fase 2: lista de posiciones heroe ·············
        
        lista_heroe = [self.hero_x,self.hero_y]
        lista_posiciones.append(lista_heroe)

        # Fase 3: lista de posiciones de items ··········

        if self.patita.creado!= -1: #osea, si esta creada
            lista_patita = []
            lista_patita.append(self.patita.coordenada[0]*32)
            lista_patita.append(self.patita.coordenada[1]*32)
            lista_posiciones.append(lista_patita)
        if self.ssc.creado!= -1 and self.ssc.timer2 == 0 and self.ssc.marca == 0: #tiene que ser igual a 0, para no estar activado.
            lista_ssc = []
            lista_ssc.append(self.ssc.coordenada[0]*32)
            lista_ssc.append(self.ssc.coordenada[1]*32)
            lista_posiciones.append(lista_ssc)
        if self.bandera.creado!= -1 and self.bandera.marca ==0: #estar creado y no ser dominado por nadie (no está activado)
            lista_bandera = []
            lista_bandera.append(self.bandera.coordenada[0]*32)
            lista_bandera.append(self.bandera.coordenada[1]*32)
            lista_posiciones.append(lista_bandera)
           
        self.posiciones = lista_posiciones # lista con numeros. Por fluidez de la serpiente se trabaja con pixeles

        # Fase 4: distancia más corta con pixeles ········

        for serpiente in self.objetos_serpiente:
            x_serpiente_antiguo = serpiente.serpiente_x # esto en pixeles
            y_serpiente_antiguo = serpiente.serpiente_y
            if self.contador_serpiente > 0 and self.contador_serpiente < 3 and serpiente.marca == 2: #es decir, si quiere dominar un PD del heroe
                serpiente.serpiente_x = x_serpiente_antiguo
                serpiente.serpiente_y = y_serpiente_antiguo
            if self.contador_serpiente == 0: # si el timer está en 0
                serpiente.marca = 0
            lista_distancias = [] # esta lista incluirá las distancias diagonales que persigue la serpiente
            lista_objetivo = [] # en esta lista, vinculo las distancias a sus coordenadas de la forma [x,y]
            for objetivo in self.posiciones: # ahora las comparo con el objetivo
                objetivo_x = objetivo[0] #la coordenada de mi objetivo en PIXELES!!!!!!!!
                objetivo_y = objetivo[1]
                diff_x = abs(objetivo_x - serpiente.serpiente_x)
                diff_y = abs(objetivo_y - serpiente.serpiente_y) # sacamos pitágoras
                suma = ((diff_x)**2) + ((diff_y)**2)
                suma = suma**(1/2) # obtengo la distancia diagonal
                lista_distancias.append(suma) # pongo la distancia diagonal en la lista
                lista_mini_objetivo = [] # aqui voy a vincular la distancia a un set de coordenadas [x,y] en el mismo indice
                lista_mini_objetivo.append(objetivo_x)
                lista_mini_objetivo.append(objetivo_y) 
                lista_objetivo.append(lista_mini_objetivo) # tengo la lista de objetivo final de la serpiente
            destino = min(lista_distancias) # aqui obtengo la distancia mas corta, debo ligarla a una coordenada [x,y]
            i = -1
            for elemento in lista_distancias:# con esto obtengo el indice, y el indice para mi sublista
                i = i+1
                if elemento == destino:
                    break
            objective = lista_objetivo.pop(i) #aqui tengo el objetivo, es una mini lista [x,y] EN PIXELES
            objective_x = objective[0] #la coordenada objetivo X de la serpiente EN PIXEL
            objective_y = objective[1] #la coordenada objetivo Y de la serpiente EN PIXEL

            if serpiente.serpiente_x < (objective_x):
                if self.ssc.timer2 !=0:
                    serpiente.serpiente_x = serpiente.serpiente_x + 210*segundos
                if self.bandera.timer !=0: # cuando esta causando efecto el heroe
                    serpiente.serpiente_x = serpiente.serpiente_x + 20*segundos #baja en 10
                else:
                    serpiente.serpiente_x = serpiente.serpiente_x + 110*segundos
            if serpiente.serpiente_x > (objective_x):
                if self.ssc.timer2!=0:
                    serpiente.serpiente_x = serpiente.serpiente_x - 210*segundos
                if self.bandera.timer != 0:
                    serpiente.serpiente_x = serpiente.serpiente_x - 20*segundos
                else:
                    serpiente.serpiente_x = serpiente.serpiente_x - 110*segundos
            if serpiente.serpiente_y > (objective_y):
                if self.ssc.timer2!=0:
                    serpiente.serpiente_y = serpiente.serpiente_y - 210*segundos
                if self.bandera.timer != 0 :
                    serpiente.serpiente_y = serpiente.serpiente_y - 20*segundos
                else:
                    serpiente.serpiente_y = serpiente.serpiente_y - 110*segundos
            if serpiente.serpiente_y < (objective_y):
                if self.ssc.timer2!=0:
                    serpiente.serpiente_y = serpiente.serpiente_y + 210*segundos
                if self.bandera.timer != 0:
                    serpiente.serpiente_y = serpiente.serpiente_y + 20*segundos
                else:
                    serpiente.serpiente_y = serpiente.serpiente_y + 110*segundos

        # Fase 5: que no choque con un muro, pds e items ··············

            x_serpiente_cuadro = int((serpiente.serpiente_x+14.5)//32)
            y_serpiente_cuadro = int((serpiente.serpiente_y+14.5)//32)
            coordenada_serpiente_cuadros = [x_serpiente_cuadro, y_serpiente_cuadro]

            for pd in self.objetos_pd:
                if (x_serpiente_cuadro == pd.punto_x) and (y_serpiente_cuadro == pd.punto_y) and (pd.estado==1):
                    self.timer.timer_serpiente = 1
                
            if self.timer.timer_serpiente == 1:
                self.contador_serpiente = self.contador_serpiente + segundos
                if self.contador_serpiente > 3:
                    for pd in self.objetos_pd:
                        if (pd.estado == 1) and (pd.marca==2): #en proceso de ser dominado por la serpiente
                            self.escenario.cambia_punto_dominacion(pd.id, 2) #este si resulta
                            pd.estado = 2
                            self.gana.gana_serpiente = self.gana.gana_serpiente + 1
                            self.gana.gana_heroe = self.gana.gana_heroe - 1
                            self.escenario.set_puntos_enemigo(self.gana.gana_serpiente)
                            self.escenario.set_puntos_jugador(self.gana.gana_heroe)
                            self.contador_serpiente = 0
                            self.timer.timer_serpiente = 0

            if (coordenada_serpiente_cuadros not in self.coordenadas_muro) and (serpiente.marca==0):
                if serpiente.serpiente_x != objective_x:
                    self.escenario.mueve_serpiente(serpiente.id,serpiente.serpiente_x,serpiente.serpiente_y)
                elif serpiente.serpiente_y != objective_y:
                    self.escenario.mueve_serpiente(serpiente.id,serpiente.serpiente_x,serpiente.serpiente_y)
            else:
                serpiente.serpiente_x = x_serpiente_antiguo
                serpiente.serpiente_y = y_serpiente_antiguo

        # ********************** PARTE 3: CAMBIANDO PD'S **************************************

        for pd in self.objetos_pd:
            for serpiente in self.objetos_serpiente: # pds de las serpientes
                x_serpiente_cuadro = int((serpiente.serpiente_x+14.5)//32)
                y_serpiente_cuadro = int((serpiente.serpiente_y+14.5)//32)
                if (pd.punto_x == x_serpiente_cuadro) and (pd.punto_y == y_serpiente_cuadro):
                    if pd.estado == 0: #tomado por nadie
                        self.escenario.cambia_punto_dominacion(pd.id,2)
                        pd.estado = 2 # el caso que, si ya es rojo, no interesa para la serpiente
                        self.gana.gana_serpiente = self.gana.gana_serpiente + 1
                        self.escenario.set_puntos_enemigo(self.gana.gana_serpiente)
                    if pd.estado == 1: # si esta tomado por el heroe
                        pd.marca = 2 # es de la serpiente
                        serpiente.marca = 2 # identificamos la serpiente especifica que la marco
            if (pd.punto_x == cuadro_x) and (pd.punto_y == cuadro_y): # pds del heroe
                if pd.estado == 0:
                    self.escenario.cambia_punto_dominacion(pd.id, 1) 
                    pd.estado = 1
                    self.gana.gana_heroe = self.gana.gana_heroe +1
                    self.escenario.set_puntos_jugador(self.gana.gana_heroe)
                if pd.estado == 2: # si esta tomado por la serpiente
                    pd.marca = 1

        coordenadas_del_heroe = [cuadro_x, cuadro_y]

        if coordenadas_del_heroe in self.coordenadas_pd: #esta parado en un punto de dominacion
            self.intento_dominacion = 1
            self.contador_heroe = self.contador_heroe + segundos
            self.timer.timer_heroe = 1
        else:
            self.intento_dominacion = 0
            self.contador_heroe = 0
            self.timer.timer_heroe = 0
                
        if self.intento_dominacion == 1 and self.contador_heroe!=0: #mientras se mantenga esto
            if self.contador_heroe > 3:
                for pd in self.objetos_pd:
                    if pd.estado == 2 and pd.marca == 1 and coordenadas_del_heroe in self.coordenadas_pd: #tomado por la serpiente y yo intentando atraparlo
                        self.escenario.cambia_punto_dominacion(pd.id, 1)
                        pd.estado = 1
                        self.gana.gana_heroe = self.gana.gana_heroe + 1
                        self.gana.gana_serpiente = self.gana.gana_serpiente - 1
                        self.escenario.set_puntos_enemigo(self.gana.gana_serpiente)
                        self.escenario.set_puntos_jugador(self.gana.gana_heroe)
                        self.contador_heroe = 0
                        self.timer.timer_heroe = 0
                        self.intento_dominacion = 0

        # ********************** PARTE 4: ITEMS *************************************

        # Fase 1: posiciones a no ocupar ················

        posiciones_no_ocupar = []
        for pd in self.objetos_pd: #este esta en cuadritos
            sublist = []
            sublist.append(pd.punto_x)
            sublist.append(pd.punto_y)
            posiciones_no_ocupar.append(sublist)
        for serpiente in self.objetos_serpiente: #hacemos conversion a cuadros
            x_serpiente_cuadro = int((serpiente.serpiente_x+14.5)//32)
            y_serpiente_cuadro = int((serpiente.serpiente_y+14.5)//32)
            sublist = []
            sublist.append(x_serpiente_cuadro)
            sublist.append(y_serpiente_cuadro)
            posiciones_no_ocupar.append(sublist)
        for muro in self.objetos_muro: # en cuadritos
            sublist = []
            sublist.append(muro.muro_x)
            sublist.append(muro.muro_y)
            posiciones_no_ocupar.append(sublist)
        sublist = []
        sublist.append(cuadro_x)
        sublist.append(cuadro_y)
        posiciones_no_ocupar.append(sublist)

        # Fase 2: generar lista de todas las posibilidades ·······

        posiciones_totales = [] # todo esta en cuadritos
        for i in range(0,self.ancho_mapa):
            coordenada_x = i
            for j in range(0,self.alto_mapa):
                coordenada_y = j
                sublist = []
                sublist.append(coordenada_x)
                sublist.append(coordenada_y)
                posiciones_totales.append(sublist)

        # Fase 3: comparaciones, para ver las libres actualizadas ····················

        self.item = []
        for posicion in posiciones_totales: # una minilista de la forma [x,y]
            if posicion not in posiciones_no_ocupar:
                self.item.append(posicion)

        # Fase 4: crear un item aleatorio en una posicion aleatoria ··················

        if self.timer.llegando_a_timer_item >= self.timer.timer_aparicion_item:
            self.timer.timer_aparicion_item = random.randint(0,20)
            self.timer.llegando_a_timer_item = 0
            if self.item_creado == -1: #no se ha creado item aun
                indice_azar = random.randint(0,(len(self.item)-1))  # indice de la lista, para la posicion
                tipo_de_item = random.randint(0,2) # obtenemos el tipo de item aleatoriamente
                if tipo_de_item == 0 and len(self.objetos_serpiente)!=0: # si es una patita, no creada
                    id = self.escenario.crea_item((self.item[indice_azar][0]),(self.item[indice_azar][1]),0) #creo la patita
                    self.patita.creado = 10 # ponemos que ha sido creada
                    self.patita.identificar(id) #le agrego su id para quedar identificada
                    self.patita.coordenada.append(self.item[indice_azar][0])
                    self.patita.coordenada.append(self.item[indice_azar][1]) #guardo las coordenadas [x,y]
                    self.item_creado = 0 # es importante cambiarlo. es porque ahora hay un item creado
                elif tipo_de_item == 1 and len(self.objetos_serpiente)!= 0: # este item es el ssc
                    id = self.escenario.crea_item((self.item[indice_azar][0]),(self.item[indice_azar][1]),1) #creo un ssc
                    self.ssc.creado = 10 #esta creado
                    self.ssc.identificar(id)
                    self.ssc.coordenada.append(self.item[indice_azar][0])
                    self.ssc.coordenada.append(self.item[indice_azar][1])
                    self.item_creado = 0
                elif tipo_de_item == 2 and len(self.objetos_serpiente)!=0:
                    id = self.escenario.crea_item((self.item[indice_azar][0]),(self.item[indice_azar][1]),2) #creo una bandera
                    self.bandera.creado = 10 #esta creado
                    self.bandera.identificar(id)
                    self.bandera.coordenada.append(self.item[indice_azar][0])
                    self.bandera.coordenada.append(self.item[indice_azar][1])
                    self.item_creado = 0 #item creado

        self.timer.llegando_a_timer_item = self.timer.llegando_a_timer_item + segundos
        
        # Fase 5: efectos de los items ···············································

        if self.item_creado == 0: # hay un item creado. una vez que se elimine, debe cambiar a -1.
            if self.patita.creado == 10: # patita creada
                if ((cuadro_x) == self.patita.coordenada[0]) and ((cuadro_y)==self.patita.coordenada[1]):
                    if len(self.objetos_serpiente) !=0: #si quedan serpientes
                        serpiente_azar = random.randint(0,(len(self.objetos_serpiente)-1)) #buscamos indice al azar
                        serpiente_victima = self.objetos_serpiente[serpiente_azar] #sacaremos serpiente al azar
                        id_serpiente_victima = serpiente_victima.id #obtenemos su id
                        self.escenario.elimina_serpiente(id_serpiente_victima) #la eliminamos
                        for serpiente in self.objetos_serpiente:
                            if serpiente.id == id_serpiente_victima:
                                self.objetos_serpiente.remove(serpiente)
                        self.escenario.elimina_item(self.patita.id) #borro la patita
                        self.patita.creado = -1 #ya no esta creada
                        self.item_creado = -1 # ya no hay objeto creado
                        self.patita.coordenada = [] #ya no hay coordenadas para el item
                else:
                    for serpiente in self.objetos_serpiente:
                        x_serpiente_cuadro = int((serpiente.serpiente_x+14.5)//32)
                        y_serpiente_cuadro = int((serpiente.serpiente_y+14.5)//32)
                        lista_x_mas = [(x_serpiente_cuadro)+1,y_serpiente_cuadro]
                        lista_x_menos = [(x_serpiente_cuadro)-1,y_serpiente_cuadro]
                        lista_y_mas = [(x_serpiente_cuadro),(y_serpiente_cuadro)+1]
                        lista_y_menos = [(x_serpiente_cuadro),(y_serpiente_cuadro)-1]
                        if ((x_serpiente_cuadro)==(self.patita.coordenada[0])) and ((y_serpiente_cuadro)==(self.patita.coordenada[1])):
                            if (lista_x_mas) in self.item:
                                serpiente_extra = Serpiente(((x_serpiente_cuadro)+1)*32,(y_serpiente_cuadro*32))
                                id = self.escenario.crea_serpiente(serpiente_extra.serpiente_x,serpiente_extra.serpiente_y)
                                serpiente_extra.identificar(id) #ahora identifico la serpiente
                                self.objetos_serpiente.append(serpiente_extra) # la agrego a la lista
                                self.escenario.elimina_item(self.patita.id) #primero borro la patita
                                self.patita.creado = -1 # ya no hay patita
                                self.item_creado = -1 # ya no hay item
                                self.patita.coordenada = [] #coordenadas iniciales de patita se restauran
                                break
                            elif (lista_x_menos) in self.item:
                                serpiente_extra = Serpiente(((x_serpiente_cuadro)-1)*32,(y_serpiente_cuadro*32))
                                id = self.escenario.crea_serpiente(serpiente_extra.serpiente_x,serpiente_extra.serpiente_y)
                                serpiente_extra.identificar(id) #ahora identifico la serpiente
                                self.objetos_serpiente.append(serpiente_extra) # la agrego a la lista
                                self.escenario.elimina_item(self.patita.id) #primero borro la patita
                                self.patita.creado = -1 # ya no hay patita
                                self.item_creado = -1 # ya no hay item
                                self.patita.coordenada = [] #coordenadas iniciales de patita se restauran
                                break
                            elif (lista_y_menos) in self.item:
                                serpiente_extra = Serpiente((x_serpiente_cuadro)*32,(((y_serpiente_cuadro)-1)*32))
                                id = self.escenario.crea_serpiente(serpiente_extra.serpiente_x,serpiente_extra.serpiente_y)
                                serpiente_extra.identificar(id) #ahora identifico la serpiente
                                self.objetos_serpiente.append(serpiente_extra) # la agrego a la lista
                                self.escenario.elimina_item(self.patita.id) #primero borro la patita
                                self.patita.creado = -1 # ya no hay patita
                                self.item_creado = -1 # ya no hay item
                                self.patita.coordenada = [] #coordenadas iniciales de patita se restauran
                                break
                            elif (lista_y_mas) in self.item:
                                serpiente_extra = Serpiente((x_serpiente_cuadro)*32,(((y_serpiente_cuadro)+1)*32))
                                id = self.escenario.crea_serpiente(serpiente_extra.serpiente_x,serpiente_extra.serpiente_y)
                                serpiente_extra.identificar(id) #ahora identifico la serpiente
                                self.objetos_serpiente.append(serpiente_extra) # la agrego a la lista
                                self.escenario.elimina_item(self.patita.id) #primero borro la patita
                                self.patita.creado = -1 # ya no hay patita
                                self.item_creado = -1 # ya no hay item
                                self.patita.coordenada = [] #coordenadas iniciales de patita se restauran
                                break
            elif self.ssc.creado == 10: #de esta forma, aqui va a entrar una vez
                if ((cuadro_x) == self.ssc.coordenada[0]) and ((cuadro_y) == self.ssc.coordenada[1]):
                    if self.ssc.timer == 0 and self.ssc.marca != 2: #no es de la serpiente
                        self.ssc.timer = self.ssc.timer + segundos
                        self.ssc.marca = 1
                else:
                    for serpiente in self.objetos_serpiente: #para las serpientes
                        x_serpiente_cuadro = int((serpiente.serpiente_x+14.5)//32)
                        y_serpiente_cuadro = int((serpiente.serpiente_y+14.5)//32)
                        if (x_serpiente_cuadro)== ((self.ssc).coordenada)[0] and (y_serpiente_cuadro)== ((self.ssc).coordenada)[1] and (self.ssc.marca != 1):
                            self.ssc.timer2 = self.ssc.timer2 + segundos
                            self.ssc.marca = 2
                if self.ssc.timer !=0: # esto es para el heroe
                    self.ssc.timer = self.ssc.timer + segundos
                    if self.ssc.timer > 12:
                        self.ssc.timer = 0
                        self.escenario.elimina_item(self.ssc.id) #primero borro la patita
                        self.ssc.creado = -1 # ya no hay patita
                        self.item_creado = -1 # ya no hay item
                        self.ssc.coordenada = [] #coordenadas inicia
                        self.ssc.marca = 0
                if self.ssc.timer2 !=0: #esto es para la serpiente
                    self.ssc.timer2 = self.ssc.timer2 + segundos
                    if self.ssc.timer2 > 12:
                        self.ssc.timer2 = 0
                        self.escenario.elimina_item(self.ssc.id) #primero borro la patita
                        self.ssc.creado = -1 # ya no hay ssc
                        self.item_creado = -1 # ya no hay item
                        self.ssc.coordenada = [] #coordenadas inicia
                        self.ssc.marca = 0
            elif self.bandera.creado == 10:
                if ((cuadro_x) == self.bandera.coordenada[0]) and ((cuadro_y) == self.bandera.coordenada[1]): #para el heroe
                    if self.bandera.timer == 0 and self.bandera.marca != 2: # no ha sido dominado por la serpiente
                        self.bandera.timer = self.bandera.timer + segundos
                        self.bandera.marca = 1 #ha sido tomado por el heroe
                else:
                    for serpiente in self.objetos_serpiente: 
                        x_serpiente_cuadro = int((serpiente.serpiente_x+14.5)//32)
                        y_serpiente_cuadro = int((serpiente.serpiente_y+14.5)//32)
                        if (x_serpiente_cuadro)== ((self.bandera).coordenada)[0] and (y_serpiente_cuadro)== ((self.bandera).coordenada)[1] and (self.bandera.marca != 1):
                            self.bandera.timer2 = self.bandera.timer2 + segundos
                            self.bandera.marca = 2
                if self.bandera.timer!=0: #efecto del heroe sobre las serpientes
                   self.bandera.timer = self.bandera.timer + segundos
                   if self.bandera.timer > 12:
                       self.bandera.timer = 0 # se resetea
                       self.escenario.elimina_item(self.bandera.id) #primero borro la patita
                       self.bandera.creado = -1 # ya no hay patita
                       self.item_creado = -1 # ya no hay item
                       self.bandera.coordenada = [] #coordenadas inicia
                       self.bandera.marca = 0 #nadie lo ha tomado aun , se resetea la opcion
                if self.bandera.timer2!=0: #efecto de serpientes sobre las serpientes
                   self.bandera.timer2 = self.bandera.timer2 + segundos
                   if self.bandera.timer2 > 12:
                       self.bandera.timer2 = 0 # se resetea
                       self.escenario.elimina_item(self.bandera.id) #primero borro la patita
                       self.bandera.creado = -1 # ya no hay patita
                       self.item_creado = -1 # ya no hay item
                       self.bandera.coordenada = [] #coordenadas inicia
                       self.bandera.marca = 0 #nadie lo ha tomado aun , se resetea la opcion

        # ********************** PARTE 5: QUIEN GANA *************************************

        for serpiente in self.objetos_serpiente:
            x_serpiente_cuadro = int((serpiente.serpiente_x+14.5)//32)
            y_serpiente_cuadro = int((serpiente.serpiente_y+14.5)//32)
            if (cuadro_x) == (x_serpiente_cuadro) and (cuadro_y)==(y_serpiente_cuadro):
                self.escenario.muestra_mensaje("Aire!!! Aire!!!", "Oh, no! Las serpientes me están... asfixiado...")
                self.escenario.muestra_mensaje("Un rayo de esperanza??","Espera... Qué es esa luz allá arriba?")
                self.escenario.salir()
                
        if self.gana.gana_heroe == (len(self.coordenadas_pd)):
            self.escenario.muestra_mensaje("Nuevo estado de Facebook: Pythonia's Master!", "Sí!! He sobrevivido!! Ahora puedo irme y enseñar el lenguaje de Pythonia :3 !")
            self.escenario.salir()
        elif self.gana.gana_serpiente == (len(self.coordenadas_pd)):
            self.escenario.muestra_mensaje("NO!", "Las serpientes me han ganado! Debo escapar o me asfixiarán :( !!")
            self.escenario.salir()
                    
    def corre(self): 
        self.escenario.corre()

j = Juego()
j.corre()
