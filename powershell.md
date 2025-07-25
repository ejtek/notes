
# Powershell

**Navigating the File System**
Get-ChildItem: Lists items in a directory.
Set-Location: Changes the current directory.
Push-Location: Saves the current directory on a stack so you can return to it.
Pop-Location: Returns to the directory saved by Push-Location.

**File Manipulation**
New-Item: Creates a new file or directory.
Remove-Item: Deletes a file or directory.
Copy-Item: Copies a file or directory to another location.
Move-Item: Moves a file or directory to a new location.
Rename-Item: Renames a file or directory.

**System Administration**
Get-Service: Lists all services on a computer.
Start-Service: Starts a stopped service.
Stop-Service: Stops a running service.
Restart-Service: Restarts a service.

**User & Permissions Management**
Get-LocalUser: Retrieves local user accounts.
New-LocalUser: Creates a new local user account.
Remove-LocalUser: Deletes a local user account.
Get-Acl: Gets access control list (ACL) for a file or resource.
Set-Acl: Sets the ACL for a file or resource.

**Netwoking Commands**
Test-Connection: Sends ICMP echo requests to a target host to test connectivity.
Get-NetIPAddress: Retrieves IP address configuration.
Get-NetAdapter: Lists network adapters.
Resolve-DnsName: Resolves a DNS name to an IP address.

**Process Management**
Get-Process: Lists currently running processes.
Start-Process: Starts a new process.
Stop-Process: Stops a running process.
Wait-Process: Waits for a process to exit.

**working With Objects**
Select-Object: Selects specific properties of an object.
Where-Object: Filters objects based on property values.
Sort-Object: Sorts objects by property values.
Group-Object: Groups objects by property values.


# CMD

**HELP**
command /?                              - help page for commands

**DIRECTORIES & NAVIGATION**
C:                                      - change drive
cd..                                    - change directory
dir                                     - list files
dir *.ext                               - list filtered by extension
mkdir                                   - creates directory
rmdir                                   - removes empty directory
type                                    - read file
type nul> file.txt                      - touch file
rename                                  - rename
del                                     - delete file
copy    / xcopy                         - copy file
move                                    - move file
clip                                    - add to clipboard

**FIND & SEARCH**
findstr                                 - find string
