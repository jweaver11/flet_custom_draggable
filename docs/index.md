# Introduction

CustomDraggable for Flet.

## Examples

```
import flet as ft

from custom_draggable import CustomDraggable


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=CustomDraggable(
                    tooltip="My new CustomDraggable Control tooltip",
                    value = "My new CustomDraggable Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[CustomDraggable](CustomDraggable.md)


