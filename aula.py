import flet as ft 

def main(page: ft.Page):
    page.bgcolor = 'amber'
    page.bgcolor = ft.colors.AMBER_500
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.add(
        ft.Text(value="Olá Mundo "),
        ft.Container(ft.Text(value="Ola Mundo!"),bgcolor='black')
    )
    
    page.update()
    
ft.app(target=main)