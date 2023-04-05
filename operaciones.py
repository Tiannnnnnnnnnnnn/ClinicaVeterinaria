#from AtencionCliente import AgendarHora
import csv
 
class Operaciones:
    
    def __init__(self, personal_requerido, salas):
        self.personal_requerido = personal_requerido
        self.salas = salas
    
    def reservarQuirofano():
        salas = input("Ingrese sala para reservar: ")
        personal_requerido = int(input("¿Cuanto personal requiere?"))

        reserva = [personal_requerido, salas]

        with open("reservasQuirofano.csv", 'a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(reserva)
    
    def verReservas():

        with open('reservasQuirofano.csv', 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            
            for reserva in lector_csv:
                print(f"Cantidad de personal: {reserva[0]}, Sala: {reserva[1]}")

    
while True:
    print("1. Hacer una reserva")
    print("2. Ver reservas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        Operaciones.reservarQuirofano()
    elif opcion == "2":
        Operaciones.verReservas()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
