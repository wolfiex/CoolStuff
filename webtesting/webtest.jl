#= 
A web server to run an html file and forward commands through julia 
requires Blink : 
    Pkg.add("Blink")
    Blink.AtomShell.install()

Can be used on weburls or locally- this script covers the local selection. 

D.Ellis 2017
=#

using blink
w = Blink.AtomShell.Window()

loadurl(w, string("file://" ,pwd(),"/index.html"))
@js w console.log("You have succesfully loaded index.html from Julia")
