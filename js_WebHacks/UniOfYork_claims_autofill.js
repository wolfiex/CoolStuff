/*
A simple script to save you having to retype your details for the first page of the university of york's claim form

For information on how to make a bookmark to do this in chrome:
  In Chrome, click Bookmarks->Bookmark Manager.
  You should see a new tab with the bookmarks and folders listed.
  Select the "Bookmarks Tab" folder on the left.
  Click the "Organize" link, then "Add Page" in the drop down.
  You should see two input fields. Type the name of the bookmark you would like (i.e., claims_fill) in the first field.
  Paste the javascript code below into the second field.

Alternatively just paste into console (google how to open this with your browser cmd+alt+i for Opera)
*/

//If making a bookmark, copy all lines below, alternatively just paste the function ignoring the javascript line into console.
// if all fails you can manually type 'javascript:' (copy and paste does not work) into your browser url and paste the function after

javascript:

(function(){

//location of the claims form:
//window.location.href = "https://uni_york.formstack.com/forms/casual_payroll_claim_worker";

//authorisation details
document.getElementById("field38126433_1").checked=true;
document.getElementById("field38126437").value = 'Dr';
document.getElementById("field38126438").value = 'John';
document.getElementById("field38126439").value = 'Pasley';
document.getElementById("field38126440").value = 'john.pasley@york.ac.uk';
document.getElementById("field38126441").value = 'Physics Demonstrators';

//cell definitions
var title = document.getElementById("field38126426"),
firstname = document.getElementById("field38126427"),
surname = document.getElementById("field38126428"),
email = document.getElementById("field38126429"),
phone = document.getElementById("field38126430"),
day = document.getElementById("field38126431D"),
month = document.getElementById("field38126431M"),
year = document.getElementById("field38126431Y"),
ni= document.getElementById("field38126434");

//your details
title.value = 'test';
firstname.value = 'test1';
surname.value = 'test2';
email.value = 'test@york.ac.uk';
phone.value = '01111111111';
day.value = '01';
month.value = 'January';
year.value = '1969';
ni.value = 'PA1234A';

})()
