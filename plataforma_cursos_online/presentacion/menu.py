import sys
from datos import nombre_app,version_app,main_menu
from presentacion.presentacion_comunas import mostrar_comunas
from presentacion.presentacion_cursos import mostrar_cursos

def menu_principal():
    print(f'{nombre_app} {version_app}')
    print('='*len(nombre_app) + "=" + '='*len(version_app))

    while True:
        for clave,valor in main_menu.items():
            print(f'[{clave}] - {valor}')

        opcion_usuario = input('Ingrese una opción [1-4]: ')

        if opcion_usuario == '1':
            mostrar_comunas()
        elif opcion_usuario == '2':
            mostrar_cursos()
        elif opcion_usuario == '3':
            print('Seleccionada opcion 3')
        elif opcion_usuario == '4':
            print('Saliendo de Sistema')
            sys.exit()
        else:
            print('Opción Ingresada NO corresponde...\nIngrese nuevamente.')
