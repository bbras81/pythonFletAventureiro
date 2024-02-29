import flet as ft

def main(page: ft.Page):
    img = ft.Image(
        src='images/Python-Symbol.png',
        height=1000,
        width=400,
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.REPEAT,
        tooltip='Logo do Python'
    )

    page.add(img)

ft.app(target=main, assets_dir='assets')