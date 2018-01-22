//node Echo.js
//sudo lsof -t -i tcp:8080 | xargs kill -9

var http = require('http');
var fs = require('fs');
var robot = require("robotjs");
var WebSocketServer = require('ws').Server;
var exec = require('child_process').exec;
var os = require('os')

const port = 8000
console.log(os.hostname())
const clipath='../cliclick/'


var server = http.createServer(function (req, res) {


    res.writeHead(200, {'Content-Type': 'text/html'});
    var readSream = fs.createReadStream('index.html','utf8')
    readSream.pipe(res);

})

server.on('upgrade', d=>console.log('cmd'));

server.on('listening',function(){
    console.log('ok, server is running');
});

server.listen(port, os.hostname());





function test(action = 'c') {
      pos = {x: 648, y: 416}
      exec(clipath+'/cliclick '+action+':'+pos.x+',='+pos.y,
      function(){});
    }

    // Create an instance of websocket server.
    var wss = new WebSocketServer({server:server})//{port: 1234,noServer: true});// host: os.hostname()

    console.log('New server created, waiting for connections...');
    // Add the connection listener that will be triggered once the connection is established.

    wss.on('connection', function(ws) {
        console.log('Server was connected.');
        //  Add the listener for that particular websocket connection instance.
        ws.on('message', function(message) {
            test();

            console.log('Server received message: %s', message);
            // Send back the message that we receive from the browser
            //ws.send('server+ '+message);
            ws.send(robot.getMousePos().x)
        });
    });



var visits = 0;




//console.log( server.address());
console.log('Server running at http://'+os.hostname()+':'+port);
