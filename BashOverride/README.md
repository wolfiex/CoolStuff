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
- symbolic (soft) link `ln -s file1 file2`
- hard link `ln file1 file2`
- ls or grep files mathcing one set but not another `comm -23 <(ls *.svg) <(ls dontmatchprefix*.svg)`



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
- filename at beggining `</var/log.txt grep 'error'>`
- change filename for batch using regex `for file in <*.png file-match>; do mv "$file" "${file/<regex_match>/<regex_replace>}"; done`




#### Path  
___
########recently submitted: 
- last `!$`
- first`!^`
- all `!*`

>eg ls/usr/bin/log.txt    ;    
!$:h -> /usr/bin (head)  ;    
!$:t -> log.txt (tail)

-push to ftp server`find ./ -exec curl -T {} ftp://ftp.<ftpserver link>/<filepath>/ --user <username>:<passwd> \;`


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


#### Useful commands
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
- number of lines in file `wc -l <filename>`
- get all files from url `wget -r -nH --cut-dirs=7 --reject="index.html*"  http://www-users.york.ac.uk/~dp626/force/ics`
-delete all files NOT ending with .json `find . -type f ! -name "*.json" -delete`
- list files in repositories recursively `ls -r *`

#### Python
___

- compile `python -O -m py_compile <myprog.py>`
- run `python <myprog.pyo>` (or pyc for non optimised)
- cython `cython --embed -o <cfile>.c <mypyfile>.py`
- cython compile `gcc -Ofast -I /Users/dna/anaconda/include/python2.7 -o hello hello.c -lpython #-lpthread -lm -lutil -ldl`
- instal module for pypy: `pypy -m pip install sympy`
- server with timeout: `timeout 3600 python -m SimpleHTTPServer 80`
- kill server: `fuser -k 80/tcp`



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

For the next section use  `^A + <keystrokes stated> `

- new screen `c`
- fit to new terminal size `:fit`
- detach screen from terminal `d`
- `:split -v (vertical) -h (horizontal)`
- `:resize -v 50% -h 10 lines`
- del split `:remove`
- remove all splits `Q`
- rename window `A`
- view all `w` 
- next window `n`
- previous winddow `p`
- select from list ` " `
- "previous window viewed `^A`
- move to next regioun `<tab>`
- copy mode (enables scrolling) `[`
- paste `]`
- kill screen `:quit`
- kill current `k`
- kill all `\`
- lock session `x`
- show key bindings/cmd names `?`
- screen cmd prompt `:`


#### git 
- large file `git filter-branch -f --index-filter "git rm -rf --cached --ignore-unmatch FOLDER/FILENAME" -- --all`

#### Makefile
- `-rm -f *.o` - ignore exit status / errors and run
