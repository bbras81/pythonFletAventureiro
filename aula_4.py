import flet as ft

def main(page: ft.Page):
    icon_1 = ft.Icon(name=ft.icons.FAVORITE, color=ft.colors.PINK)
    icon_2 = ft.Icon(name=ft.icons.AUDIOTRACK, color=ft.colors.GREEN, size=300)
    icon_3 = ft.Icon(name=ft.icons.BEACH_ACCESS, color=ft.colors.BLUE, size=300)
    icon_4 = ft.Icon(name='settings', tooltip='Configurações', size=100)
    page.add(icon_1, icon_2, icon_3, icon_4)

ft.app(target=main, assets_dir='assets')