//Tools => script editor on the taskbar from the google sheet you want to use 


function importData() {
  var fi = DriveApp.getFilesByName(
  
  '<the csv file being uploaded - name.csv> '
  
  ); 
  var ss = SpreadsheetApp.openById(
  
  '<section between d/ .... /edit on the google sheets page you plan to update>'
  
  ); 
  
  
  
  
  if ( fi.hasNext() ) { // proceed if "report.csv" file exists in the reports folder
    var file = fi.next();
    var csv = file.getBlob().getDataAsString();
    var csvData = CSVToArray(csv); // see below for CSVToArray function
    //var j = ss.deleteSheet(ss.getSheetByName('NEWDATA'));
    //var newsheet = ss.insertSheet('NEWDATA'); // create a 'NEWDATA' sheet to store imported data
    var newsheet = ss.getSheetByName('NEWDATA');
    // loop through csv data array and insert (append) as rows into 'NEWDATA' sheet
    for ( var i=0, lenCsv=csvData.length; i<lenCsv; i++ ) {
      newsheet.getRange(i+1, 1, 1, csvData[i].length).setValues(new Array(csvData[i]));
    }
      }
};


// http://www.bennadel.com/blog/1504-Ask-Ben-Parsing-CSV-Strings-With-Javascript-Exec-Regular-Expression-Command.htm
function CSVToArray( strData, strDelimiter ) {  strDelimiter = (strDelimiter || ",");  var objPattern = new RegExp(("(\\" + strDelimiter + "|\\r?\\n|\\r|^)" +"(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +"([^\"\\" + strDelimiter + "\\r\\n]*))"    ),    "gi"  );  var arrData = [[]];  var arrMatches = null;  while (arrMatches = objPattern.exec( strData )){    var strMatchedDelimiter = arrMatches[ 1 ];if (strMatchedDelimiter.length &&(strMatchedDelimiter != strDelimiter)){arrData.push( [] );}if (arrMatches[ 2 ]){var strMatchedValue = arrMatches[ 2 ].replace(new RegExp( "\"\"", "g" ),"\"");} else {var strMatchedValue = arrMatches[ 3 ];}arrData[ arrData.length - 1 ].push( strMatchedValue );}  return( arrData );};


//update when called
function onOpen() {
  return importData()
}
function doGet(){
  return importData();
}

function doPost(){
  return importData();
}


//resources // add triggers
