

const electron = require('electron');
const app = electron.app;  // Module to control application life.
const BrowserWindow = electron.BrowserWindow;  // Module to create native browser window.
var mainWindow = null;

app.on('window-all-closed', function() {
    if (process.platform != 'darwin') {
        app.quit();
    }});

app.on('ready', function() {
    const myLocation = 'file://' + __dirname
    mainWindow = new BrowserWindow({width:900, height: 800,resizable: true,title:'Dan Ellis 2016' ,
    show:true});
    mainWindow.openDevTools();    // and load the index.html of the app.
    mainWindow.loadURL( myLocation + '/index.html');

    mainWindow.on('closed', function() { mainWindow = null;  app.quit();});
});
