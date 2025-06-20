
# Pacman

- Update package list
`sudo pacman -Syy`

- Update and upgrade all
`sudo pacman -Syu`

- Install specific package
`sudo pacman -S pkgname`

- Find available packages
`sudo pacman -Ss keyword`

- Find available local packages
`sudo pacman -Qs keyword`

- Show manually installed from AUR
`pacman -Qm`

- Delete unused packages
`sudo pacman -Sc`

- List package information
`pacman -Qi`

- List package dependencies in tree view
`pactree <package>`

- List all files from package
`pacman -Ql pkgname`

- To remove a package and its dependencies which are not required by any other installed package
`sudo pacman -Rs package_name`

- List all packages no longer required as dependencies
`sudo pacman -Qdt`

- Pacman log file
`/var/log/pacman.log`

- Get distro version
`lsb_release -a`
