# Tmux

## Settings

* `PREFIX :source-file <filename>` Reload the tmux config from <filename>
* `unbind` Remove a keybinding
* `set -g escape-time 0` tmux adds a delay to sending the escape key in case it is followed by escape sequences. This makes that delay zero. This is nice for using vim under tmux.

## Copy / Paste

The default copy / paste commands:
* `PREFIX [` to enter copy mode
* `space` to select start of selection
* `enter` to end selection and copy text to paste buffer
* `PREFIX ]` to paste the contents of the paste buffer
* `PREFIX #` to see the contents of the paste buffer
* `capture-pane` copy entire visible contens of a pane into the paste buffer
* `save-buffer <filename>` saves the buffer contents to <filename>
* `list-buffers` list all paste buffers
* `PREFIX =` list all paste buffers and choose one to paste from

## Windows and Panes

* `move-window -s src-window -t dst-window` Move a window, use full `session_name:window` format for a different session
* `join-pane -s :3` join the current window with window 3 in the current session
* `join-pane -s code:3 -t writing:4` Merge window 4 from the 'writing' session with window 3 in the 'code' session.
* `:swap-window -s 4 -t 0` Swap windows 4 and 0
* `PREFIX z` zoom into (make "fullscreen") the current window pane, press again to zoom out
* `PREFIX !` moves current pane to its own window
* `PREFIX ;` switch to most recently used pane
* `PREFIX f` Find a window by name.
* `PREFIX w` View a list of windows open in the current session.

## Sessions

* `PREFIX (` Move to previous session
* `PREFIX )` Move to next session
* `PREFIX s` Choose from list of sessions
