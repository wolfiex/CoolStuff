   ## SSH less LOGIN
   
   
      ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/myuser/.ssh/id_rsa): /Users/myuser/.ssh/myserver_id_rsa
    
     brew install ssh-copy-id
    
     ssh-copy-id -i ~/.ssh/id_rsa.pub myuser@myserver
    
 Alternatively just use the oldschool method 
 
     cat ~/.ssh/id_rsa.pub | ssh user@hostname 'cat >> .ssh/authorized_keys'
    
    
 ## Install FUSE and SSHFS
 https://osxfuse.github.io
    
 ## MOUNT and setup
 
    mkdir ~/Desktop/mnt
    
    sshfs server.example.com:/work/home/dirname ~/Desktop/mnt -o defer_permissions -o volname=Server

 To unmount:
 
      umount ~/mnt
  
  
  To share with other users:
  
      -o allow_other
  
  
  ## AutoStart
  
Add your example begin script in an executable inside your mount directory. This means if you open it and the progam is not mounted, you can then mount it. 

         cd ~/Desktop/mnt
         
         nano mountServer
         
   Include your run script and a crunchbang 
   
         #!/bin/bash
         sshfs server.example.com:/work/home/dirname ~/Desktop/mnt -o defer_permissions -o volname=Server
         
         
   and make executable
   
        chmod a+x mountServer
         

