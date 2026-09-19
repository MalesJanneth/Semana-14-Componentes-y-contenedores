# Restaurante App - Semana 13

**Estudiante:** Janneth Talía Males Conejo

## Objetivo

Esta versión de `restaurante_app` representa la transición de una aplicación de consola a una interfaz gráfica utilizando **Tkinter**.

En esta etapa se trabaja únicamente con la información básica de **usuarios y productos**. La funcionalidad de ventas queda pendiente para una semana posterior.

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
    ├── main.py
    └── README.md

## Responsabilidades

- **Modelos:** representan los productos y usuarios del restaurante.
- **ArchivoServicio:** se encarga de leer la información almacenada en archivos JSON.
- **RestauranteServicio:** carga los datos y proporciona las operaciones de validación y consulta utilizadas por la interfaz.
- **LoginView:** permite ingresar usuario y contraseña y muestra mensajes cuando los datos son incorrectos.
- **MainView:** muestra la información de productos y usuarios después de iniciar sesión. La opción de ventas se encuentra pendiente.
- **main.py:** crea la ventana principal de Tkinter, prepara los servicios y coordina el cambio entre las vistas.

## Flujo de la aplicación

    Inicio
      ↓
    main.py
      ↓
    LoginView
      ↓
    Usuario y contraseña
      ↓
    RestauranteServicio valida el acceso
      ↓
    MainView
      ↓
    Productos | Usuarios | Ventas (pendiente)
      ↓
    Cerrar sesión
      ↓
    LoginView

## Ejecución

Desde la carpeta del proyecto ejecutar:

    python restaurante_app/main.py

La aplicación inicia mostrando la pantalla de inicio de sesión. Después de ingresar credenciales válidas, se puede consultar la información registrada de productos y usuarios.