import flet as ft
from anyio.abc import value


def main(page: ft.Page):
    page.title = "Contador"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    titulo = ft.Text('App Contador', size=20, color='blue', weight="bold")
    contenedor = ft.TextField("0", width=60, text_align='center')

    def max_click(e):
        contenedor.value = str(int(contenedor.value)-1)
        page.update()
    def meno_click(e):
        contenedor.value = str(int(contenedor.value) + 1)
        page.update()

    contenido = ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=max_click),
        contenedor,
        ft.IconButton(ft.icons.ADD, on_click=meno_click)
    ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(titulo, contenido)

ft.app(target=main)
