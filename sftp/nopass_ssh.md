# No password shhing
```
ssh-keygen -t rsa

ssh ${USER}@viking mkdir -p .ssh

cd ~/
cat .ssh/id_rsa.pub | ssh ${USER}@viking 'cat >> .ssh/authorized_keys'
```
