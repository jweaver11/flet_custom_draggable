'''
Actual definition of the control. This gives default control values and a control name.
'''


from typing import Any, Optional

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import Control
from flet.core.control import OptionalNumber


class CustomDraggable(ConstrainedControl):
    """
    CustomDraggable Control description.
    """

    def __init__(
        self,
        content: Control | None = None,
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
        # Anything custom we want to pass in (Custom Draggable specific)
        #
        group: str = "",
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

        self.on_drag_start = on_drag_start
        self.on_drag_cancel = on_drag_cancel

        # single logical child control
        self.__content: Control | None = content
        

        # We just build this in flutter
        #self.content_feedback = content_feedback




    # Returns the name of our control. 
    def _get_control_name(self):
        return "custom_draggable"
    

    # Need to declare and set our properties here so that flutter can access them
    
    ''' Group property for the draggable '''
    @property
    def group(self) -> str:
        return self._get_attr("group")
    @group.setter
    def group(self, value: str):
        self._set_attr("group", value)


    ''' Event handler for the drag start event '''
    @property
    def on_drag_start(self):
        return self._get_event_handler("drag_start")
    
    @on_drag_start.setter
    def on_drag_start(self, handler):
        self._add_event_handler("drag_start", handler)


    ''' Event handler for the drag cancel event '''
    @property
    def on_drag_cancel(self):
        return self._get_event_handler("drag_cancel")   
    
    @on_drag_cancel.setter
    def on_drag_cancel(self, handler):
        self._add_event_handler("drag_cancel", handler)


    ''' Content property for the draggable '''
    @property
    def content(self) -> Control:
        # stored locally; returned as a named child via _get_children()
        return self.__content

    @content.setter
    def content(self, value: Control):
        self.__content = value

    def _get_children(self):
        children = []
        if self.__content:
            self.__content._set_attr_internal("n", "content")
            children.append(self.__content)
        return children

    


   



  
    

