import flet as ft

def main(page: ft.Page):

# Aula de Row
    row1 = ft.Row(
        controls=[
            ft.ElevatedButton(text="1", bgcolor=ft.colors.RED, color=ft.colors.WHITE ),
            ft.ElevatedButton(text="1", bgcolor=ft.colors.RED, color=ft.colors.WHITE ),
            ft.ElevatedButton(text="1", bgcolor=ft.colors.RED, color=ft.colors.WHITE ),

            # ft.ElevatedButton(text="1", bgcolor=ft.colors.RED, color=ft.colors.WHITE ),
            # ft.ElevatedButton(text="1", bgcolor=ft.colors.RED, color=ft.colors.WHITE ),
            # ft.ElevatedButton(text="1", bgcolor=ft.colors.RED, color=ft.colors.WHITE ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
        wrap=False,
        run_spacing=30,
        # expand=True,s
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    row2 = ft.Row(
        [
            ft.Image(height=200, src='https://t.ctcdn.com.br/jTjYeys-_yXSApZpsCNEBlUwPFE=/768x432/smart/i569772.jpeg'),
            ft.Image(height=200, src='https://t.ctcdn.com.br/jTjYeys-_yXSApZpsCNEBlUwPFE=/768x432/smart/i569772.jpeg'),
        ],
        scroll=ft.ScrollMode.AUTO
    )


    # page.add(row1, row2)

# Breakpoint	Dimension
# xs	<576px
# sm	≥576px
# md	≥768px
# lg	≥992px
# xl	≥1200px
# xxl	≥1400px



    rrow1 = ft.ResponsiveRow(
        columns=12,
        run_spacing=20,
        spacing=50,
        expand=True,
        controls=[
            ft.ElevatedButton(
                col={'xs':4, 'sm':6, 'md':3},
                text='1',
                bgcolor=ft.colors.AMBER,
                color=ft.colors.BLACK
            ),
            ft.ElevatedButton(
                col=4,
                text='1',
                bgcolor=ft.colors.AMBER,
                color=ft.colors.BLACK
            ),
            ft.ElevatedButton(
                col=4,
                text='1',
                bgcolor=ft.colors.AMBER,
                color=ft.colors.BLACK
            )
        ]
    )
    text = ft.Text()

    def page_size(e):
        text.value = f'Largura: {page.window_width}, Altura: {page.window_height}'
        text.update()


    page.on_resize = page_size

    page.add(rrow1, text)

    ft.Column()


ft.app(target=main)