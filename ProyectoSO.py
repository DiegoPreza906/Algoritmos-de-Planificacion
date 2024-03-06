import os
def ProcesoFCFS(procesoM, rafagas, programas, llegadas):
	sumaT = 0
	tiempo_inicio = [0] * len(procesoM)  # Almacenar el tiempo de inicio de cada proceso
	tiempo_final = [0] * len(procesoM)   # Almacenar el tiempo de finalización de cada proceso
	tiempo_espera = [0] * len(procesoM)  # Almacenar el tiempo de espera de cada proceso

	print("\n-------------Ejecutando los Programas------------")

	# Ordenar los procesos por su tiempo de llegada (FCFS)
	procesoM = [x for _, x in sorted(zip(llegadas, procesoM))]
	rafagas = [x for _, x in sorted(zip(llegadas, rafagas))]
	llegadas = sorted(llegadas)

	for i in range(len(procesoM)):
		print(f"Proceso: {programas[procesoM[i]]}\tRáfaga: {rafagas[i]}\tTiempo de llegada: {llegadas[i]}")

	for i in range(len(procesoM)):
		tiempo_inicio[i] = max(sumaT, llegadas[i])  # El tiempo de inicio de un proceso es máximo entre su llegada y el tiempo acumulado
		tiempo_espera[i] = tiempo_inicio[i] - llegadas[i]  # Calcular el tiempo de espera
		sumaT = tiempo_inicio[i] + rafagas[i]  # Actualizar el tiempo acumulado
		tiempo_final[i] = sumaT  # El tiempo de finalización es el tiempo acumulado después de ejecutar la ráfaga del proceso

	print("\n-------------Tiempos de inicio, salida y espera------------")
	for i in range(len(procesoM)):
		print(f"Proceso: {programas[procesoM[i]]}\tTiempo de inicio: {tiempo_inicio[i]}\tTiempo de salida: {tiempo_final[i]}\tTiempo de espera: {tiempo_espera[i]}")

	promedio_espera = sum(tiempo_espera) / len(procesoM)
	promedio_finalizacion = sum(tiempo_final) / len(procesoM)
	print(f"\nPromedio de tiempo de espera: {promedio_espera}")
	print(f"Promedio de tiempo de finalización: {promedio_finalizacion}")

	os.system("Pause")
	os.system("cls")

def ProcesoSJF(procesoM, rafagas, programas, llegadas):
     
     
	tiempo_inicio = [0] * len(procesoM)  # Almacenar el tiempo de inicio de cada proceso
	tiempo_final = [0] * len(procesoM)   # Almacenar el tiempo de finalización de cada proceso
	tiempo_espera = [0] * len(procesoM)  # Almacenar el tiempo de espera de cada proceso
	tiempo_restante = rafagas.copy()     # Tiempo restante para cada proceso

	tiempo_actual = min(llegadas)        # Tiempo actual de la simulación
	cola_procesos = []                   # Cola para los procesos listos

	print("\n-------------Ejecutando los Programas con SJF------------")

	while True:
		# Agregar los procesos que llegan en este tiempo a la cola
		for i in range(len(procesoM)):
			if llegadas[i] <= tiempo_actual and tiempo_restante[i] > 0:
				cola_procesos.append(i)

		if not cola_procesos:
			break  # Si no hay procesos en la cola, salir del bucle

		# Ordenar la cola de procesos por su ráfaga restante (SJF)
		cola_procesos.sort(key=lambda x: tiempo_restante[x])

		# Ejecutar el proceso con la ráfaga más corta en este momento
		proceso = cola_procesos[0]
		tiempo_inicio[proceso] = tiempo_actual

		# Determinar cuánto tiempo se ejecutará este proceso
		tiempo_ejecucion = tiempo_restante[proceso]

		# Reducir el tiempo restante del proceso
		tiempo_restante[proceso] = 0

		# Avanzar el tiempo actual
		tiempo_actual += tiempo_ejecucion

		# Calcular el tiempo de espera y finalización del proceso
		tiempo_espera[proceso] = tiempo_actual - rafagas[proceso] - llegadas[proceso]
		tiempo_final[proceso] = tiempo_actual

		# Eliminar el proceso de la cola
		cola_procesos.pop(0)

	print("\n-------------Tiempos de inicio, salida y espera------------")
	for i in range(len(procesoM)):
		print(f"Proceso: {programas[procesoM[i]]}\tTiempo de inicio: {tiempo_inicio[i]}\tTiempo de salida: {tiempo_final[i]}\tTiempo de espera: {tiempo_espera[i]}")

	promedio_espera = sum(tiempo_espera) / len(procesoM)
	promedio_finalizacion = sum(tiempo_final) / len(procesoM)
	print(f"\nPromedio de tiempo de espera: {promedio_espera}")
	print(f"Promedio de tiempo de finalización: {promedio_finalizacion}")

	os.system("Pause")
	os.system("cls")
     
