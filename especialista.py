class Especialista:
    def __init__(self, nombre, experiencia, especialidad, contacto):
        self.nombre = nombre
        self.experiencia = experiencia
        self.especialidad = especialidad
        self.contacto = contacto

    def __str__(self):
        return """
        Especialista: {self.nombre}
        Años de experiencia: {self.experiencia}
        Especialidad: {self.especialidad}
        Contacto: {self.contacto}"""



