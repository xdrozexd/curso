import flet as ft



def main(page: ft.Page):
    page.title = 'To Do App'

    def boton_click(e):
        page.add(ft.Checkbox(label=input_text.value))
        input_text.value = ''
        page.update()

    input_text = ft.TextField(hint_text="Que quiere hacer hoy", width=350)
    boton_input = ft.ElevatedButton("Agregar", on_click=boton_click)
    fila_input = ft.Row([
        input_text,
        boton_input,
    ])




    page.add(fila_input)


ft.app(target=main)