import flet as ft

#Aula de Text

def main(page: ft.Page):
    page.fonts = {
        # 'Kanit': 'Colocar o path da Font ou o url',
        'kodeMono' : 'fonts/KodeMono-VariableFont_wght.ttf'

    }
    texto1 = ft.Text(
        value='Olá Mundo seja bem vindo ao curso de Flet do Programador Aventureiro',
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        # font_family='kodeMono',
        italic=True,
        # max_lines=2,
        # overflow=ft.TextOverflow.ELLIPSIS
        # no_wrap=True,
        size=40,
        text_align=ft.TextAlign.JUSTIFY,
        weight=ft.FontWeight.W_100
    )
    linkStyle = ft.TextStyle(color=ft.colors.BLUE)
    titleStyle = ft.TextStyle(
        bgcolor=ft.colors.AMBER,
        color=ft.colors.RED,

        )

    texto2 = ft.Text(
        spans= [
            ft.TextSpan(text='Texto com link ', style=linkStyle, url='https://google.com'),
            ft.TextSpan(text='continuação do texto', ),
            ft.TextSpan(text='Texto em destaque', style=titleStyle),
        ],
        size=70
    )

    page.add(texto1, texto2)

    

ft.app(target=main, assets_dir= 'assets' )