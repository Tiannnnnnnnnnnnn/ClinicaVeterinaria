class Cliente:
    def __init__(self, id, nombres, apellido_materno, apellido_paterno, genero, fecha_nacimiento, rut, email, telefono, domicilio, mascotas, historial):
        self.id = id
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.genero = genero
        self.fecha_nacimiento = fecha_nacimiento
        self.rut = rut
        self.email = email
        self.telefono = telefono
        self.domicilio = domicilio
        self.mascotas = mascotas
        self.historial = historial
    
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombres(self):
        return self.nombres

    def set_nombres(self, nombres):
        self.nombres = nombres
    
    def get_apellido_materno(self):
        return self.apellido_materno
    
    def set_apellido_materno(self, apellido_materno):
        self.apellido_materno = apellido_materno
    
    def get_apellido_paterno(self):
        return self.apellido_paterno
    
    def set_apellido_paterno(self, apellido_paterno):
        self.apellido_paterno
        
    def get_genero(self):
        return self._genero

    def set_genero(self, genero):
        self._genero = genero

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def get_rut(self):
        return self._rut

    def set_rut(self, rut):
        self._rut = rut

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_domicilio(self):
        return self._domicilio

    def set_domicilio(self, domicilio):
        self._domicilio = domicilio

    def get_mascotas(self):
        return self._mascotas

    def set_mascotas(self, mascotas):
        self._mascotas = mascotas

    def get_historial(self):
        return self._historial

    def set_historial(self, historial):
        self._historial = historial

    def __str__(self):
        return """
        Nombre: {self.nombres} {self.apellido_materno} {self.apellido_paterno}
        Genero: {self.genero}
        Fecha nacimiento: {self.fecha_nacimiento}
        Rut: {self.rut}
        Contacto: {self.email} {self.domicilio} {self.telefono}
        Mascotas: {self.mascotas}
        Historial: {self.historial}
        """
        
