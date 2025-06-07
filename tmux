#############
# TMUX
#############

MODDED CONFIG
# Send prefix
set-option -g prefix C-a
unbind-key C-a
bind-key C-a send-prefix
 
# Use Alt-arrow keys to switch panes
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D
 
# Shift arrow to switch windows
bind -n S-Left previous-window
bind -n S-Right next-window
 
# Mouse mode
setw -g mouse on
 
# Set easier window split keys
bind-key v split-window -h
bind-key h split-window -v
 
# Easy config reload
bind-key r source-file ~/.tmux.conf \; display-message "~/.tmux.conf reloaded."


------
ORIGINAL CONFIG				# https://tmuxcheatsheet.com/
tmux ls					# list-sessions
tmux a 					# attach
tmux a -t #tmux new -s "name"		# new session at start


------
ctrl b 					# prefix
up, down, left, right			# move between windows
"					# vertical split
%					# horizontal aplit
x					# exit panes
z					# zoom
c					# new window
n					# next window
p					# previous window
&					# close window
,					# rename window
$					# rename session
s					# switch sessions
