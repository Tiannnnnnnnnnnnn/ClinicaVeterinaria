import csv
import os

class MenuClientes:
    def __init__(self):
        self.clientes = []
        self.cargarClientes()
    
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menuCliente(self):
        

        while True:
            
            self.limpiar_pantalla()

            print("---- Menu Clientes ----")
            print("1. Agregar Cliente")
            print("2. Buscar Cliente")
            print("3. Modificar Cliente")
            print("4. Eliminar Cliente")
            print("5. Lista Clientes")
            print("6. Volver al menu principal")
            opcion = input("Ingrese una opcion: ")

            if opcion == "1":
                self.agregarCliente()
            elif opcion == "2":
                self.buscarCliente()
            elif opcion == "3":
                self.modificarCliente()
            elif opcion == "4":
                self.eliminarCliente()
            elif opcion == "5":
                self.listaClientes()
            elif opcion == "6":
                return
            else:
                print("Ingrese una opcion(numero): ")

    def cargarClientes(self):
        try:
            with open("cliente.csv", newline='') as archivo:
                reader = csv.reader(archivo)
                next(reader) # saltar la primera fila que contiene los encabezados
                for row in reader:
                    self.clientes.append(row)
        except FileNotFoundError:
            print("Archivo 'cliente.csv' no encontrado")

    def guardarClientes(self):
            with open("cliente.csv", "w", newline='') as archivo:
                writer = csv.writer(archivo)
                writer.writerow(["ID", "Nombre", "Apellido_paterno", "Apellido_materno", "Genero", "Fecha_nacimiento", "Rut", "Email", "Telefono", "Domicilio", "Mascotas", "Historial"])
                for cliente in self.clientes:
                    writer.writerow(cliente)

    def agregarCliente(self):
        while True:    
            print("---- Agregar Cliente ----")
            id = input("ID: ")
            nombre = input("Nombre: ")
            Apellido_paterno = input("Apellido paterno: ")
            Apellido_materno = input("Apellido materno: ")
            genero = input("Genero: ")
            Fecha_nacimiento = input("Fecha Nacimiento (AÑO/MES/DIA): ")
            rut = input("Rut: ")
            email = input("Email: ")
            telefono = input("Telefono: ")
            domicilio = input("Domicilio: ")
            mascotas = input("Mascota/s: ")
            Historial = input("ninguno")
            self.clientes.append([id, nombre, Apellido_paterno, Apellido_materno, rut, email, telefono, domicilio, mascotas, Historial])
            self.guardarClientes()
            print("Cliente agregado con exito")
            opcion = input("¿Desea agregar a otro cliente? 1.si 2.no ")
            if opcion == "1":
                self.limpiar_pantalla()
            elif opcion == "2":
                break
            else:
                print("opcion invalida, intente ingresando 1 o 2")

    def buscarCliente(self):

        print("---- Buscar Cliente ----")
        id = input("ID: ")
        while True:    
            for cliente in self.clientes:
                if cliente[0] == id:
                    print("ID:", cliente[0])
                    print("Nombre:", cliente[1], cliente[2], cliente[3])
                    print("RUT: ", cliente[4])
                    print("Email:", cliente[5])
                    print("Telefono:", cliente[6])
                    print("Domicilio: ", cliente[7])
                    print("Mascota/s: ", cliente[8])
                    print("Historial: ", cliente[9])
                    opcion = input("¿Desea buscar a otro cliente? 1.si 2.no ")
                    if opcion == "1":
                        self.limpiar_pantalla()
                    elif opcion == "2":
                        break
                    else:
                        print("opcion invalida, intente ingresando 1 o 2")
            print("Cliente no encontrado")

    def modificarCliente(self):
        self.limpiar_pantalla()

        print("---- Modificar Cliente ----")
        id = input("ID: ")
        for cliente in self.clientes:
            if cliente[0] == id:
                print("ID:", cliente[0])
                print("1. Nombre:", cliente[1])
                print("2. Apellido paterno: ", cliente[2])
                print("3. Apellido materno: ", cliente[3])
                print("4.RUT: ", cliente[4])
                print("5.Email:", cliente[5])
                print("6.Telefono:", cliente[6])
                print("7.Domicilio: ", cliente[7])
                print("8.Mascota/s: ", cliente[8])
                print("9.Historial: ", cliente[9])

                opcion = input("Ingrese el numero del campo que desea modificar: ")
                if opcion == "1":
                    cliente[1] = input("Nuevo Nombre: ")
                elif opcion == "2":
                    cliente[2] = input("Nuevo Apellido paterno: ")
                elif opcion == "3":
                    cliente[3] = input("Nuevo Apellido materno: ")
                elif opcion == "4":
                    cliente[4] = input("Nuevo RUT: ")
                elif opcion == "5":
                    cliente[5] = input("Nuevo Email: ")
                elif opcion == "6":
                    cliente[6] = input("Nuevo Telefono: ")
                elif opcion == "7":
                    cliente[7] = input("Nuevo Domicilio: ")
                elif opcion == "8":
                    cliente[8] = input("Nueva Mascota: ")
                elif opcion == "9":
                    cliente[9] = input("Nuevo historial: ")

                self.guardarClientes()
    
    def listaClientes(self):
        print("Lista de Clientes:")
        for cliente in self.clientes:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Mascota/s: {cliente[8]}")
            
        print("Para mas informacion busque al cliente en la seleccion buscar clientes.")
        input("Presione enter para continuar...")

    def eliminarCliente(self):
        self.limpiar_pantalla()

        print("---- Eliminar Cliente ----")
        print("Para eliminar un cliente proporcione su ID")
        print("Si quiere regresar presione enter sin ingresar un dato.")
        id = input("ID: ")
        for i, cliente in enumerate(self.clientes):
            if cliente[0] == id:
                del self.clientes[i]
                self.guardarClientes()
                print("Cliente eliminado con éxito")
                return
            elif id == none:
                return
        print("Cliente no encontrado")
