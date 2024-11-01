import flet as ft
from time import sleep


def main(page: ft.Page):
    page.title = 'Counter app'
    page.theme_mode= ft.ThemeMode.DARK
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    titulo = ft.Text('Nuestra aplicacion', size=30, color='red')
    text = ft.Text()
    page.add(titulo, text)

    for i in range(1, 11):
        text.value = f'Counter {str(i)}'
        page.update()
        sleep(1)


ft.app(main)
