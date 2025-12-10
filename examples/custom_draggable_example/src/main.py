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
            expand=1, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, 
            content=CustomDraggable(
                content=ft.Container(content=ft.Row([ft.Icon(ft.Icons.DRAG_HANDLE), ft.Text("Drag me plez")]), bgcolor=ft.Colors.with_opacity(.1, "red")),
                group="Group 1",    
                data="Data 1", 
                title="Title 1", 
                content_feedback=ft.Text("I'm being dragged!"),
                on_drag_start=on_drag_start,
                on_drag_cancel=lambda e: print("Drag 1 cancelled!"),
                on_drag_end=lambda e: print("Drag 1 ended!")
            ),
        ),

        ft.Container(
            expand=1, alignment = ft.alignment.center, bgcolor=ft.Colors.BLUE_200, 
            content=CustomDraggable(
                content=ft.Text("Draggable 2"),
                group="Group 2",    
                data={'title': 'Title 2'},  
                title="Title 2",
                content_feedback=ft.TextButton("I'm dragging too!"),
                on_drag_start=lambda e: print("Drag started event received for Title 2!"),
                on_drag_cancel=lambda e: print("Drag 2 cancelled!"),
                on_drag_end=lambda e: print("Drag 2 ended!")
            ),
        ),

        ft.Row(
            #height=100,
            expand=True,
            controls=[
                ft.DragTarget(
                    group="Group 1",
                    content=ft.Container(
                        expand=1, alignment = ft.alignment.center, bgcolor=ft.Colors.GREEN_200, 
                        content=ft.Text("Drop here (Group 1)"),
                    ),
                    on_will_accept=lambda e: print("Will accept drag for Group 1") or True,
                    on_accept=lambda e: print(f"Accepted drag with data: {e.data}"),
                ),
                ft.DragTarget(
                    group="Group 2",
                    content=ft.Container(
                        expand=1, alignment = ft.alignment.center, bgcolor=ft.Colors.ORANGE_200, 
                        content=ft.Text("Drop here (Group 2)"),
                    ),
                    on_will_accept=lambda e: print("Will accept drag for Group 2") or True,
                    on_accept=lambda e: print(f"Accepted drag with data: {e.data}"),
                ),
        ])

    ) 


ft.app(main)
