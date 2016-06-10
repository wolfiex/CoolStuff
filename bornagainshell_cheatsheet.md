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
- reverse search `<fragment to match> ^R`
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
- ignore history entries `export HISTIGNORE='&:[]*:<cmd eg exit>`
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
- top (once inside) k  , h , z, i 
- pkill `<process name>`
- xkill (click on window)

#### Q-Sub 
___

- interactive `-I`
- memory `-l mem=<number><unit: Mb/Gb/kB>`
- qstat -u <username>
- qdel -u <username> (version dependant)
- qsub -q 



