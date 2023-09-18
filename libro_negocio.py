from modelo.libro import Libro

class LibroNegocio:
    
    libros = []
    
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def editar_libro(self, cod_libro, nuevo_titulo, nuevo_anio, nuevo_tomo):
        for libro in self.libros:
            if libro.get_cod_libro() == cod_libro:
                libro.set_titulo(nuevo_titulo)
                libro.set_anio(nuevo_anio)
                libro.set_tomo(nuevo_tomo)
                return True
        return False

    def eliminar_libro(self, cod_libro):
        for libro in self.libros:
            if libro.get_cod_libro() == cod_libro:
                self.libros.remove(libro)
                return True
        return False
   
    def reporte_libros(self):
        if not self.libros:
            print("No hay libros en la lista.")
        else:
            print("Reporte de Libros:")
            for libro in self.libros:
                print(f"Código de Libro: {libro.get_cod_libro()}")
                print(f"Título: {libro.get_titulo()}")
                print(f"Año: {libro.get_año()}")
                print(f"Tomo: {libro.get_tomo()}")
                print('-' * 30)
         

mantenimiento = MantenimientoLibros()

libro1 = Libro(1001, "Cien años de soledad", 1967, 1)
libro2 = Libro(1002, "El amor en los tiempos del cólera", 1985, 1)

mantenimiento.agregar_libro(libro1)
mantenimiento.agregar_libro(libro2)

print("Libros existentes:")
mantenimiento.reporte_libros()

print("\nEditar libro con código 1001:")
if mantenimiento.editar_libro(1001, "Cien años de soledad - Edición especial", 1970, 2):
    print("Libro editado exitosamente.")
else:
    print("Libro no encontrado.")

print("\nEliminar libro con código 1002:")
if mantenimiento.eliminar_libro(1002):
    print("Libro eliminado exitosamente.")
else:
    print("Libro no encontrado.")

print("\nLibros actualizados:")
mantenimiento.reporte_libros()