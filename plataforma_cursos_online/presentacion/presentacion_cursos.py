from negocio.negocio_cursos import cargar_cursos
from prettytable import PrettyTable

def mostrar_cursos():
    tabla_cursos = PrettyTable()
    tabla_cursos = cargar_cursos(tabla_cursos)
    print(tabla_cursos)
