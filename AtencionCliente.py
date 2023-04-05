
class AgendarHora:
    def __init__(self, veterinario, mascota, tipo_atencion):
        self.veterinario = veterinario
        self.mascota = mascota
        self.tipo_atencion = tipo_atencion
    
    def reservarHora():
        
        tipo_atencion = input("""Que tipo de consulta viene el paciente:
        1. Consultas
        2. Urgencias
        3. Operaciones
        Seleccione un numero...   
        """)
        
        if tipo_atencion == "1":
            consulta = Consultas()
            consulta.realizar_consulta()

        if tipo_atencion == "2":
            urgencia = Urgencias()
            urgencia.orden_atencion()

        if tipo_atencion == "3":
            operacion = operaciones()
            operacion.reservarQuirofano()

    def mostrarMenu():

        while True:
            opcion = input("""¿Quiere agendar una hora? Responda si o no  
            """)
            if opcion == "si":
                AgendarHora.reservarHora()
            elif opcion == "no":
                brake
            else:
                print("Opción inválida. Intente nuevamente.")


        

