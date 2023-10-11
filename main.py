import flet as ft
import os
from user_controls.payment_card import PaymentCard
from user_controls.add_pay import AddPay
from datetime import date

DEFAULT_FLET_PATH = ''  # or 'ui/path'
DEFAULT_FLET_PORT = 8502
mes = None



def main(page):
    mpm = {
        "date":"28.08.2023",
        "price":500,
        "name": "apple",
        "category": "Еда"
    }

    payments_col = ft.Ref[ft.Column]()
    banner_button = ft.Ref[ft.ElevatedButton]()

    def close_banner(e):
        page.banner.open = False
        banner_button.current.text="Добавить покупку"
        page.update()

    def add_payment(e):
        print(page.banner.content.name_field.current.value)
        print(page.banner.content.price_field.current.value)
        print(page.banner.content.category_select.current.value)
        new_payment = {
            "date": date.today().strftime("%d.%m.%Y"),
            "price": page.banner.content.price_field.current.value,
            "name": page.banner.content.name_field.current.value,
            "category": page.banner.content.category_select.current.value
        }

        payments_col.current.controls.insert(0, PaymentCard(new_payment))
        close_banner(e)

    page.banner = ft.Banner(
        bgcolor=ft.colors.GREY_900,
        content=AddPay(),
        force_actions_below = True,
        actions=[ft.ElevatedButton("Добавить", on_click=add_payment)])

    def show_banner_click(e):
        if page.banner.open:
            close_banner(e)
        else:
            page.banner.open = True
            banner_button.current.text="Закрыть"
        page.update()


    page.add(ft.ElevatedButton("Добавить покупку", ref=banner_button, on_click=show_banner_click),
             ft.Column([PaymentCard(mpm)], expand=True, scroll=ft.ScrollMode.ALWAYS, ref=payments_col))
  

if __name__ == "__main__":
    flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
    flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
    ft.app(name=flet_path, target=main, assets_dir="assets",  view=None, port=flet_port)