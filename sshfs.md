   ## SSH less LOGIN
   
   
      ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/myuser/.ssh/id_rsa): /Users/myuser/.ssh/myserver_id_rsa
    
     brew install ssh-copy-id
    
     ssh-copy-id -i ~/.ssh/myserver_id_rsa.pub myuser@myserver
    
    
 ## Install FUSE and SSHFS
 https://osxfuse.github.io
    
 ## MOUNT and setup
 
    mkdir ~/Desktop/mnt
    
    sshfs server.example.com:/var/www ~/Desktop/mnt -o defer_permissions -o volname=Server

 To unmount:
 
      umount ~/mnt
  
  
  To share with other users:
  
      -o allow_other
  
  
  
  
