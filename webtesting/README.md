# A couple of files needed to run the Electron local-webserver on index.html (changable)
See Electron and npm for help

```
curl https://raw.githubusercontent.com/wolfiex/CoolStuff/master/webtesting/main.js > main.js;
curl https://raw.githubusercontent.com/wolfiex/CoolStuff/master/webtesting/package.json > package.json;
```



`wget https://raw.githubusercontent.com/wolfiex/CoolStuff/master/webtesting/main.js --no-check-certificate && `
`wget https://raw.githubusercontent.com/wolfiex/CoolStuff/master/webtesting/index.html --no-check-certificate &&`
`wget https://raw.githubusercontent.com/wolfiex/CoolStuff/master/webtesting/automate.py --no-check-certificate &&`
`wget https://raw.githubusercontent.com/wolfiex/CoolStuff/master/webtesting/package.json --no-check-certificate &&npm install`








## node incomp vers
```

rm -rf node_modules *.lock

npm i -D electron-rebuild

npm i 

./node_modules/.bin/electron-rebuild


```







document.lastModified

Add svg fonts 
`<defs>  <style type="text/css">@import url(https://fonts.googleapis.com/css?family=Lato);tspan,text{
  font: 1.0em Lato, sans-serif;}</style></defs>`




Aleternatively you can also spawn an electron window through Julia 

`wget https://raw.githubusercontent.com/wolfiex/CoolStuff/master/webtesting/webtest.jl`
`include("./webtest.jl")`
