
# John

- Wordlist Mode(Dictionary Attack)
`./john --wordlist=password.list hashfile`

- Mangling Rules Mode (hybrid)
`./john --wordlist=password.lst –rules:<rulename> hashfile`

- Incremental mode (Brute Force)
`./john --incremental hashfile`


# Hashcat

`hashcat -h cd`

locate wordlists > /opt or (kali) /usr/share/wordlists/

`hashcat -m 0 -a 0 -o cracked.txt target_hashes.txt /usr/share/wordlist/rockyou.txt`

The -m flag is used to specify the hash type and the -a flag is to specify the attack mode
