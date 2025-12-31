// Defines our CustomDraggableControl that is passed into flutter when flet encounters the 'fletty' control type.
import 'dart:convert';
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

// Our CustomDraggableControl class that extends StatelessWidget
class CustomDraggableControl extends StatelessWidget {
  final Control? parent;
  final Control control;
  final List<Control> children;
  final FletControlBackend backend;

  // Receives control data from flet
  const CustomDraggableControl({
    super.key,
    required this.parent,
    required this.control,
    required this.children,
    required this.backend,
  });

  // Builds the actual widget and how it will be rendered in flutter
  @override
  Widget build(BuildContext context) {
    // Set our data. Simple attributes are ez
    dynamic data = control.attrString("data", "")!;
    String title = control.attrString("title", "Drag Me")!;
    String group = control.attrString("group", "")!;

    // This is what Flet's DragTarget will see as `e.data`
    final String dragPayload = jsonEncode({
      "src_id":
          control.id, // must match your Python `event_data["src_id"]` usage
      "group": group,
      "data": data,
    });

    // Get "content" child controls
    final contentCtrls =
        children.where((c) => c.name == "content" && c.isVisible);

    // Turn first "content" control into a Widget
    final Widget child = contentCtrls.isNotEmpty
        ? (createControl(
            control, // parent
            contentCtrls.first.id, // <- child control id (String)
            control.isDisabled, // <- parentDisabled (or false if you prefer)
          ))
        : Text(title);

    // Get "content_feedback" child controls
    final feedbackCtrls =
        children.where((c) => c.name == "content_feedback" && c.isVisible);

    // Turn first "content_feedback" control into a Widget
    final Widget feedback = feedbackCtrls.isNotEmpty
        ? (createControl(
            control, // parent
            feedbackCtrls.first.id, // <- child control id (String)
            control.isDisabled, // <- parentDisabled (or false if you prefer)
          ))
        : Text(title);

    Widget myControl = Draggable(
      data: dragPayload, // Set our data
      feedback: feedback, // Set our feedback control
      child: child, // Set the content passed in that we defined earlier

      onDragStarted: () {
        backend.triggerControlEvent(control.id, "drag_start", "");
      },

      onDragEnd: (details) {
        final payload = jsonEncode({
          "wasAccepted": details.wasAccepted,
          "offsetX": details.offset.dx,
          "offsetY": details.offset.dy,
        });

        backend.triggerControlEvent(control.id, "drag_end", payload);
      },

      // Only when *not* accepted by any DragTarget
      onDraggableCanceled: (velocity, offset) {
        final payload = jsonEncode({
          "offsetX": offset.dx,
          "offsetY": offset.dy,
        });
        backend.triggerControlEvent(control.id, "drag_cancel", payload);
      },

      // Only when dropped on an accepting DragTarget
      onDragCompleted: () {
        backend.triggerControlEvent(control.id, "drag_complete", "");
      },
    );

    // The build we return
    return constrainedControl(context, myControl, parent, control);
  }
}
