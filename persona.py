class Persona:
    cod_persona = 0
    nombre = ""
    ap_paterno = ""
    ap_materno = ""
    fecha_nacimiento = ""
   
    def __init__(self, nombre, ap_paterno, ap_materno, fecha_nacimiento):
        self._nombre = nombre
        self._ap_paterno = ap_paterno
        self._ap_materno = ap_materno
        self._fecha_nacimiento = fecha_nacimiento


    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_ap_paterno(self):
        return self._ap_paterno

    def set_ap_paterno(self, ap_paterno):
        self._ap_paterno = ap_paterno

    def get_ap_materno(self):
        return self._ap_materno

    def set_ap_materno(self, ap_materno):
        self._ap_materno = ap_materno

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"Código de Persona: {self._cod_persona}\nNombre: {self._nombre}\nApellido Paterno: {self._ap_paterno}\nApellido Materno: {self._ap_materno}\nFecha de Nacimiento: {self._fecha_nacimiento}"