
# Networking

- Proxychains config
`/etc/proxychains4.conf`

- DNS manual config
`/etc/dhcp/dhclient.comf`

- DNS network config
`/etc/resolv.config`

- Netstat
`netstat -natu | grep 'ESTABLISHED'`
`netstat -natu | grep 'LISTENING'`

- Systemctl
`systemctl start/restart networking`
`systemctl stop networking`
`systemctl status networking`

- Interface
`ip link set <interface> up/down`

- HANDSHAKE
`ipconfig/iwconfig`
`airmon-ng start (wlan0)`

- Note bssid, station, channel, beacon**
`airodump-ng (wan0mon)`
`airodump-ng -c (channel) --bssid (BSSID) -w (write file) (wlan0mon)`

- Kick off network to capture 4-way handshake
`aireplay-ng --deauth 0 -a (bssid) -c (station) wlan0mon`

- View capture.cap file in Wireshark (eapol filter)
`aircrack-ng capture.cap -w (wordlist.txt)`

- Wifite
`sudo wifite --wpa --dict (file.txt) --kill`

- Discover devices in the network
`netdiscover -r 192.168.0.0/24`

- Use nmap on target ip
`nmap 192.168.1.0`

Use browser to navigate http site
