# Restaurante App - Semana 14

**Estudiante:** Janneth Talía Males Conejo

## Propósito

En la Semana 14 se mejora la aplicación `restaurante_app` mediante una interfaz gráfica desarrollada con **Tkinter y ttk**. Se organizan los elementos utilizando componentes y contenedores para mejorar la presentación y el uso de la aplicación.

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

## Componentes y contenedores

Se utilizan componentes de **Tkinter y ttk**, entre ellos:

- `Frame`
- `LabelFrame`
- `Label`
- `Entry`
- `Button`
- `Checkbutton`
- `Treeview`
- `Scrollbar`

Los contenedores permiten organizar el formulario de productos, los botones y las tablas de información.

## Mejoras realizadas

- Organización de la interfaz mediante contenedores.
- Separación del formulario y la presentación de información.
- Uso de tablas para consultar usuarios y productos.
- Uso de botones para ejecutar las operaciones.
- Actualización de la información después de realizar cambios.
- Interfaz más ordenada y fácil de utilizar.

## Operaciones sobre productos

La aplicación permite:

- Registrar productos.
- Consultar productos por código.
- Actualizar productos.
- Eliminar productos.
- Consultar los productos registrados.

## Persistencia

La información se almacena en archivos **JSON** ubicados en la carpeta `datos`.

`ArchivoServicio` se encarga de la lectura y escritura de los archivos, mientras que `RestauranteServicio` gestiona las operaciones de la aplicación.

## Ejecución

Para ejecutar el proyecto:

1. Abrir PowerShell en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

    python restaurante_app/main.py

La aplicación inicia con la pantalla de inicio de sesión y, después de ingresar correctamente, permite acceder a las funciones principales.