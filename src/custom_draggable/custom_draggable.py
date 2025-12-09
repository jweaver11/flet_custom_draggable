'''
Actual definition of the control. This gives default control values and a control name.
'''


from typing import Any, Optional

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber

class CustomDraggable(ConstrainedControl):
    """
    CustomDraggable Control description.
    """

    def __init__(
        self,
        title: str,
        group: str,
        #
        # All flet controls 
        #
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        #
        # Flet Constrained controls Specific (ConstrainedControl)
        #
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        #
        # Anything custom we want to pass in (Fletty specific)
        #,
        on_drag_start = None, 
        on_drag_cancel = None,
    ):
        
        # Sets all our default controls values and properties to those of the constrained control
        ConstrainedControl.__init__(
            self,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,          # Data is set here
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        # Any value we want to add for ourselves
        # Our properties and setters are automatically called when we set them here

        self.group = group
        self.title = title

        self.on_drag_start = on_drag_start
        self.on_drag_cancel = on_drag_cancel

        # We just build this in flutter, since it just needs our title
        #self.content_feedback = content_feedback
        #self.content = content




    # Returns the name of our control. 
    def _get_control_name(self):
        return "custom_draggable"
    
    # Need to declare and set our properties here so that flutter can access them
    

    @property
    def group(self) -> str:
        return self._get_attr("group")
    @group.setter
    def group(self, value: str):
        self._set_attr("group", value)


    @property
    def title(self) -> str:
        return self._get_attr("title")
    @title.setter
    def title(self, value: str):
        self._set_attr("title", value)



    @property
    def on_drag_start(self):
        return self._get_event_handler("drag_start")
    @on_drag_start.setter
    def on_drag_start(self, handler):
        # this flag is what Flutter reads as "onDragStart"
        self._set_attr("onDragStart", True if handler is not None else None)
        self._add_event_handler("drag_start", handler)

    @property
    def on_drag_cancel(self):
        return self._get_event_handler("drag_cancel")   
    @on_drag_cancel.setter
    def on_drag_cancel(self, handler):
        # this flag is what Flutter reads as "onDragCancel"
        self._set_attr("onDragCancel", True if handler is not None else None)
        self._add_event_handler("drag_cancel", handler)

   



  
    