def ProcesoRRT(procesoM, rafagas, programas,arrivalTime):
    sumaT=1 #suma de todos las rafagas
    cont=0 #sirve para acumular cuando se tardo cada proceso por quantum
    done=0  #sirve para saber cuantos numeros se van a sumar en cont
    Tfinalización=0 #calcula el tiempo de cada proceso
    Tpromedio=0#calcula el promedio del tiempo de todos y dividirlo entre los procesos
    tiempo=[] #guarda en que momento se termina cada proceso
    #arrivalTime=[0,1,2,4,5] #indica el tiempo que tardo en llegar los procesos
    rafagas2=[] #guarda una doble vez las rafagas
    colaProceso=[] #primera cola que guardara todos los procesos a hacer
    colaProceso2=[] #segunda cola que guarda los procesos que faltan
    contA=0 #verifica que los tiempos sean iguales
    cont2=0 #guarda la variable que tenemos que cambiar de lugar
    qua=0 
    flag=0
    
    print("\n-------------Quantums------------")   
    flag2=1 #flag para salir de ciclo while
    while flag2==1:
        numq=int(input("\nElegir un quantum entre 2 y 4:"))
        if numq<=5 and numq>=2: #Validación para numero de quantums
            flag2=0
            qua=numq #guarda el quantum
        else:
            print("\nERROR----Por favor escoger una quantum correcto")
   
    for i in rafagas:#ciclo para llenar rafagas2 con los valores de rafagas
        rafagas2.append(i)

    for i in procesoM: #ciclo para que cola 2 tenga los mismos procesos
        colaProceso2.append(i)

    while sumaT!=0: #no sale del cilo hasta que las rafagas sean 0
        sumaT=0
        for i in range(0,len(procesoM)): #Comienza el ciclo los procesos
            if arrivalTime[i]==contA and rafagas[i]!=0: #si el tiempo de llegada es el mismo al contador
                contA=contA+1 #se agrega un 1 a cont
                colaProceso.append(i) #coloca los que vayan llegando
                var=rafagas[i]-qua #para guardar y verificar que el valor no sea menor a 0

                if var<0:
                    rafagas[i]=0
                else:
                    rafagas[i]=rafagas[i]-qua
                    

            else: #si el tiempo es diferente a contA
                for j in range(0,len(colaProceso2)): #Hace otro ciclo para cambiar la cola 2
                    if rafagas[j]!=0 and arrivalTime[i]!=contA: #si el tiempo sigue siendo diferente hace el proceso
                        contA=contA+1
                        cont2=j #guarda el valor que vamos a cambiar
                        cont3=j+1 #guarada la posición por el que cambiaremos
                        colaProceso.append(j) #primero se agrega el valor que esta en cola
                        colaProceso.append(i) #despues se agrega el que aun no ha pasado
                        flag=1
                        var=rafagas[j]-qua
                        if var<0:
                            rafagas[j]=0
                        else:
                            rafagas[j]=rafagas[j]-qua
                        
                        var=rafagas[i]-qua
                        if var<0:
                            rafagas[i]=0
                        else:
                            rafagas[i]=rafagas[i]-qua
                            
                if flag==1: #si la flag fuera 0 no se haria proceso
                    elemento = colaProceso2.pop(cont2) #elimina y guarda el numero que queremos cambiar de pos
                    colaProceso2.insert(cont3, elemento) #lo inserte en la posición siguiente
                    contA=contA+1
        

        for i in range(0,len(colaProceso2)):#pasa por todos lo procesos si un no estan en 0 y la cola no esta vacia
            if rafagas[i]!=0:
                
                colaProceso.append(colaProceso2[i]) #coloca los que vayan llegando
                var=rafagas[i]-qua

                if var<0:
                    rafagas[i]=0
                else:
                    rafagas[i]=rafagas[i]-qua
        
        for i in rafagas:
            sumaT=sumaT+i
    
    for i in range(0,len(procesoM)): #llena otra vez las rafagas para el siguente proceso
        rafagas[i]=rafagas2[i]
    
    
    for y in range(0,len(procesoM)):
        tiempo.append(0) #Llena el arreglo de tiempo que servira para saber cuanto tiempo tardo en realizarse un proceso
    print("\n-------------Ejecutando los Programas------------")  
    sumaT=1
    while sumaT!=0:
        sumaT=0 

        for i in rafagas: #ciclo para saber si las suma de las rafagas da 0
            sumaT=sumaT+i

        for j in range(0,len(colaProceso2)): #pasa por todos lo procesos
    
            cont=cont+done #total de cuanto tiempo se tardaron los procesos
            if rafagas[j]!=0: #si la rafaga no es 0
                var=rafagas[j]-qua
                if var<0:
                    doneP=qua-rafagas[j]
                    done=qua-doneP
                    tiempo[j]=cont+done
                    
                    rafagas[j]=0

                else:
                    rafagas[j]=rafagas[j]-qua
                    done=qua
                    if rafagas[j]==0:
                        tiempo[j]=cont+done
            else:
                
                done=0

    print("\n---------------Finalización de procesos------------")        
    for y in range(0,len(procesoM)):
        Tespera=tiempo[y]-rafagas2[y]-arrivalTime[y]
        Tfinalización=Tfinalización+tiempo[y]
        Tpromedio=Tpromedio+Tespera
        print(f"\nPrograma:{programas[procesoM[y]]}\tNumero en donde termino:{tiempo[y]} \tTiempo de Espera:{Tespera}")
    
    Tfinalización=Tfinalización/len(procesoM)
    Tpromedio=Tpromedio/len(procesoM)
    print(f"\nEl tiempo de espera promedio fue {Tpromedio} y el tiempo de finalización fue {Tfinalización}")

    os.system("Pause")
    os.system("cls")
             
