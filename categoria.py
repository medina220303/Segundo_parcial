class Categoría:
    cod_categoría = 0
    categoria = ""
    
    def __init__(self, cod_categoría, categoria):
        self._cod_categoría = cod_categoría
        self._categoria = categoria

    def get_cod_categoría(self):
        return self._cod_categoría

    def set_cod_categoría(self, cod_categoría):
        self._cod_categoría = cod_categoría

    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def __str__(self):
        return f"Código de Categoría: {self._cod_categoría}\nCategoría: {self._categoria}"



