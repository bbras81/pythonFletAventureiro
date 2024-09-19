import flet as ft


def main(page: ft.Page):
    

    container = ft.Container(
        # height=100,
        # width=200,
        # bgcolor=ft.colors.BLACK,
        # image_src='https://flet.dev/img/docs/controls/container/container-diagram.png',
        expand=True,
        # margin=ft.margin.only(left=30, top=20, right=60, bottom=40)
        # border=ft.border.all(20, ft.colors.BLUE),
        border_radius=ft.border_radius.all(30),
        # border= ft.border.symmetric(
        #     ft.BorderSide(30, ft.colors.BLUE),
        #     ft.BorderSide(30, ft.colors.GREEN)
        # ),
        content=ft.Row(
            [
                ft.ElevatedButton(text="Teste 1"),
                ft.ElevatedButton(text="Teste 2"),
                ft.ElevatedButton(text="Teste 3"),
                ft.ElevatedButton(text="Teste 4"),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(container)


if __name__ =='__main__':
    ft.app(target = main)