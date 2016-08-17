/* A simple method to 'mark' a set of species from a list on the MCM website.
To use paste species in a comma delimited format after the string variable below. eg. 'CH4,C3H8' .

Once done, open http://mcm.leeds.ac.uk/MCMv3.2/roots.htt?None
Copy this whole code and paste into your web browsers console.
These can be accessed using the following shortcuts: 

Chrome : ctrl+shift+J
Firefox: ctrl+shift+k
Safari : crtl+shift+c 
(cmd+opt for osx)

Dan Ellis,  April 2016 

*/


var string = 'CH4,C3H8'; //paste species here


string = string.replace(/\s/g,'');var specs = string.split(',');var checkboxes = document.myform.marks;
var found= false;var missing=[];

for (i = 0; i < specs.length; i++){
    found=false;
    for (j = 0; j < checkboxes.length; j++){
        if (checkboxes[j].value == specs[i]){
            checkboxes[j].checked=true;
            found = true;
        };
    };  
    if (!found) {missing.push(specs[i])};
}    
 
 
if (missing.length>0) { alert("Below species were not found, please select manually: \n\n" + missing)}; 


