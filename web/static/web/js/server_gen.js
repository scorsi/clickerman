/*
* @Author: yoppoy
* @Date:   2017-01-31 16:01:55
* @Last Modified 2017-01-31
* @Last Modified time: 2017-01-31 17:56:05
FILE FOR SERVER BASED GENERATION ON NUMBERS
*/

var getJSON = function(url) {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open('get', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status == 200) {
        resolve(xhr.response);
      } else {
        reject(status);
      }
    };
    xhr.send();
  });
};

function 	generate_num()
{
	var 	random;
	var 	JData;

    var data = '{"name": "mkyong","age": 30,"address": {"streetAddress": "88 8nd Street","city": "New York"},"phoneNumber": [{"type": "home","number": "111 111-1111"},{"type": "fax","number": "222 222-2222"}]}';

	var json = JSON.parse(data);

	getJSON('http://localhost:8000/api/bundle/1/click').then(function(data) {
   			JData = JSON.parse(JSON.stringify(data));
   			alert(JData.personal.position);
   			return (JData.personal.position);
   		}, function(status) { //error detection....
  			alert('Something went wrong.');
  	});
}
