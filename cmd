
# CMD

**HELP**
command /?					        	- help page for commands


**DIRECTORIES & NAVIGATION**
C:						                - change drive
cd..						        	- change directory
dir						            	- list files
dir *.ext					        	- list filtered by extension
mkdir						        	- creates directory
rmdir						        	- removes empty directory
type						        	- read file
type nul> file.txt			        	- touch file
rename						        	- rename
del						            	- delete file
copy	/ xcopy				        	- copy file
move						        	- move file
clip						        	- add to clipboard


**FIND & SEARCH**
findstr						        	- find string
where						        	- locate files


**NETWORKING**
iponfig						        	- show ip list
netstat 					        	- show open ports
getmac						        	- shows MAC address


**UTILS**
cls						            	- clear screen
tree						        	- shows directory structure
assoc .txt=word				        	- change file extention
attrib						        	- shows file attributes
attrib +/-argument			        	- add/remove attributes
attrib -h -r -s 			        	- completely hide files
shutdown /r /fw /w /t 0		        	- system shutdown into BIOS
color   					        	- change color


**SYSTEM MANAGEMENT (admin)**
ver						            	- version info
systeminfo					        	- full system details
driverquery					        	- list running drivers
tasklist					        	- list running tasks
taskkill /PID#				        	- kill task
net start					        	- running services
net stop/start "service"	        	- stop/start service
wmic logicaldisk get name	        	- shows all drive

wmic						        	- enter wmic:root
cpu						            	- cpu details
/output:c:\file.txt product get name,version 		- product list to text file

diskpart					        	- enter disk partition
list disk					        	- list number of disks
select disk 
detail disk					        	- shows details
clean
create partition primary
format fs=ntfs quick

chkdsk						        	- check disk
chkntfs
schtasks					        	- view system tasks


**MANAGE USERS (admin)**
net user					        	- list user accounts
net user name /add passwd				- add user
net user /del name 				    	- delete user
net user administrator /active:yes/no	- enable/disable admin account
net user "administrator" *				- change admin password


**ENCRYPTION**
cipher -e					        	- encrypt files
cipher -d					        	- decript files
rekey						        	- change decription keys
