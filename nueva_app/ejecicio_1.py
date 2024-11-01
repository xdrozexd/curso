import flet as ft
from flet_core import MainAxisAlignment
from flet_core.border_radius import horizontal
from requests.packages import target


def main(page: ft.Page):
    page.title = 'Ejercicio Contador'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    titulo = ft.Text('Ejercicio Contador', size=25, color='blue', weight='bold')


    def max_clik(e):
        input_pets.value = int(input_pets.value) +5
        if input_pets.value == 25:
            clear_clik(e)
        page.update()

    def minu_click(e):
        input_cruelty.value = int(input_cruelty.value) - 5
        page.update()

    def clear_clik(e):
        input_pets.value = '0'
        page.update()
        input_cruelty.value = '100'
        page.update()

    icono_pets = ft.IconButton(icon=ft.icons.PETS, on_click=max_clik)
    icono_cruelty = ft.IconButton(icon=ft.icons.CRUELTY_FREE, on_click=minu_click)
    input_pets = ft.TextField(value='0', width=60, text_align='center')
    input_cruelty = ft.TextField(value='100', width=60, text_align='center')
    icono_clear = ft.ElevatedButton("Limpiar", on_click=clear_clik)

    fila_contenido = ft.Row([
        icono_pets,
        input_pets,
        input_cruelty,
        icono_cruelty,


    ],alignment=MainAxisAlignment.CENTER
    )

    page.add(titulo, fila_contenido, icono_clear)



ft.app(target=main)