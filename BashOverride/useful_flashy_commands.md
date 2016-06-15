Bash Cheat Sheet - Dan Ellis
------

#### Redirection 
___

- multiple cd `alias cd4="cd ../../../.."`
- escape alias `/<alias>`
- switch to previous dir `cd -`
- list only subdirectories `ls -d */` 
- make nested directories `mkdir -p tmp/a/b/c
- typographical `alias mkae=make`


#### Command Processing
___

- cut all left `^U`
- cut word left `^W`
- paste buffer `^Y`
- end of line `^E`
- start of line `^A`
- cut after cursor `^K`
- reverse search `^R`
- undo `^_`
- last bash cmd:  `esc + . /  alt + - / !!:*`

> mkdir /tmp/bin ;
> cd !!:*

- repeat last `!!`
- replace word in last cmd `^<mispelt word eg filname>^<correct word eg filename>
- filename at beggining `</var/log.txt grep 'error'`





#### Path  
___
########recently submitted: 
- last `!$`
- first`!^`
- all `!*`

>eg ls/usr/bin/log.txt    ;    
!$:h -> /usr/bin (head)  ;    
!$:t -> log.txt (tail)



#### .bashrc .bash_profile .profile
___

-autocomplete cacse `set completion-ignore-case on`
########history:
- ignore duplicates `export HISTCONTROL='erasedups:ignoreboth'`
- ignore history entries `export HISTIGNORE='&:[]*:<cmd eg exit>'`
- write history upon exit `shopt -s histappend`


#### Exit SSH
___

- `^D`
- `<enter> ~.`


#### useful commands
___
- more `less`
- recursively answer y `yes`
- filenames and numbers `grep -in`
- hidden `ls -a`
- vim readonly `view`
- diff `vimdiff`
- where is it `which`
- repeat `watch`
- all places program available `type a- <PROGNAME>`
- rename batch of files `rename's/txt_match/txt_new/' *.txt`
- recursive copy `cd -r` 
- force delete (use with caution) `rm -rf`
- `top` (once inside) k , h , z, i , u 
- `pkill <process name>`
- `xkill` (click on window)
- modified `ls -lth --time-style=+%Y-%m-%d--%H:%M`

#### Q-Sub 
___

- interactive `-I`
- memory `-l mem=<number><unit: Mb/Gb/kB>`
- `qstat -u <username>`
- `qdel -u <username>` (version dependant)
- `qsub -q`


#### Screen GNU - the terminal multiplexer
___
See .screenrc

- new session `screen -S <sessionname>`
- list all `screen -ls`
- resume running session `screen -rd <sessionname>`

using `^A + `

- kill screen `:quit`
- remove all splits `Q`
- kill current `k`
- `:resize -v 50% -h 10 lines`
- del split `:remove`
- new screen `c`
- view all `w` 
- rename window `A`
- next window `n`
- previous winddow `p`
- select from list ` " `
- "previous window viewed `^A`
- fit to new terminal size `:fit`
- move to next regioun `<tab>`
- detach screen from terminal `d`
- copy mode (enables scrolling) `[`
- paste `]`
- `:split -v (vertical) -h (horizontal)`
- kill all `\`
- lock session `x`
- show key bindings/cmd names `?`
- screen cmd prompt `:`




