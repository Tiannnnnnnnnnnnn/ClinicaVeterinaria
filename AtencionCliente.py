



class AgendarHora:
    def __init__(self, veterinario, mascota, tipo_atencion):
        self.veterinario = veterinario
        self.mascota = mascota
        self.tipo_atencion = tipo_atencion
    
    def reservarHora(tipo_atencion):
        
        tipo_atencion = input("Que tipo de consulta viene el paciente: ")
        
        if tipo_atencion == "consulta":
            consulta = Consultas()
            consulta.realizar_consulta()


        if tipo_atencion == "urgencia":
            urgencia = Urgencias()
            urgencia.orden_atencion()

        if tipo_atencion == "operacion":
            operacion = Operacion()
            operacion = reservarQuirofano()

        

