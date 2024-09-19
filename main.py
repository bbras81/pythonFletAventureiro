import flet as ft
def main(page: ft.Page):
    grid = ft. GridView(
        controls=[
            ft.Image(src=f'https://picsum.photos/250/300?{num}', fit='cover') for num in range(20)
        ],
        runs_count=4,
        padding=36,
    )

    page.add(grid)

if __name__ =='__main__':
    ft.app(target = main)