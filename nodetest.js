console.log("hi usha")
var fs = require('fs');
        fs.writeFile("/tmp/test", "Hey there!", function(err) {
            if(err) {
                return console.log(err);
            }

            console.log("The file was saved!");
        }); 
fs.appendFile('message.py', 'data to append', function (err) {

});
