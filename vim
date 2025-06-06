#############
# VIM
#############

(esc)			  Enter command mode
i				  Insert mode
v				  Visual mode
ctrl + v          Visual block mode

----------
FILES & SEARCH
^x^f			  Insert file from path
^x^n			  For just this file
:%s/search/replace/gc	search and replace (g=reaplce all, c=confirmation)

----------
TABS
vim -p from the command line opens multiple files 
:tabedit <file>
gt                Back tab
gT                Forward tab
<#>gt             Tab by number

----------
BUFFER
:bn				  Next buffer
:bp				  Previous buffer
:bd				  Delete buffer
:badd			  Adds new buffer in background
:e				  Edit file
:r				  Read file

----------
SPLIT WINDOW
:split/vsplit	  Split horizontally/vertically
ctrl ww			  Switch window

----------
NAVIGATION
h, j, k, l		  Move left, down, up, right
G				  Go to last line
gg				  Go to first line
:7				  Go to 7th line (etc)
/text 			  Go to "text"
n				  Repeat last search
w				  Go to next word
0				  Go to beginning of line
$				  Go to end of line

----------
EDITING
I				  Insert at the beginning of line
a				  Append
A				  Append to end of line
x				  Delete character at cursor
o				  Opned new line below cursor
O				  Opend new line above cursor
y				  Cut current line
yy				  Copies current line
p				  Paste above cursor
P				  Paste below cursor
dd 				  Delete line
dw		 		  Delete word
cw				  Change word
ct				  Change to a character
u				  Undo last change
.				  Repeat last change

----------
SAVE & QUITTING
:w				  Save file
:w "file"		  Save as "file"
:q				  Quit
:wq				  Save and quit
ZZ				  Save and quit	
:q!			      Quit without saving

----------
CODE FOLD KEYBINDS
zc                This closes (folds) the code at the cursor
zM                This closes all folds in the current window
zo                Open (unfold) the fold at the cursor
zO                Open all folds under the cursor
za                Toggle the fold at the cursor (open if closed, close if open)
zm                Increase the fold level by one (close more folds)
zr                Decrease the fold level by one (open more folds)
