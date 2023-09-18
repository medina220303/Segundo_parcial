from modelo.autor import Autor
from modelo.categoria import Categoria

class Libro:
    def __init__(self, cod_libro, titulo, anio, tomo):
        self._cod_libro = cod_libro
        self._titulo = titulo
        self._anio = anio
        self._tomo = tomo

    def get_cod_libro(self):
        return self._cod_libro

    def set_cod_libro(self, cod_libro):
        self._cod_libro = cod_libro

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_anio(self):
        return self._anio

    def set_anio(self, anio):
        self._anio = anio

    def get_tomo(self):
        return self._tomo

    def set_tomo(self, tomo):
        self._tomo = tomo
    
    def asignar_autor(self, autor):
        self.autor = autor

    def mostrar_autor(self):
        return f'Autor: {self.autor}'
    
    def asignar_categoria(self, categoria):
        self.categoria = categoria

    def mostrar_categoria(self):
        return f'Categoría: {self.categoria}'
    
    def __str__(self):
        return f"Código de Libro: {self._cod_libro}\nTítulo: {self._titulo}\nAño: {self._anio}\nTomo: {self._tomo}"

