// Defines our FlettyControl that is passed into flutter when flet encounters the 'fletty' control type.

import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

// Our CustomDraggableControl class that extends StatelessWidget
class CustomDraggableControl extends StatelessWidget {
  final Control? parent;
  final Control control;
  final FletControlBackend backend;

  // Receives control data from flet
  const CustomDraggableControl({
    super.key,
    required this.parent,
    required this.control,
    required this.backend,
  });

  // Builds the actual widget and how it will be rendered in flutter
  @override
  Widget build(BuildContext context) {
    // Set our data. Simple attributes are ez
    dynamic data = control.attrString("data", "")!;
    String title = control.attrString("title", "Drag Me")!;

    // Bool checks to see if we have the event handlers for drag start and cancel
    final hasOnDragStart = control.attrBool("onDragStart", false) ?? false;
    final hasOnDragCancel = control.attrBool("onDragCancel", false) ?? false;

    // Text style for the feedback text during dragging
    final textStyle = Theme.of(context)
        .textTheme
        .titleMedium
        ?.copyWith(decoration: TextDecoration.none);

    // The build we return
    return Draggable(
      data: data,
      feedback: Material(
        // make it use Material/Theme in the overlay
        color: Colors.transparent,
        child: Text(
          title,
          style: textStyle, // themed, no underline
        ),
      ),
      child: Container(
          child: Text(title,
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold))),
      onDragStarted: hasOnDragStart
          ? () => backend.triggerControlEvent(
                control.id, // <- String, not Control
                "drag_start", // event name
                "",
              )
          : null,
      onDraggableCanceled: hasOnDragCancel
          ? (velocity, offset) => backend.triggerControlEvent(
                control.id,
                "drag_cancel",
                "",
              )
          : null,
    );
  }
}
