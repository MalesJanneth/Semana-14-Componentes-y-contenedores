# Restaurante App - Semana 14

**Estudiante:** Janneth Talía Males Conejo

## Objetivo

Esta versión de `restaurante_app` mejora la interfaz gráfica desarrollada anteriormente utilizando **Tkinter y ttk**.

En esta etapa se trabajan **componentes y contenedores** para organizar mejor la interfaz y facilitar la gestión de usuarios y productos.

## Estructura del proyecto

    restaurante_app/
    ├── datos/
    │   ├── productos.json
    │   └── usuarios.json
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   └── usuario.py
    ├── servicios/
    │   ├── __init__.py
    │   ├── archivo_servicio.py
    │   └── restaurante_servicio.py
    ├── ui/
    │   ├── __init__.py
    │   ├── login_view.py
    │   └── main_view.py
    ├── assets/
    │   └── logo/
    ├── main.py
    └── README.md

## Componentes y responsabilidades

- **Modelos:** representan los productos y usuarios del restaurante.
- **ArchivoServicio:** se encarga de leer y guardar la información en archivos JSON.
- **RestauranteServicio:** contiene las operaciones y validaciones del restaurante.
- **LoginView:** permite ingresar usuario y contraseña.
- **MainView:** permite consultar usuarios y gestionar productos.
- **main.py:** crea la ventana principal y coordina las vistas.

## Funcionalidades

- Inicio de sesión.
- Consulta de usuarios.
- Registro de productos.
- Consulta de productos por código.
- Actualización de productos.
- Eliminación de productos.
- Persistencia de datos mediante archivos JSON.

## Interfaz gráfica

Se utilizan componentes de **Tkinter y ttk**, como `Frame`, `LabelFrame`, `Entry`, `Button`, `Checkbutton`, `Treeview` y `Scrollbar`.

Los componentes se organizan mediante contenedores para separar formularios, botones y tablas de información.

## Flujo de la aplicación

    Inicio
       ↓
    main.py
       ↓
    LoginView
       ↓
    RestauranteServicio valida el acceso
       ↓
    MainView
       ↓
    Usuarios | Productos
       ↓
    Operaciones de productos
       ↓
    Cerrar sesión

## Ejecución

Desde la carpeta del proyecto ejecutar:

    python restaurante_app/main.py

La aplicación inicia mostrando la pantalla de inicio de sesión. Después de ingresar credenciales válidas, se pueden consultar usuarios y realizar las operaciones de registro, consulta, actualización y eliminación de productos.