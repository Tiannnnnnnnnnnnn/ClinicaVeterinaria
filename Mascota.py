class Mascota:
    def __init__(self,id,nombre,especie,raza,fecha_nacimiento,sexo,peso,tamanho,volumen,ficha_medica):
        self._id = id
        self._nombre = nombre
        self._especie = especie
        self._raza = raza
        self._fecha_nacimiento = fecha_nacimiento
        self._sexo = sexo
        self._peso = peso
        self._tamanho = tamanho
        self._volumen = volumen
        self._ficha_medica = list(ficha_medica)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,nuevo_id):
        self._id = nuevo_id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def especie(self):
        return self._especie
    
    @especie.setter
    def especie(self,nueva_especie):
        self._especie = nueva_especie

    @property
    def raza(self):
        return self._raza
    
    @raza.setter
    def raza(self,nueva_raza):
        self._raza = nueva_raza
    
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self,nueva_fecha):
        self._fecha_nacimiento = nueva_fecha

    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self,nuevo_sexo):
        self._sexo = nuevo_sexo

    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self,nuevo_peso):
        self._peso = nuevo_peso

    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self,nuevo_tamanho):
        self._tamanho = nuevo_tamanho
    
    @property
    def volumen(self):
        return self._volumen
    
    @volumen.setter
    def volumen(self,nuevo_volumen):
        self._volumen = nuevo_volumen

    def __str__(self):
        return f"""
        Animal [{self._id}]
        Nombre: {self._nombre}
        Especie: {self._especie}
        Raza: {self._raza}
        Fecha Nacimiento: {self._fecha_nacimiento}
        Sexo: {self._sexo}
        Peso: {self._peso}
        Tamanho: {self._tamanho}
        Volumen: {self._volumen}
        Ficha medica: {self._ficha_medica}"""
    
if __name__ == "__main__":
    PerroJuan = Mascota(1,"Juan","Perro","Pudul","10/11/2006","Macho","5kg",1.33,33,1)

    print(PerroJuan)