
# FZF

- Fuzzy completion for bash and zsh
`COMMAND [DIRECTORY/][FUZZY_PATTERN]**<TAB>`

- Files under the current directory, select multiple items with `TAB`
`vim **<TAB>`

- Files under parent directory
`vim ../**<TAB>`

- Files under parent directory that match `fzf`
`vim ../fzf**<TAB>`

- Files under your home directory
`vim ~/**<TAB>`

- Directories under current directory (single-selection)
`cd **<TAB>`

- Directories under ~/github that match `fzf`
`cd ~/github/fzf**<TAB>`

- Process IDs, select multiple processes with `<TAB>` or `<Shift-TAB>`
`kill -9 **<TAB>`

- For ssh and telnet commands, fuzzy completion for hostnames is provided. The names are extracted from /etc/hosts and ~/.ssh/config.
`ssh **<TAB>`
`telnet **<TAB>`

- Environment variables / Aliases
`unset **<TAB>`
`export **<TAB>`
`unalias **<TAB>`
