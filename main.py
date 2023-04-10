from AtencionCliente import AgendarHora
from cliente import MenuClientes
import os #para poder hacer clear

menuAgendarHora = AgendarHora()

def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        print("Bienvenido a la aplicaccion de la clinica veterinaria")
        print("""
        1.Consultas
        2.Registrar/modificar Cliente
        3.
        """)
        opcion = input("Porfavor, a continuacion seleccione una opcion (numero): ")
    
        limpiar_pantalla()

        if opcion == "1":
            menuAgendarHora.reservarHora()
        elif opcion == "2":
            cliente = MenuClientes()
            cliente.menuCliente()
        else:
            print("Ingrese una opcion valida")


if __name__ == "__main__":
    menu_principal()

    
    

