import msgGUI
import mensajeria

def tarea(gui):
    
    #INICIO TAREA

    # PARTE 1: FUNCIONES

    def string_a_binario(s): # función que pasa string a binario
        respf=''
        for car in s:
            asci=ord(car) # tiene número de cada carácter
            respi=''
            num=1
            while num!=0:
                num=(asci//2) # aquí se tiene el entero de la división
                num2=(asci%2) # aquí se tiene el resto de la división 
                asci=num
                respi=respi+str(num2) # respuesta de un carácter
            respi=respi[::-1]
            if len(respi)<8:
                delt=8-len(respi)
                lista=[0]*delt
                for i in lista:
                    respi=str(lista[i])+respi
            respf=respf+respi
        return respf

    def binario_a_string(s): # función que pasa de binario (en forma string) a string final
        lista=[]
        k=len(s)
        num=0
        resultf=''
        while k!=0: # coloca pedacitos - múltiplos de 8 - de binario en lista 
            pedacito=s[0:8]
            s=s[8:k]
            lista.append(pedacito)
            k=len(s) # hasta aquí, pedacitos en una lista
        for element in lista: # un solo pedacito 
            i=7
            for car in element: # caracteres de un pedacito 
                suma=(int(car)*(2**i))
                i=i-1
                num=num+suma # aquí, la suma de un pedacito
            h=chr(num)
            resultf=resultf+h
            num=0
        return resultf

    def OTP(msg,clave): # encripta y desencripta
        resultado=''
        i=0
        if len(msg)==len(clave):
            while i!=(len(msg)):
                if msg[i]==clave[i]:
                    resultado=resultado+str(0)
                elif msg[i]!=clave[i]:
                    resultado=resultado+str(1)
                i=i+1
        elif len(msg)<len(clave):
            clave=clave[0:len(msg)]
            while i!=(len(msg)):
                if msg[i]==clave[i]:
                    resultado=resultado+str(0)
                elif msg[i]!=clave[i]:
                    resultado=resultado+str(1)
                i=i+1
        return resultado

    # FUNCIÓN EXTRA PARA ORDENAMIENTO DE LISTAS RECIBIDOS Y ENVIADOS

    def ordenar_enviados(l):
        k=0
        long=len(l)
        auxiliar=[]
        clave = '010000011101100111101101101001000100101110101110100011110001000100011000010110000001100110011110111001100011101000010010010111101110100101111001111111010100100101110010111011011110111111101101011111110100111100010001100100111011011110110111010000101110001011100011011100100000101011010101101100101010001110010110000100110001101100110011000101001011001011011011'
        while k<long:
            sublista=l[k]
            h=OTP(sublista[2],clave)
            mensajelisto=sublista[1]+"De: bastitic@puc.cl Para: "+sublista[0]+" - "+(binario_a_string(h))
            auxiliar.append(mensajelisto)
            k=k+1
        return auxiliar

    def ordenar_recibidos(l):
        k=0
        long=len(l)
        auxiliar=[]
        clave = '010000011101100111101101101001000100101110101110100011110001000100011000010110000001100110011110111001100011101000010010010111101110100101111001111111010100100101110010111011011110111111101101011111110100111100010001100100111011011110110111010000101110001011100011011100100000101011010101101100101010001110010110000100110001101100110011000101001011001011011011'
        while k<long:
            sublista=l[k]
            h=OTP(sublista[2],clave)
            mensajelisto=sublista[1]+"De: "+sublista[0]+" Para: bastitic@puc.cl"+" - "+(binario_a_string(h))
            auxiliar.append(mensajelisto)
            k=k+1
        return auxiliar


    # ****** PROGRAMA PRINCIPAL EMPIEZA AQUI *********
  
    # PARTE 1: CAMBIO TÍTULO, MAIL Y CLAVE
    
    gui.cambiar_titulo('Mensajería Segura')
    
    mail='bastitic@puc.cl'
    clave = '010000011101100111101101101001000100101110101110100011110001000100011000010110000001100110011110111001100011101000010010010111101110100101111001111111010100100101110010111011011110111111101101011111110100111100010001100100111011011110110111010000101110001011100011011100100000101011010101101100101010001110010110000100110001101100110011000101001011001011011011'

    # PARTE 2: CHEQUIAR SERVIDOR
    
    while True:
        if mensajeria.conectar(mail, clave):
                gui.alerta('Te has conectado correctamente al servidor! :)')
                break
        else:
                gui.alerta('Imposible conectar con el servidor de mensajería :(')
                ask=gui.preguntar('Quieres intentarlo otra vez? :3')
                if ask==False:
                    gui.alerta('Adiós!! Recuerda seguirnos en Facebook y Twitter :p')
                    gui.salir()

    #PARTE 3: ANTES DE EMPEZAR - VARIABLES INICIALES
    
    seccion=1 # indica la sección (o pantalla) en la que estoy.
              # 1 es sección de redactar, y 2 es sección de mensajes

    recibidos=mensajeria.mensajes_recibidos() # lista de recibidos

    enviados=mensajeria.mensajes_enviados() # lista de los enviados

    #PARTE 4: CARGA INICIAL DE MENSAJES

    enviados=mensajeria.mensajes_enviados()
    enviados=ordenar_enviados(enviados) # lista ordenada con strings en formato Para/De
        
    recibidos=mensajeria.mensajes_recibidos()
    recibidos=ordenar_recibidos(recibidos) # lista ordenada con strings en formato Para/De

    j=0
    while j<len(recibidos):
        enviados.append(recibidos[j])
        j=j+1

    listafinal=enviados
    listafinal.sort() 
    listafinal.reverse()

    for car in range(len(listafinal)): # Esto solo lo ordena 
        mensajito=listafinal[car]
        msje_final=mensajito[29:]
        gui.poner_mensaje_al_final(msje_final)
    

    #PARTE 5: EMPIEZA EL CICLO  *******************************************

    while True:

        boton=gui.esperar_click()
        
        enviados=mensajeria.mensajes_enviados()
        enviados=ordenar_enviados(enviados) # lista ordenada con strings en formato Para/De
        
        recibidos=mensajeria.mensajes_recibidos()
        recibidos=ordenar_recibidos(recibidos) # lista ordenada con strings en formato Para/De

        # ORDEN DE LISTA

        j=0
        while j<len(recibidos):
            enviados.append(recibidos[j])
            j=j+1

        listafinal=enviados
        listafinal.sort()
        listafinal.reverse()

        # LOS BOTONES

        if boton==0: #Actualizar
            gui.alerta('Has presionado el botón para actualizar mensajes.')
            gui.borrar_mensajes()
            for car in range(len(listafinal)):
                mensajito=listafinal[car]
                msje_final=mensajito[29:]
                gui.poner_mensaje_al_final(msje_final)
            
        elif boton==1: #Búsqueda
            gui.alerta('Has presionado el botón para buscar.')
            gui.borrar_mensajes()
            buscado=gui.busqueda()
            buscado=buscado.lower()
            for car in range(len(listafinal)):
                mensajestring_original=listafinal[car] # esto es un mensaje unido en forma string, que hay que guardar
                mensajestring2=mensajestring_original # obtener la copia
                mensajestring2=mensajestring2[29:]# sacar fecha
                mensajestring2=mensajestring2[4:] # sacar "De: "
                i_espacio_dos=mensajestring2.find(' ')
                copia=mensajestring2[0:i_espacio_dos] # aquí se guarda el primer mail
                mensajestring2=mensajestring2[(i_espacio_dos)+1:]# aquí se tiene de "Para: " en adelante
                i_espacio_para=mensajestring2.find('Para: ') # antes solo hay mail
                mensajestring2=mensajestring2[(i_espacio_para)+1:] # se tiene desde 'ara'
                mensajestring2=mensajestring2[5:]# segundo mail
                i_espacio_tres=mensajestring2.find(' ')
                copia=copia+mensajestring2[0:i_espacio_tres] #dos mails
                mensajestring2=mensajestring2[(i_espacio_tres)+1:]
                mensajestring2=mensajestring2[2:]
                copia=copia+mensajestring2 # aquí hay una copia con los dos mails y mensajes
                copiaminusc=copia.lower()
                if buscado in copiaminusc: # buscado está en lower case (mensajestring2)
                    mensajestring_original=mensajestring_original[29:] # sacar la fecha
                    gui.poner_mensaje_al_final(mensajestring_original)
        
        elif boton==2: # Para enviar mensaje
            if seccion==1: # Cuando estaba en redactar
                gui.alerta('Has presionado el botón para redactar un mensaje.')
                seccion=1
            elif seccion==2: # Cuando estaba en mensajes
                seccion=1
                gui.alerta('Has presionado el botón para redactar un mensaje.')
                gui.pantalla_redactar()
                    
        elif boton==3:
            seccion=2 # Cambio a la seccion de mensajes
            gui.alerta('Has presionado el botón para mostrar mensajes.')
            gui.pantalla_mensajes() # Muestro la seccion de mensajes
            
        elif boton==4: # Si lo aprieta, es porque la seccion es 1
            total=mensajeria.mensajes_enviados_hoy()
            if total < 50:
                seccion=1
                gui.alerta('Has presionado el botón para enviar mensajes.')
                destino=gui.destinatario()
                message=gui.mensaje_redactado()
                if mensajeria.enviar_mensaje(destino,OTP(string_a_binario(message),clave))==True:
                    gui.alerta('Mensaje enviado correctamente.')
                    total=mensajeria.mensajes_enviados_hoy()
                    gui.alerta('Has enviado '+str(total)+' mensajes hoy. Te quedan '+str(50-total)+' mensajes para enviar este día.')
                    gui.borrar_destinatario()
                    gui.borrar_mensaje_redactado()
                else:
                    gui.alerta('El mensaje no se ha podido enviar.')
                    gui.alerta('Esto puede deberse a un mensaje de más de 45 caracteres o algún error del servicio de mensajería.')
            elif total>=50:
                gui.alerta('Ya has superado la cuota de mensajes para hoy! Tendrás que esperar hasta mañana :)')
                
    #FIN TAREA
    
app = msgGUI.Application(None)
app.cargar_programa(tarea)
app.iniciar()
