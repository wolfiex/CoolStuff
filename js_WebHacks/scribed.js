var pages = []
var i = 0;

function run()
{
setTimeout(function(){
i+=1
console.log(i)
var item = document.getElementById('page'+i).querySelector('[class=absimg]'); 
item.scrollIntoView(); 
pages.push('curl '+item.src+' --output '+("000" + i).slice(-4)+'.jpg')
run()
},600)
}
run()



//https://www.scribd.com/doc/133057762/RYA-Navigation-Handbook
//// curl script 
console.log(pages.join(' ; '))
//// turn into pdf
convert *.jpg pictures.pdf
