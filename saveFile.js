var http = require('http');
var fs = require('fs');
var formidable = require("formidable");
var util = require('util');
var express=require('express');
var async = require('async');
var app = express();
 var path = require('path')



var express = require('express');
var app = express();
app.use('/', express.static(__dirname + '/public'));

app.use(express.static(path.join('lib'+ '/public')));
var server = http.createServer(function (req, res) {
    

});

var server=http.createServer(function (req, res) {
    console.log('req starting...');
    
    var filePath = '.' + req.url;
    if (filePath == './')
        filePath = './index.htm';
    if (req.method.toLowerCase() == 'get') {
       path.exists(filePath, function(exists) {
    
        if (exists) {
            fs.readFile(filePath, function(error, content) {
                if (error) {
                    res.writeHead(500);
                    res.end();
                }
                else {
                    res.writeHead(200, { 'Content-Type': 'text/html' });
                    res.end(content, 'utf-8');
                }
            });
        }
        else {
            res.writeHead(404);
            res.end();
        }
    });
    } else if (req.method.toLowerCase() == 'post') {
        processAllFieldsOfTheForm(req, res);
    }
})

function displayForm(res) {

	 fs.readFile('index1.html', function (err, data) {
        res.writeHead(200, {
            'Content-Type': 'text/html',
                'Content-Length': data.length
        });
 
        res.write(data);
        res.end();
    });
}

function processAllFieldsOfTheForm(req, res) {
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
        //Store the data from the fields in your data store.
        //The data store could be a file or database or any other store based
        //on your application.
        res.writeHead(200, {
            'content-type': 'text/plain'
        });
        fs.writeFile('output.py', fields.code, function (err) {
        	if(err) {
        		return console.log(err);
            }
            console.log("The file was saved!");
        });
        var PythonShell = require('python-shell');
        var pyshell = new PythonShell('hack.py');
        pyshell.on('message', function (message) {
            // received a message sent from the Python script
            console.log(message);

            
        });
        // end the input stream and allow the process to exit 
        pyshell.end(function (err) {
            if (err) throw err;
            console.log('finished');
        });
    });
}
server.listen(1185);
console.log("server listening on 1185");
