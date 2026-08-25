print("---- Convertidor de segundos a minutos----\n")
seconds = 0
minutes = 0
seconds_left = 0

seconds = int(input("Digite un tiempo en segundos:  \n"))
minutes = seconds / 60
seconds_left = 600 - seconds
if(minutes < 10):
    print("El tiempo en segundos es menor a 10 minutos")
    print(f"Se necesitan {seconds_left} segundos restantes para llegar a 10 min ")
elif(minutes > 10):
    print("El tiempo en segundos es mayor a 10 minutos")
elif(minutes == 10):
    print("El tiempo en segundos es igual a 10 minutos")


