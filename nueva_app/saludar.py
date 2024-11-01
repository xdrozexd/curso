import flet as ft

def main(page: ft.Page):
    page.title = 'Salud App'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    titulo = ft.Text("App de Saludo \n", size=25, color='blue', weight="bold")
    name_input = ft.TextField(hint_text="Ingrese su nombre", width=250, autofocus=True)
    lastn_input = ft.TextField(hint_text="Ingrese su apellida", width=250)

    greeting = ft.Column()

    def saludar_click(e):
        greeting.controls.append(ft.Text(f"Hola {name_input.value} {lastn_input.value}"))
        name_input.value = ""
        lastn_input.value = ""
        name_input.focus()
        page.update()

    colunna = ft.Column([
        titulo,
        name_input,
        lastn_input,
        ft.ElevatedButton("saluda", on_click=saludar_click),
        greeting,

    ])

    page.add(colunna)





ft.app(target=main)