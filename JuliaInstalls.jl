brew install Caskroom/cask/julia

using Homebrew; Homebrew.install_brew()

Pkg.build("HDF5")

Pkg.add("LightGraphs")

Pkg.add("NetCDF")



## node interface
npm install node-gyp
npm install node-julia
