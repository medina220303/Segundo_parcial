from modelo.persona import Persona

class Autor(Persona):
    cod_autor = 0
    pais = ""
    editorial = ""
    
    def __init__(self, cod_autor, nombre, ap_paterno, ap_materno, fecha_nacimiento, pais, editorial):
        super().__init__(cod_autor, nombre, ap_paterno, ap_materno, fecha_nacimiento)
        self._cod_autor = cod_autor
        self._pais = pais
        self._editorial = editorial

    def get_cod_autor(self):
        return self._cod_autor

    def set_cod_autor(self, cod_autor):
        self._cod_autor = cod_autor

    def get_pais(self):
        return self._pais

    def set_pais(self, pais):
        self._pais = pais

    def get_editorial(self):
        return self._editorial

    def set_editorial(self, editorial):
        self._editorial = editorial

    def __str__(self):
        return f"Código de Autor: {self._cod_autor}\nNombre: {self._nombre}\nApellido Paterno: {self._ap_paterno}\nApellido Materno: {self._ap_materno}\nFecha de Nacimiento: {self._fecha_nacimiento}\nPaís: {self._pais}\nEditorial: {self._editorial}"

