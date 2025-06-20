
# Notes

- Programming language hierarchy
CPU -> Assembly -> C, C++ -> C#, Java, Swift -> Javascript, Python, Ruby -> HTML/CSS

- Create temp file
`file_name=$(mktemp)`
`echo "Temporary data" > "$tmpfile"`

- Create temp directory
`dir_name=$(mktemp -d)`
`echo "Working in $tmpdir"`

- Command for iso
`dd bs=4M if=iso_file.iso of=/dev/sdX status=progress oflag=sync`

- Searching
`find / -type f -iname "string"`

- Ommit directory from search
`find / -path "/timeshift" -prune -o -type f -iname "string" -print`

- Remove duplicated
`awk '!seen[$0]++' file > new_file`

- DPKG
`dpkg-reconfigure openssh-server`

- HTTP server
`python3 -m http.server 80`

- FTP server
`python3 -m pyftpdlib -p 21 -w`

- Venv
`mkdir virtual-python-env`
`python -m venv (project)`
`bin/activate`

- Entr
`ls *.py | entr python file_name`

- Terminal
`sudo !!`                  	- Redo las command with sudo
`fc`	                   	- Fix a long command in editor
`disown -a && exit`	    	- Exit terminal without killing process

`apropos`
`2> /dev/null`		    	- Directs standard error to the void
`lsof -u`			       	- List open user files
`pushd / popd`
`ctrl + r`	       			- Reverse search
`ctrl + a,e,u`	    		- Line start, end and delete
`&& and ;`		        	- Chain commands
`||`				       	- Or
`ctrl + u`		        	- Cut to the beginning of line from cursor
`ctrl + k`		        	- Cut to the end of line from cursor
`ctrl + w` 		        	- Cut backwards by word
`ctrl + y`		        	- Paste
`alt  + .`			        - Paste previous argument

```
- Chmod
000 = --- = 0
001 = --x = 1
010 = -w- = 2
011 = -wx = 3
100 = r-- = 4
101 = r-x = 5
110 = rw- = 6
111 = rxw = 7
```

- Archive
`tar -cvf new_name.tar file_name`    	- Combine into archive, does not compress
`tar -tvf name_of_file.tar`	        	- Shows list of files inside tar
`tar -xvf name_of_file`		        	- Extract files
`tar -czvf new_name.tar.gz file_name` 	- Combine + compress
`gzip name_of_file`	            		- Compress file
`gunzip name_of_file`		           	- Decompress file

```
- Systemctl
systemctl is-enabled (service)
systemctl enable/disable (service)
systemctl start/stop (service)
systemctl status/restart (service)
```
