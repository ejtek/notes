
# Vim

```
Enter command mode  
(esc)

Insert mode  
i

Visual mode  
v

Visual block mode  
ctrl + v
```

**Files & Search**  
Insert file from path  
`^x^f`

For just this file  
`^x^n`

Search and replace (g=reaplce all, c=confirmation)  
`:%s/search/replace/gc`


**Tabs**  
vim -p from the command line opens multiple files  
`:tabedit <file>`

Back tab  
`gt`

Forward tab  
`gT`

Tab by number  
`<#>gt`


**Buffer**  
Next buffer  
`:bn`

Previous buffer  
`:bp`

Delete buffer  
`:bd`

Adds new buffer in background  
`:badd`

Edit file  
`:e`

Read file  
`:r`


**Split Window**  
Split horizontally/vertically  
`:split/vsplit`

Switch window  
`ctrl ww`


**Navigation**  
Move left, down, up, right  
`h, j, k, l`

Go to last line  
`G`

Go to first line  
`gg`

Go to 7th line (etc)  
`:7`

Go to "text"  
`/text`

Repeat last search  
`n`

Go to next word  
`w`

Go to beginning of line  
`0`

Go to end of line  
`$`


**Editing**  
Insert at the beginning of line  
`I`

Append  
`a`

Append to end of line  
`A`

Delete character at cursor  
`x`

Open new line below cursor  
`o`

Open new line above cursor  
`O`

Cut current line  
`y`

Copies current line  
`yy`

Paste above cursor  
`P`

Paste below cursor  
`p`

Delete line  
`dd`

Delete word  
`dw`

Delete ALL lines  
`dG`

Change word  
`cw`

Change to a character  
`ct`

Undo last change  
`u`

Repeat last change  
`.`

Move line(s)  
`m+1` , `m-2` or `visual mode, select lines, :m target line number`

**Save & Quit**  
Save file  
`:w`

Save as "file"  
`:w "file"`

Quit  
`:q`

Save and quit  
`:wq` or `ZZ`

Quit without saving  
`:q!`


**Code Fold**  
Open (unfold) the fold at the cursor  
`zo`

loses (folds) the code at the cursor  
`zc`

Open all folds under the cursor  
`zO`

Closes all folds in the current window  
`zM`

Toggle the fold at the cursor (open if closed, close if open)  
`za`

Increase the fold level by one (close more folds)  
`zm`

Decrease the fold level by one (open more folds)  
`zr`

```
Adding/Removing hash in multiple lines
In visual mode, select lines, x to delete, esc
in visual mode, select lines, shift i + #, esc 
```
