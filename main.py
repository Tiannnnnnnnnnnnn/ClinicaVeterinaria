from AtencionCliente import AgendarHora

menuAgendarHora = AgendarHora()

if __name__ == "__main__":

    print("Bienvenido a la aplicaccion de la clinica veterinaria...")
    print("""
    1.Consultas
    2.
    3. """)
    opcion = input("Porfavor, a continuacion seleccione la opcion deseada: ")
    if opcion == "1":
        menuAgendarHora.reservarHora()
    

