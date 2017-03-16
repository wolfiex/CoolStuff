brew install Caskroom/cask/julia

using Homebrew; Homebrew.install_brew()

Pkg.build("HDF5")

Pkg.add("LightGraphs")

Pkg.add("NetCDF")



## node interface
npm install -g node-gyp
npm install node-julia


#last stable node 5.2 for julia linking 
One way is to use NVM, the Node Version Manager. You can find it at https://github.com/creationix/nvm

It allows you to easily install and manage multiple versions of node. Here's a snippet from the help:

Usage:
nvm install <version>       Download and install a <version>
nvm use <version>           Modify PATH to use <version>
nvm ls                      List versions (installed versions are blue)

install: 
curl https://raw.githubusercontent.com/creationix/nvm/v0.19.0/install.sh | bash
add . ~/.nvm/nvm.sh to bash profile 
http://flnkr.com/2014/11/install-nvm-and-node-js-on-os-x/
update npm: 
npm i -g npm

