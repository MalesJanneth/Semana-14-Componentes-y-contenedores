import tkinter as tk
from tkinter import ttk, messagebox


class MainView(tk.Frame):
    def __init__(
        self,
        master,
        restaurante_servicio,
        usuario_actual,
        al_cerrar_sesion
    ):
        super().__init__(master, bg="#eef3f8")

        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion

        self.contenido = None
        self.estado = None

        self.codigo_entry = None
        self.nombre_entry = None
        self.categoria_entry = None
        self.precio_entry = None
        self.stock_entry = None
        self.disponible_var = tk.BooleanVar(value=True)
        self.productos_tree = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "Menu.TButton",
            font=("Arial", 10, "bold"),
            padding=(12, 8)
        )

        estilo.configure(
            "Accion.TButton",
            font=("Arial", 10, "bold"),
            padding=(10, 7)
        )

    def construir_interfaz(self):
        encabezado = tk.Frame(
            self,
            bg="#1f2a44",
            padx=20,
            pady=16
        )
        encabezado.pack(fill="x")

        tk.Label(
            encabezado,
            text="RESTAURANTE",
            bg="#1f2a44",
            fg="#ffffff",
            font=("Arial", 20, "bold")
        ).pack(anchor="w")

        tk.Label(
            encabezado,
            text=f"Bienvenido, {self.usuario_actual.nombre}",
            bg="#1f2a44",
            fg="#dbe5f1",
            font=("Arial", 11)
        ).pack(anchor="w", pady=(4, 0))

        cuerpo = tk.Frame(
            self,
            bg="#eef3f8"
        )
        cuerpo.pack(fill="both", expand=True)

        menu = tk.Frame(
            cuerpo,
            bg="#ffffff",
            width=170,
            padx=12,
            pady=15
        )
        menu.pack(
            side="left",
            fill="y",
            padx=(0, 10)
        )
        menu.pack_propagate(False)

        tk.Label(
            menu,
            text="NAVEGACIÓN",
            bg="#ffffff",
            fg="#516173",
            font=("Arial", 9, "bold")
        ).pack(anchor="w", pady=(0, 12))

        ttk.Button(
            menu,
            text="Inicio",
            command=self.mostrar_inicio,
            style="Menu.TButton"
        ).pack(fill="x", pady=4)

        ttk.Button(
            menu,
            text="Usuarios",
            command=self.mostrar_usuarios,
            style="Menu.TButton"
        ).pack(fill="x", pady=4)

        ttk.Button(
            menu,
            text="Productos",
            command=self.mostrar_productos,
            style="Menu.TButton"
        ).pack(fill="x", pady=4)

        ttk.Button(
            menu,
            text="Cerrar sesión",
            command=self.cerrar_sesion,
            style="Menu.TButton"
        ).pack(fill="x", pady=4)

        area_principal = tk.Frame(
            cuerpo,
            bg="#eef3f8"
        )
        area_principal.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.contenido = tk.Frame(
            area_principal,
            bg="#ffffff",
            padx=20,
            pady=20
        )
        self.contenido.pack(
            fill="both",
            expand=True
        )

        self.estado = tk.Label(
            area_principal,
            text="Seleccione una opción.",
            bg="#eef3f8",
            fg="#516173",
            font=("Arial", 10)
        )
        self.estado.pack(
            fill="x",
            pady=(8, 0)
        )

        self.mostrar_inicio()

    def limpiar_contenido(self):
        if self.contenido is None:
            return

        for widget in self.contenido.winfo_children():
            widget.destroy()

    def actualizar_estado(self, texto):
        if self.estado is not None:
            self.estado.config(text=texto)

    def mostrar_inicio(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Inicio",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 20, "bold")
        ).pack(anchor="w", pady=(0, 10))

        tk.Label(
            self.contenido,
            text="Panel principal del sistema de restaurante.",
            bg="#ffffff",
            fg="#516173",
            font=("Arial", 11)
        ).pack(anchor="w", pady=(0, 20))

        resumen = tk.Frame(
            self.contenido,
            bg="#f7f9fc",
            padx=20,
            pady=20
        )
        resumen.pack(fill="x")

        tk.Label(
            resumen,
            text=f"Usuarios registrados: "
                 f"{self.restaurante_servicio.cantidad_usuarios()}",
            bg="#f7f9fc",
            fg="#243447",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", pady=5)

        tk.Label(
            resumen,
            text=f"Productos registrados: "
                 f"{self.restaurante_servicio.cantidad_productos()}",
            bg="#f7f9fc",
            fg="#243447",
            font=("Arial", 11, "bold")
        ).pack(anchor="w", pady=5)

        self.actualizar_estado("Inicio")

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Usuarios registrados",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 18, "bold")
        ).pack(anchor="w", pady=(0, 15))

        usuarios = self.restaurante_servicio.listar_usuarios()

        if not usuarios:
            tk.Label(
                self.contenido,
                text="No existen usuarios registrados.",
                bg="#ffffff",
                fg="#516173",
                font=("Arial", 11)
            ).pack(anchor="w")

            self.actualizar_estado(
                "No existen usuarios registrados."
            )
            return

        tabla_frame = tk.Frame(
            self.contenido,
            bg="#ffffff"
        )
        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "identificacion",
            "nombre",
            "correo"
        )

        tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        tabla.heading(
            "identificacion",
            text="Identificación"
        )
        tabla.heading(
            "nombre",
            text="Nombre"
        )
        tabla.heading(
            "correo",
            text="Correo"
        )

        tabla.column(
            "identificacion",
            width=130
        )
        tabla.column(
            "nombre",
            width=200
        )
        tabla.column(
            "correo",
            width=250
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=tabla.yview
        )

        tabla.configure(
            yscrollcommand=scrollbar.set
        )

        tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        for usuario in usuarios:
            tabla.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.correo
                )
            )

        self.actualizar_estado(
            f"Usuarios encontrados: {len(usuarios)}"
        )

    def mostrar_productos(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestión de productos",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 18, "bold")
        ).pack(anchor="w", pady=(0, 12))

        formulario = tk.LabelFrame(
            self.contenido,
            text="Datos del producto",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold"),
            padx=12,
            pady=10
        )
        formulario.pack(
            fill="x",
            pady=(0, 12)
        )

        formulario.columnconfigure(1, weight=1)
        formulario.columnconfigure(3, weight=1)

        tk.Label(
            formulario,
            text="Código:",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.codigo_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.codigo_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Nombre:",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.nombre_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.nombre_entry.grid(
            row=0,
            column=3,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Categoría:",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.categoria_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.categoria_entry.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Precio:",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.precio_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.precio_entry.grid(
            row=1,
            column=3,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            formulario,
            text="Stock:",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )

        self.stock_entry = tk.Entry(
            formulario,
            font=("Arial", 10)
        )
        self.stock_entry.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        self.disponible_var = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            formulario,
            text="Producto disponible",
            variable=self.disponible_var
        ).grid(
            row=2,
            column=2,
            columnspan=2,
            sticky="w",
            padx=5,
            pady=5
        )

        botones = tk.Frame(
            self.contenido,
            bg="#ffffff"
        )
        botones.pack(
            fill="x",
            pady=(0, 12)
        )

        ttk.Button(
            botones,
            text="Registrar",
            command=self.registrar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Cargar por código",
            command=self.cargar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Actualizar",
            command=self.actualizar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Eliminar",
            command=self.eliminar_producto,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        ttk.Button(
            botones,
            text="Limpiar",
            command=self.limpiar_formulario,
            style="Accion.TButton"
        ).pack(
            side="left",
            padx=4
        )

        tabla_frame = tk.Frame(
            self.contenido,
            bg="#ffffff"
        )
        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock",
            "disponible"
        )

        self.productos_tree = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.productos_tree.heading(
            "codigo",
            text="Código"
        )
        self.productos_tree.heading(
            "nombre",
            text="Nombre"
        )
        self.productos_tree.heading(
            "categoria",
            text="Categoría"
        )
        self.productos_tree.heading(
            "precio",
            text="Precio"
        )
        self.productos_tree.heading(
            "stock",
            text="Stock"
        )
        self.productos_tree.heading(
            "disponible",
            text="Disponible"
        )

        self.productos_tree.column(
            "codigo",
            width=75
        )
        self.productos_tree.column(
            "nombre",
            width=150
        )
        self.productos_tree.column(
            "categoria",
            width=120
        )
        self.productos_tree.column(
            "precio",
            width=80
        )
        self.productos_tree.column(
            "stock",
            width=70
        )
        self.productos_tree.column(
            "disponible",
            width=90
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.productos_tree.yview
        )

        self.productos_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.productos_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.refrescar_productos()

    def obtener_datos_producto(self):
        return (
            self.codigo_entry.get().strip(),
            self.nombre_entry.get().strip(),
            self.categoria_entry.get().strip(),
            self.precio_entry.get().strip(),
            self.stock_entry.get().strip(),
            self.disponible_var.get()
        )

    def registrar_producto(self):
        datos = self.obtener_datos_producto()

        try:
            self.restaurante_servicio.registrar_producto(
                *datos
            )

            messagebox.showinfo(
                "Producto registrado",
                "El producto se registró correctamente."
            )

            self.limpiar_formulario()
            self.refrescar_productos()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def cargar_producto(self):
        codigo = self.codigo_entry.get().strip()

        if not codigo:
            messagebox.showerror(
                "Error",
                "Ingrese el código del producto."
            )
            return

        producto = (
            self.restaurante_servicio
            .buscar_producto_por_codigo(codigo)
        )

        if producto is None:
            messagebox.showerror(
                "Producto no encontrado",
                "No existe un producto con ese código."
            )
            return

        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, producto.nombre)

        self.categoria_entry.delete(0, tk.END)
        self.categoria_entry.insert(0, producto.categoria)

        self.precio_entry.delete(0, tk.END)
        self.precio_entry.insert(0, producto.precio)

        self.stock_entry.delete(0, tk.END)
        self.stock_entry.insert(0, producto.stock)

        self.disponible_var.set(producto.disponible)

        self.actualizar_estado(
            f"Producto cargado: {producto.codigo}"
        )

    def actualizar_producto(self):
        datos = self.obtener_datos_producto()

        if not datos[0]:
            messagebox.showerror(
                "Error",
                "Ingrese el código del producto."
            )
            return

        try:
            self.restaurante_servicio.actualizar_producto(
                *datos
            )

            messagebox.showinfo(
                "Producto actualizado",
                "El producto se actualizó correctamente."
            )

            self.limpiar_formulario()
            self.refrescar_productos()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def eliminar_producto(self):
        codigo = self.codigo_entry.get().strip()

        if not codigo:
            messagebox.showerror(
                "Error",
                "Ingrese el código del producto."
            )
            return

        producto = (
            self.restaurante_servicio
            .buscar_producto_por_codigo(codigo)
        )

        if producto is None:
            messagebox.showerror(
                "Producto no encontrado",
                "No existe un producto con ese código."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar el producto "
            f"'{producto.nombre}'?"
        )

        if not confirmar:
            return

        try:
            self.restaurante_servicio.eliminar_producto(
                codigo
            )

            messagebox.showinfo(
                "Producto eliminado",
                "El producto se eliminó correctamente."
            )

            self.limpiar_formulario()
            self.refrescar_productos()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def refrescar_productos(self):
        if self.productos_tree is None:
            return

        for item in self.productos_tree.get_children():
            self.productos_tree.delete(item)

        productos = self.restaurante_servicio.listar_productos()

        for producto in productos:
            self.productos_tree.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock,
                    "Sí" if producto.disponible else "No"
                )
            )

        self.actualizar_estado(
            f"Productos encontrados: {len(productos)}"
        )

    def limpiar_formulario(self):
        if self.codigo_entry is not None:
            self.codigo_entry.delete(0, tk.END)

        if self.nombre_entry is not None:
            self.nombre_entry.delete(0, tk.END)

        if self.categoria_entry is not None:
            self.categoria_entry.delete(0, tk.END)

        if self.precio_entry is not None:
            self.precio_entry.delete(0, tk.END)

        if self.stock_entry is not None:
            self.stock_entry.delete(0, tk.END)

        self.disponible_var.set(True)

        self.actualizar_estado(
            "Formulario limpiado."
        )

    def cerrar_sesion(self):
        self.al_cerrar_sesion()