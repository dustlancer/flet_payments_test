from typing import Any, List, Optional, Union
import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue

class PaymentCard(ft.UserControl):
    def __init__(self, payment):
        super().__init__()
        self.payment = payment

    # def add_click(self, e):
    #     self.counter += 1
    #     self.text.value = str(self.counter)
    #     self.update()

    def build(self):
        if self.payment['category']=="Еда":
            border_color=ft.colors.GREEN_400
        if self.payment['category']=="Развлечения":
            border_color=ft.colors.ORANGE_400
        if self.payment['category']=="Транспорт":
            border_color=ft.colors.BLUE_400
        if self.payment['category']=="Социальные платежи":
            border_color=ft.colors.GREY_400
        self.counter = 0
        self.text = ft.Text(str(self.counter))
        return ft.Container(
            ft.Row([
                        ft.Text(self.payment['date'], weight=ft.FontWeight.BOLD),
                        ft.Text(self.payment['name'], size=20),
                        ft.Column([
                                    ft.Text(self.payment["price"], size=20),
                                    ft.Text(self.payment['category'], size=15)
                                    ], horizontal_alignment=ft.CrossAxisAlignment.END,
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                  bgcolor=ft.colors.GREY_800,
                  border_radius=10,
                  padding=15,
                  border=ft.border.all(2, border_color)
                  
        )