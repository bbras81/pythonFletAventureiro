import flet as ft 

def main(page: ft.Page):
    
    page.title = 'Flet App'

    # #A janela fica sempre por cima das outras paginas
    # page.window_always_on_top = False

    # # #Remove a barra superior do sistema operativo
    # # page.window_title_bar_hidden = False
    # # #Remove os botões da barra do sistema
    # # page.window_frameless = False
    # # #Abre a aplicação em FullScreen
    # # page.window_full_screen = False

    # #definir o tamanho que abre a tela
    # page.window_height = 300
    # # page.window_max_height = 900
    # page.window_width = 600

    # page.window_resizable = False

    # page.window_top = 50
    # page.window_left = 20
    # page.window_movable = True
    # page.window_prevent_close = False
    # page.window_progress_bar = 0.5

    # print(page.platform)
    def page_resize(e):
        print('Tamanho :', page.window_width, page.window_height)

    def window_event(e):
        match e.data:
            case 'moved':
                print('Moveu a pagina')
            case 'resized':
                print('Redimensionoua pagina')
            case 'minimize':
                print('Minimizou')
            case _:
                print('Outra Opção')

    page.on_resize = page_resize

    page.on_event = window_event


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