def ProcesoRR(procesoM,rafagas,programas):
    sumaT=1 #suma de todos las rafagas
    cont=0 #sirve para acumular cuando se tardo cada proceso por quantum
    done=0 #sirve para saber cuantos numeros se van a sumar en cont
    Tfinalización=0 #calcula el tiempo de cada proceso
    Tpromedio=0 #calcula el promedio del tiempo de todos y dividirlo entre los procesos
    tiempo=[] #guarda en que momento se termina cada proceso
    rafagas2=[] #guarda una doble vez las rafagas

    for j in range(0,len(procesoM)): #ciclo para llenar rafagas2 con los valores de rafagas
        rafagas2.append(rafagas[j])
    
    for y in range(0,len(procesoM)):
        tiempo.append(0) #Llena el arreglo de tiempo que servira para saber cuanto tiempo tardo en realizarse un proceso
    
    print("\n-------------Quantums------------")   
    flag2=1 #flag para salir de ciclo while
    while flag2==1:
        numq=int(input("\nElegir un quantum entre 2 y 4:"))
        if numq<=4 and numq>=2: #Validación para numero de quantums
            flag2=0
            qua=numq #guarda el quantum
        else:
            print("\nERROR----Por favor escoger una quantum correcto")

    print("\n-------------Ejecutando los Programas------------")  
    
    while sumaT!=0:
        sumaT=0

        for i in rafagas:  #ciclo para saber si las suma de las rafagas da 0
            sumaT=sumaT+i

        for j in range(0,len(procesoM)): #pasa por todos lo procesos
    
            cont=cont+done #total de cuanto tiempo se tardaron los procesos
            if rafagas[j]!=0: #si la rafaga no es 0
                var=rafagas[j]-qua #para guardar y verificar que el valor no sea menor a 0
                
                if var<0: 
                    doneP=qua-rafagas[j] #guarda el resultado de lo quantums menos la rafaga
                    done=qua-doneP #cuanto se le va a sumar a cont
                    tiempo[j]=cont+done #agrega el tiempo en el que termino el proceso
                    rafagas[j]=0 #pone la rafaga en 0

                else:
                    rafagas[j]=rafagas[j]-qua #poner el valor de las rafagas menos el quantum
                    done=qua #sumara a cont el quantum
                    if rafagas[j]==0:
                        tiempo[j]=cont+done 
            else:
                
                done=0

    print("\n---------------Finalización de procesos------------")        
    for y in range(0,len(procesoM)): #para mostrar y hacer calculo de tiempo
        Tespera=tiempo[y]-rafagas2[y] #Calcula el tiempo de espera de cada proceso
        Tfinalización=Tfinalización+tiempo[y]  #para calcular el promedio de tiempo de finalización
        Tpromedio=Tpromedio+Tespera #para calcular el promedio de los tiempos 
        print(f"\nPrograma:{programas[procesoM[y]]}\tNumero en donde termino:{tiempo[y]} \tTiempo de Espera:{Tespera}")
    
    Tfinalización=Tfinalización/len(procesoM)
    Tpromedio=Tpromedio/len(procesoM)
    print(f"\nEl tiempo de espera promedio fue {Tpromedio} y el tiempo de finalización fue {Tfinalización}")

    os.system("Pause")
    os.system("cls")

