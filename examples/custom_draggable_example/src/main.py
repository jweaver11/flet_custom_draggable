import flet as ft
#from custom_draggable import CustomDraggable

import os
import sys
import flet as ft

# add project src/ folder to sys.path so we use the local custom_draggable
src_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "src")
)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from custom_draggable.custom_draggable import CustomDraggable  # <- use local file


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
                content=ft.Container(content=ft.Row([ft.Icon(ft.Icons.DRAG_HANDLE), ft.Text("Drag me plez")]), bgcolor=ft.Colors.with_opacity(.1, "red")),
                group="Group 1",    
                data="Title 1",  
                on_drag_start=on_drag_start,
                on_drag_cancel=lambda e: print("Drag 1 cancelled!"),
            ),
        ),

        ft.Container(
            height=350, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.BLUE_200, 
            content=CustomDraggable(
                content=ft.Text("Drag me 2 plez"),
                group="Group 2",    
                data={'title': 'Title 2'},  
                
                on_drag_start=lambda e: print("Drag started event received for Title 2!"),
                on_drag_cancel=lambda e: print("Drag 2 cancelled!"),
            ),
        ),

    ) 


ft.app(main)
