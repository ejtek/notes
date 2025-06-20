
# Nmap

**Basic port scan**
- This scans the most common 1000 ports on the target.
`nmap <target>`

**OS detection scan**
- This enables OS detection, version scanning, script scanning, and traceroute.
`nmap -A <target>`

**Version scanning**
- This probes open ports to determine service/version info.
`nmap -sV <target>`

**Stealth/SYN scan**
- This performs a TCP SYN scan, which is relatively unobtrusive and stealthy.
`nmap -sS <target>`

**UDP scan**
- This scans for open UDP ports.
`nmap -sU <target>`

**Ping scan (host discovery)**
- This performs a ping scan to discover live hosts without port scanning.
`nmap -sn <target>`

**Specific port scan**
- This scans specific port(s) on the target.
`nmap -p <port(s)> <target>`

**Aggressive scan**
- This sets the timing template to "aggressive", speeding up the scan.
`nmap -T4 <target>`

**Script scan**
- This uses the default Nmap scripts for scanning.
`nmap -sC <target>`

**Verbose output**
- This increases the verbosity of the output.
`nmap -v <target>`

**Save output to file**
- This saves the scan results in normal format to a file.
`nmap -oN <filename> <target>`

**Fast scan**
- This scans fewer ports than the default scan for quicker results.
`nmap -F <target>`


# Netcat

**General Options**

- Normal syntax
`nc [options] [host] [port number]`

- Use IPv4 addressing only
`nc -4 [host] [port number]`

- Use IPv6 addressing only
`nc -6 [host] [port number]`


**Client Examples**

- Connect to listening server. Data is captured and transmitted from STDIN. Responses directed to STDOUT
`netcat 192.168.0.1 5050`

- Transmit contents of file "filename.in"
`netcat 192.168.0.1 5051 < filename.in`

- Retrive webpage
`echo -e "GET / HTTP/1.0\r\n\r\n" | netcat somewebserver.sometld 80`
