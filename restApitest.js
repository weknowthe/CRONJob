//1.
var http = require('http');
 
var emp = [];
 
//2.
//http://rest-service.guides.spring.io/greeting
var extServerOptions = {
    host: 'rest-service.guides.spring.io',
    //port: '3752',
    path: '/greeting',
    method: 'GET'
};
//3.
function get() {
    http.request(extServerOptions, function (res) {
        res.setEncoding('utf8');
        res.on('data', function (data) {
            emp = JSON.parse(data);
            //emp.foreach(function (e) {
                console.log(emp.id + "\t" + emp.content );
           // });
        });
 
    }).end();
};
 
get();