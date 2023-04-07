import csv
 
class Operaciones:
    
    def reservarQuirofano(self):
        salas = input("Ingrese sala para reservar: ")
        personal_requerido = int(input("¿Cuanto personal requiere?: "))

        reserva = [personal_requerido, salas]

        with open("reservasQuirofano.csv", 'a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(reserva)
    
    def verReservas(self):

        with open('reservasQuirofano.csv', 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            
            hay_reservas = False
            
            for reserva in lector_csv:
                if len(reserva) >= 2:
                    print(f"Cantidad de personal: {reserva[0]}, Sala: {reserva[1]}")
                    hay_reservas = True

            if hay_reservas == False:
                print("No hay reservas.")

    
    def mostrarMenuOP(self):
        
        while True:
            
            print("1. Hacer una reserva")
            print("2. Ver reservas")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.reservarQuirofano()
            elif opcion == "2":
                self.verReservas()
            elif opcion == "3":
                break
            else:
                print("Opción inválida. Intente nuevamente.")
