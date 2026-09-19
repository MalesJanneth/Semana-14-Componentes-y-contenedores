import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class AplicacionRestaurante:
    """
    Clase principal de la interfaz gráfica.
    """

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Restaurante - Tkinter")
        self.root.geometry("920x560")
        self.root.minsize(780, 500)

        ruta_base = Path(__file__).resolve().parent

        archivo_servicio = ArchivoServicio(
            ruta_base / "datos"
        )

        self.restaurante_servicio = RestauranteServicio(
            archivo_servicio
        )

        self.vista_actual = None

        self.mostrar_login()

    def cambiar_vista(self, nueva_vista):
        """
        Cambia la vista actual dentro de la misma ventana.
        """

        if self.vista_actual is not None:
            self.vista_actual.destroy()

        self.vista_actual = nueva_vista

        self.vista_actual.pack(
            fill="both",
            expand=True
        )

    def mostrar_login(self):
        """
        Muestra la pantalla de inicio de sesión.
        """

        vista = LoginView(
            self.root,
            self.restaurante_servicio,
            self.mostrar_interfaz_principal
        )

        self.cambiar_vista(vista)

    def mostrar_interfaz_principal(self, usuario_actual):
        """
        Muestra la interfaz principal después
        de validar correctamente el acceso.
        """

        vista = MainView(
            self.root,
            self.restaurante_servicio,
            usuario_actual,
            self.mostrar_login
        )

        self.cambiar_vista(vista)

    def ejecutar(self):
        """
        Inicia el ciclo principal de Tkinter.
        """

        self.root.mainloop()


if __name__ == "__main__":
    app = AplicacionRestaurante()
    app.ejecutar()