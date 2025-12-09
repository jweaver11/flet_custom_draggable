import flet as ft
from custom_draggable import CustomDraggable


def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def on_drag_start(e):
        print("Drag started event received!")
        print(f"Drag started! for {e.control.data}")

    page.add(
        ft.Container(
            height=350, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, 
            content=CustomDraggable(
                group="Group 1",    
                data="Title 1",  
                title="Title 1",
                on_drag_start=on_drag_start,
                on_drag_cancel=lambda e: print("Drag 1 cancelled!"),
            ),
        ),

        ft.Container(
            height=350, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.BLUE_200, 
            content=CustomDraggable(
                group="Group 2",    
                data={'title': 'Title 2'},  
                title="Title 2",
                on_drag_start=lambda e: print("Drag started event received for Title 2!"),
                on_drag_cancel=lambda e: print("Drag 2 cancelled!"),
            ),
        ),

    ) 


ft.app(main)
