// When flet encounters the 'custom_draggable' control type that it needs to pass to flutter, it returns a CustomDraggableControl widget
// This Registers our custom control from flet into its flutter implementation

import 'package:flet/flet.dart';
import 'custom_draggable.dart';

CreateControlFactory createControl = (CreateControlArgs args) {
  switch (args.control.type) {
    case "custom_draggable":
      return CustomDraggableControl(
        parent: args.parent,
        control: args.control,
        children: args.children,
        backend: args.backend,
      );
    default:
      return null;
  }
};

void ensureInitialized() {
  // nothing to initialize
}
