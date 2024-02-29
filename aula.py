import flet as ft 

def main(page: ft.Page):
    page.title = 'Flet App'

    page.bgcolor = 'purple'
    page.bgcolor = '#f0fafa'
    page.bgcolor = ft.colors.PURPLE
    
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
    
    page.padding = 20
    # page.padding = ft.padding.symmetric(vertical=10, horizontal=30)
    # page.padding = ft.padding.only(top=10, left=56, right=40, bottom=30)

    #equivale o margin do html
    page.spacing = 300


    page.add(
        ft.Text(value="Olá Mundo"),
        ft.Container(ft.Text(value="Ola Mundo!"),bgcolor='white'),
        ft.Container(ft.Text(value="Ola Mundo!"),bgcolor='white'),
        ft.Container(ft.Text(value="Ola Mundo!"),bgcolor='white'),
        ft.Container(ft.Text(value="Ola Mundo!"),bgcolor='white'),
    )
    
    page.update()
    
ft.app(target=main)