def menuLlegadas(numproceso):
	llegadas = []
	print("\n-------------Tiempos de llegada------------")
	for i in range(numproceso):
		while True:
			llegada = int(input(f"Ingrese el tiempo de llegada para el proceso {i + 1}: "))
			if llegada < numproceso + 1:
				llegadas.append(llegada)
				break  # Salir del bucle si el tiempo de llegada es válido
			else:
				print("¡Error! El tiempo de llegada debe ser válido.")

	return llegadas

def menuRafagas(numproceso):
    rafaga=[] #guarda las rafagas y las retorna
       
    print("\n-------------Rafagas------------")
    for i in range(numproceso): #ciclo para poner rafagas a cada uno de los procesos
        
        #Validación para no elegir una rafaga mayor a 15 y menor a 1
        flag=1
        while flag==1:
            numraf = int(input(f"Elegir una ráfaga menor a 15 para el proceso {i + 1}:"))
            if numraf<=15 and numraf>0: #validación para que rafaga sea mayo a 0 menor a 15
                flag=0
            else:
                print("\nERROR----Por favor escoger una rafaga menor a 15")

        rafaga.append(numraf)

        


    return rafaga

def menuProcesos(): #Menu para elegir que procesos queremos
	proceso = []  # Guarda los procesos y los retorna
	op = 0
	flag = 1  # Flag para salir de ciclo while

	while flag == 1:

		flag2 = 1
		print("-------------Procedimientos------------")  # Menu de procedimientos disponibles
		print("\n0.Excel\n1.Word\n2.Chrome\n3.Zoom\n4.Discord\n5.Salir")
		op = int(input("Que programas quieres que se ejecuten:"))

		if op == 5:  # Check if option is 5
			print("\nProcesos seleccionados:")
			for i, programa in enumerate(proceso, start=1):
				print(f"{i}. {programas[programa]}")
			flag = 0
		else:
			for i in proceso:  # Validar que no se haya repetido alguna opción
				if i == op:
					flag2 = 0

			if flag2 == 1 and op != 5 and op < 5:  # Se agrega a la lista sino se repitió el número, si la opción no es salir y que no sea mayor al número de opciones
				proceso.append(op)
			else:
				print("\nSu opción ya está en la lista/no se encuentra ese proceso")

			if op == 5:
				flag = 0

	return proceso

def  Menu1(): #Menu para elegir que algoritmo utilizar
    print("\n-------------Algoritmo de planificación------------\n")
    print("\n1.FCFS\n2.SJF\n3.RR\n4.RR con tiempo de llegada\n5.Salir")
    op=int(input("Numero:"))
    return op #regresa la opcion elegida

    
resp1=0
procesoM=[] #guarda todos los procesos deseados en numeros
programas=["Excel","Word","Chrome","Zoom","Discord"] #sirve para mostrar los procesos en un futuro
rafagas=[] #guarda la rafaga de cada proceso
llegadas=[]

while resp1!=5: #mientras la resp1 no sea 4 puedes utilizar el sistema
    resp1=Menu1()

    #Tipo switch que dependiendo la respuesta se hace el proceso de ese algoritmo
    if  resp1==1:
        procesoM = menuProcesos()
        rafagas = menuRafagas(len(procesoM))
        llegadas = menuLlegadas(len(procesoM))
        ProcesoFCFS(procesoM, rafagas, programas, llegadas)

    elif resp1==2:
        procesoM = menuProcesos()
        rafagas = menuRafagas(len(procesoM))
        llegadas = menuLlegadas(len(procesoM))
        ProcesoSJF(procesoM, rafagas, programas, llegadas)

    elif resp1==3:
        procesoM=menuProcesos()
        rafagas=menuRafagas(len(procesoM))
        ProcesoRR(procesoM,rafagas,programas)
    
    elif resp1==4:
        procesoM=menuProcesos()
        rafagas=menuRafagas(len(procesoM))
        llegadas=menuLlegadas(len(procesoM))
        ProcesoRRT(procesoM,rafagas,programas,llegadas)

    elif resp1==5:
        print("\nGracias <3")
    
    else:
        print("\nEliga una opcion correcta")
    
