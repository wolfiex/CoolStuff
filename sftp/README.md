Add to bashrc for autocomplete hosts

      [ -e "$HOME/.ssh/known_hosts" ] && complete -o "default" -o "nospace" -W "$(cut -f1 -d','  \
        $HOME/.ssh/known_hosts | cut -f1 -d' ')" scp sftp ssh
