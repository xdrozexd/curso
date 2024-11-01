import flet as ft

def main(page: ft.Page):
    page.title = 'Say hello'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    text_input = ft.TextField(label='Enter Name', width=300)
    text_column = ft.Column()

    def say_click(e):
        if not text_input.value:
            text_input.error_text = 'Please Enter something'
            page.update()
        else:
            page.clean()
            text_column.controls.append(ft.Text(f"Hello {text_input.value}", size=20, color='red', weight='bold'))
            page.add(text_column)



    page.add(
        text_input,
        ft.ElevatedButton('Say Hello', on_click=say_click),
    )

ft.app(target=main)