import flet as ft



class AddPay(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.name_field = None
        self.price_field = None

    def build(self):
        self.name_field = ft.Ref[ft.TextField]()
        self.price_field = ft.Ref[ft.TextField]()
        self.category_select = ft.Ref[ft.Dropdown]()

        return ft.Column([
                ft.TextField(ref=self.name_field, hint_text="Название"),
                ft.TextField(ref=self.price_field, hint_text="Стоимость", ),
                ft.Dropdown(options=[ft.dropdown.Option("Транспорт"), 
                                     ft.dropdown.Option("Еда"),
                                     ft.dropdown.Option("Развлечения"),
                                     ft.dropdown.Option("Социальные платежи")
                                     ], hint_text="Категория", ref=self.category_select)
                ],

                spacing=5
                )
