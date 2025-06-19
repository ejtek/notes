
# Vim

`(esc)`			        -Enter command mode
`i`				        -Insert mode
`v`				        -Visual mode
`ctrl + v`                -Visual block mode

- Files & Search
`^x^f`			        -Insert file from path
`^x^n`			        -For just this file
`:%s/search/replace/gc`   -Search and replace (g=reaplce all, c=confirmation)

- Tabs
**vim -p from the command line opens multiple files**
`:tabedit <file>`
`gt`                      -Back tab
`gT`                      -Forward tab
`<#>gt`                   -Tab by number

- Buffer
`:bn`			        -Next buffer
`:bp`			        -Previous buffer
`:bd`			        -Delete buffer
`:badd`	   		        -Adds new buffer in background
`:e`			        -Edit file
`:r`			        -Read file

- Split Window
`:split/vsplit`	        -Split horizontally/vertically
`ctrl ww`		        -Switch window

- Navigation
`h, j, k, l`	        -Move left, down, up, right
`G`				        -Go to last line
`gg`			        -Go to first line
`:7`			        -Go to 7th line (etc)
`/text` 		        -Go to "text"
`n`				        -Repeat last search
`w`				        -Go to next word
`0`				        -Go to beginning of line
`$`				        -Go to end of line

- Editing
`I`				        -Insert at the beginning of line
`a`				        -Append
`A`				        -Append to end of line
`x`				        -Delete character at cursor
`o`				        -Opned new line below cursor
`O`				        -Opend new line above cursor
`y`				        -Cut current line
`yy`				    -Copies current line
`P`				        -Paste above cursor
`p`				        -Paste below cursor
`dd` 				    -Delete line
`dw`		 		    -Delete word
`cw`				    -Change word
`ct`				    -Change to a character
`u`				        -Undo last change
`.`				        -Repeat last change

- Save & Quit
`:w`				    -Save file
`:w "file"`		        -Save as "file"
`:q`			        -Quit
`:wq`			        -Save and quit
`ZZ`			        -Save and quit	
`:q!`			        -Quit without saving

- Code Fold
`zo`                      -Open (unfold) the fold at the cursor
`zc`                      -Closes (folds) the code at the cursor
`zO`                      -Open all folds under the cursor
`zM`                      -Closes all folds in the current window
`za`                      -Toggle the fold at the cursor (open if closed, close if open)
`zm`                      -Increase the fold level by one (close more folds)
`zr`                      -Decrease the fold level by one (open more folds)
