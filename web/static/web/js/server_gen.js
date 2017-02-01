/*
* @Author: yoppoy
* @Date:   2017-01-31 16:01:55
* @Last Modified 2017-02-01
* @Last Modified time: 2017-02-01 09:41:27
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

function  update_info(data)
{
  //UPDATE ALL OF CURRENT INFO
}

function 	generate_num(callback, event)
{
	var 	random;
	var 	JData;

  getJSON(window.location.origin + '/api' + window.location.pathname + '/click').then(function(data) {
   			JData = JSON.parse(JSON.stringify(data));
        callback(JData.personal.score, event);
        update_info(JData);
  }, function(status) { //error detection....
  			alert('Un problème est survenu');
  });
}
