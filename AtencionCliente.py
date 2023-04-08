from operaciones import Operaciones
from urgencias import Urgencias
import os 

class AgendarHora:
    
    def reservarHora(self):  
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
              
            print("""
            Que tipo de consulta viene el paciente:
            1. Consultas rutinarias
            2. Urgencias
            3. Operaciones 
            4. Volver al menu principal

            """)
            tipo_atencion = input("Seleccione una opcion(numero): ")
        
            os.system('cls' if os.name == 'nt' else 'clear')
        
            if tipo_atencion == "1":
                consulta = Consultas()
                consulta.realizar_consulta()
        
            elif tipo_atencion == "2":
                urgencia = Urgencias()
                urgencia.menu()
        
            elif tipo_atencion == "3":
                operacion = Operaciones()
                operacion.mostrarMenuOP()

            elif tipo_atencion == "4":
                return
        
            else:
                print ("Ingrese una opcion valida")
        



        

