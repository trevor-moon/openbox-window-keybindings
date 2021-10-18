# openbox-window-keybindings

Keybindings for Openbox window snapping and tiling.

## Quickstart

1. Locate specific keybinding snippets from [keybinding-snippets](keybinding-snippets) or all avaiable keybindings in [keybindings.xml](keybindings.xml).
2. Copy the keybinding(s) to the openbox config file `<keyboard>` section located at `~/.config/openbox/`.

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
