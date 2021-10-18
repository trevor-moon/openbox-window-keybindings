# openbox-window-keybindings

Keybindings for Openbox window snapping and tiling.

## Quickstart

1. Find a window snapping feature in [keybindings](keybinding-snippets).
2. Copy the [keybinding](keybinding-snippets) snippet(s) in the openbox config file located at `~/.config/openbox/`. The snippet should go in the `<keyboard>` section of the file.

   - lxqt-rc.xml
   - rc.xml

3. Open a terminal window.
4. Run `openbox --reconfigure` to apply the changes.
5. Use the applied keybinding(s).

## Notes

The specific keybinding modifier-key combination may be changed to meet your preference. The modifier-key combination is the content between the " " in `<keybind key="">` within the snippet.

## Resources

For more information, see Openbox [actions][openbox-actions] and [bindings][openbox-bindings].

<!-- links -->
[openbox-actions]: http://openbox.org/wiki/Help:Actions#Action_syntax
[openbox-bindings]: http://openbox.org/wiki/Help:Bindings
