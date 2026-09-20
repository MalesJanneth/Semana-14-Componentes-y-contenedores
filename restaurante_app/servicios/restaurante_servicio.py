from modelos.producto import Producto
from modelos.usuario import Usuario

class RestauranteServicio:
    def __init__(self, archivo_servicio):
        self.archivo_servicio = archivo_servicio
        self.usuarios = []
        self.productos = []
        self.cargar_datos()

    def cargar_datos(self):
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        productos_json = self.archivo_servicio.leer_json("productos.json")

        self.usuarios = [
            Usuario(
                datos.get("identificacion", ""),
                datos.get("nombre", ""),
                datos.get("correo", ""),
                datos.get("usuario", ""),
                datos.get(
                    "contrasena",
                    datos.get("contraseña", "")
                ),
            )
            for datos in usuarios_json
        ]

        self.productos = [
            Producto(
                datos.get("codigo", ""),
                datos.get("nombre", ""),
                datos.get("categoria", ""),
                datos.get("precio", 0),
                datos.get("stock", 0),
                datos.get("disponible", True),
            )
            for datos in productos_json
        ]

    def validar_acceso(self, usuario, contrasena):
        for usuario_registrado in self.usuarios:
            if (
                usuario_registrado.usuario == usuario
                and usuario_registrado.contrasena == contrasena
            ):
                return usuario_registrado
        return None

    def cantidad_usuarios(self):
        return len(self.usuarios)

    def cantidad_productos(self):
        return len(self.productos)

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos

    def guardar_productos(self):
            datos = [
                producto.a_diccionario() 
                for producto in self.productos
            ]
            self.archivo_servicio.escribir_json(
                "productos.json", datos
            )

    def buscar_producto_por_codigo(self, codigo):
        codigo = codigo.strip()

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None
    
    def registrar_producto(self, codigo, nombre, categoria, precio, stock, disponible):
        codigo = codigo.strip()

        if self.buscar_producto_por_codigo(codigo):
            raise ValueError(f"El producto con ese código ya existe.")

        try:
            precio = float(precio) 
            stock = int (stock)
        except (TypeError, ValueError):
            raise ValueError(
                "El precio debe ser mayor o igual a 0."
            )
        if precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero")
        
        if stock < 0:
            raise ValueError("El stock debe ser entero mayor o igual a cero")
        
        nuevo_producto = Producto(codigo, nombre, categoria, precio, stock, disponible)
        self.productos.append(nuevo_producto)
        self.guardar_productos()
        return nuevo_producto

    def actualizar_producto(self, codigo, nombre, categoria, precio, stock, disponible):
        codigo = codigo.strip()
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            raise ValueError(f"El producto con ese código no existe.")

        try:
            precio = float(precio)
            stock = int(stock)
        except (TypeError, ValueError):
            raise ValueError(
                "El precio debe ser un número mayor o igual a cero."
            )

        if precio < 0:
            raise ValueError("l precio debe ser mayor o igual a cero")

        if stock < 0:
            raise ValueError("El sock debe ser un entero mayor o igual a cero")

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock
        producto.disponible = disponible
        self.guardar_productos()
        return producto

    def eliminar_producto(self, codigo):
        codigo = codigo.strip()
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            raise ValueError(f"El producto con ese código no existe.")
        
        self.productos.remove(producto)
        self.guardar_productos()