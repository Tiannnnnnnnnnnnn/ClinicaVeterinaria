



class AtencionCliente:
    def __init__(self, urgencias, consultas, operaciones, formato_atencion):
        self.urgencias = urgencias
        self.consultas = consultas
        self.operaciones = operaciones
        self.formato_atencion = formato_atencion
    
    def escoger(opcion):
        opcion = input("Que tipo de consulta viene el paciente: ")
        
        if opcion == "consulta":
            consulta = Consultas()
            consulta.realizar_consulta()


        if opcion == "urgencia":
            urgencia = Urgencias()
            urgencia.orden_atencion()

        if opcion == "operacion":
            operacion = Operacion()
            operacion = reservar_hora()

        

