from operaciones import Operaciones


class AgendarHora:
    
    def reservarHora(self):
        
        tipo_atencion = input("""
        Que tipo de consulta viene el paciente:
        1. Consultas rutinarias
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
            operacion = Operaciones()
            operacion.mostrarMenuOP()



        

