var fs = require("fs");
var http = require('http'); 
http.createServer(function(request, response) {  
	console.log(response)
	fs.writeFile('input3.py', 'Simplytttttttttt',  function(err) {
		response.writeHead(200, {
			'Content-Type': 'text/html'
		});
		if (err) {
			return console.error(err);
		}
	   	response.write("Data written successfully!");
	   	response.write("Let's read newly written data");
	   	fs.readFile('input2.txt', function (err, data) {
		    if (err) {
		        return console.error(err);
		    }
	    	response.write("Asynchronous read: " + data.toString());
	   });
	});
}).listen(8888, '127.0.0.1');
console.log('Server running at http://127.0.0.1:8888');

