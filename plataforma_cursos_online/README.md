# Campus Virtual - Plataforma de Cursos Online
Réplica del repositorio **IEC_N2_C2_POO** adaptada al dominio de una *plataforma de cursos online*.

Clase 10/10/2026
___

Aplicación de consola desarrollada con Programación Orientada a Objetos, organizada en tres capas independientes:

- `datos/`: modelos ORM (Peewee), repositorios, conexión a base de datos y scripts SQL.
- `negocio/`: reglas de negocio (cargar y crear cursos, comunas, etc.).
- `presentacion/`: menús y tablas en consola (PrettyTable).

## Estructura del proyecto

```
plataforma_cursos_online/
├── main.py
├── requirements.txt
├── .env.example
├── datos/
│   ├── __init__.py
│   ├── auxiliar.py              # Nombre de la app y menú principal
│   ├── conexion.py              # Conexión MySQL (Peewee + decouple)
│   ├── models.py                # Modelos generados con pwiz
│   ├── modelos/                 # Modelos ORM por entidad
│   │   ├── administrador.py
│   │   ├── comuna.py
│   │   ├── curso.py
│   │   ├── direccion.py
│   │   ├── escuela.py
│   │   ├── instructor.py
│   │   └── pais.py
│   ├── repositorio/             # Acceso a datos (CRUD)
│   │   ├── repositorio_comunas.py
│   │   ├── repositorio_cursos.py
│   │   ├── repositorio_instructores.py
│   │   └── repositorio_paises.py
│   └── sql/                     # DDL + datos de ejemplo
├── negocio/
│   ├── negocio_comunas.py
│   └── negocio_cursos.py
└── presentacion/
    ├── menu.py
    ├── menu_instructor.py
    ├── presentacion_comunas.py
    └── presentacion_cursos.py
```

## Equivalencias de dominio

| Proyecto original (Biblioteca) | Réplica (Plataforma de cursos) |
|---|---|
| Biblioteca | Escuela |
| Autor | Instructor |
| Editorial | Programa académico |
| Publicación | Edición de curso |
| Libro | Curso |
| Inventario (copia física) | Comisión (grupo del curso) |
| Préstamo | Matrícula |
| Lector | Estudiante |
| Bibliotecario | Administrador |

## Desarrollo modular

El desarrollo modular es una técnica de diseño de software que consiste en dividir un programa en partes independientes más pequeñas llamadas módulos. Cada módulo se encarga de una funcionalidad específica y se puede comunicar con los demás a través de interfaces bien definidas.

### Beneficios clave

- Facilidad de mantenimiento: Si hay un error, sabes exactamente en qué módulo buscar y puedes arreglarlo sin romper el resto del sistema.
- Reutilización de código: Un mismo módulo (por ejemplo, el sistema de autenticación de usuarios o la conexión a la base de datos) puede usarse en diferentes partes del proyecto o en proyectos futuros.
- Trabajo en equipo: Permite que varios programadores trabajen simultáneamente en diferentes partes del código sin pisarse el trabajo de los demás.
- Escalabilidad: Añadir nuevas funciones es tan fácil como crear un módulo nuevo e integrarlo en el flujo existente.

## Control DataBase
- Para controlar la base de datos necesitamos tener un usuario específico, con permisos explícitos para trabajar sobre una base de datos definida. Esto lo lograremos ejecutando las siguientes sentencias SQL:
```
CREATE USER 'nombre_usuario'@'nombre_servidor' IDENTIFIED WITH caching_sha2_password BY 'contraseña_usuario';
```

- Le asignamos los permisos a nuestra base de datos completa ejecutando la siguiente sentencia SQL:
```
GRANT ALL PRIVILEGES ON campus_virtual.* TO 'nombre_usuario'@'nombre_servidor';
```

- Finalmente debemos grabar esos privilegios con la siguiente sentencia SQL:
```
FLUSH PRIVILEGES;
```

Para conectarnos a la base de datos desde nuestra aplicación usaremos el ORM *Pewee* y el driver de base de datos *Pymysql*.
- *ORM*: Un ORM (Object-Relational Mapping o mapeo objeto-relacional) es una técnica de programación que permite conectar una base de datos relacional con el código de una aplicación *POO*, traduciendo las tablas en clases y los registros en objetos.
- Teniendo completamente creada nuestra estructura de datos, usaremos una herramienta automatizada de Peewee para crear nuestras clases, ejecutando el siguiente comando por terminal:
```
python -m pwiz -e mysql -H localhost -p 3306 -u your_username -P campus_virtual > datos/models.py
```

### Configuración de conexión
Crear el archivo `.env` en la raíz del proyecto a partir de `.env.example`:
```
db=campus_virtual
host=localhost
port=3306
user=nombre_usuario
password=contraseña_usuario
```

### Carga de datos
Ejecutar los scripts de `datos/sql/` en orden (por fecha):
1. `2026.10.10_9.40_ddl_plataforma.sql` → crea la base de datos `campus_virtual` y sus tablas.
2. `2026.10.10_10.00_Insert_paises.sql`
3. `2026.10.10_10.05_Insert_comunas.sql`
4. `2026.10.10_10.10_Insert_idiomas.sql`
5. `2026.10.10_10.15_Insert_estados_ubicaciones.sql`
6. `2026.10.10_10.20_Insert_parametros.sql`
7. `2026.10.10_10.25_Insert_escuelas.sql`
8. `2026.10.10_10.30_Insert_instructores.sql`
9. `2026.10.10_10.35_Insert_cursos.sql`

## Control de dependencias
Para tener un mejor control de las dependencias de nuestros proyectos, es conveniente crear un archivo *requirements.txt* que contendrá la lista de dependencias con sus números de versión, lo que permitirá además hacer una instalación rápida de todas las librerías que contiene.
Si ya tenemos un archivo *requirements.txt* en el directorio principal de nuestro proyecto, ejecutaremos la instalación mediante el siguiente comando por terminal:
```
pip install -r requirements.txt
```

Si no tenemos un archivo, pero ya hemos instalado las librerías, podemos crearlo con el siguiente comando por terminal:
```
pip freeze > requirements.txt
```

## Ejecución
```
python main.py
```
