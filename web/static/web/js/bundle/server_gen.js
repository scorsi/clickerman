/*
* @Author: yoppoy
* @Date:   2017-01-31 16:01:55
* @Last Modified 2017-02-02
* @Last Modified time: 2017-02-02 19:19:35
FILE FOR SERVER BASED GENERATION ON NUMBERS
*/

cur_score = $("#player_score").html();

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
  if (data != 'undefined')
  {
    $("#player_rank").html(data.position);
    $("#player_remaining_clicks").html(data.last_clicks);
    $("#player_clicks").html(data.clicks);
 }
}

function  show_no_clicks()
{
  generate_status = true;
  window.location.replace(window.location.origin + window.location.pathname + "#out_of_clicks");
}

function  update_leaderboard(data)
{
  var     data = '{leaderboard:["10000", "78987", "678", "56", "78", "7"]}';
  var     a;

  a = 0;
  while (a < 10)
  {
      $($("#score_container").children() + ":eq(" + a + ")").html("h");
    a++;
  }
}

function  call_leaderboard()
{
  getJSON(window.location.origin + '/api' + window.location.pathname + '/leaderboard').then(function(data) {
        JData = JSON.parse(JSON.stringify(data));
        if (!JData.hasOwnProperty('error'))
          update_leaderboard(JData);
        else
          alert("Erreur : " + JData.error);
  }, function(status) { //error detection....
        alert('Un problème est survenu');
  });
}

function 	generate_num(callback, event)
{
	var 	random;
	var 	JData;

  generate_status = false;
  getJSON(window.location.origin + '/api' + window.location.pathname + '/click').then(function(data) {
        JData = JSON.parse(JSON.stringify(data));
        if (!JData.hasOwnProperty('error'))
        {
          callback(JData.score, event);
          update_info(JData);
          generate_status = true;
        }
        else if (data.error == "no_last_clicks")
          show_no_clicks();
        else
          alert("Erreur : " + JData.error);
  }, function(status) { //error detection....
  			alert('Un problème est survenu');
  });
}

//HERE TO MANAGE THE APPEARANCE OF THE OUT OF CLICKS MODAL ON THE LOADING OF THE PAGE
check_modal_condition();
function  check_modal_condition()
{
  if (window.location.href.endsWith("#out_of_clicks") && !($("#player_remaining_clicks").html() == "0"))
    window.location.replace(window.location.origin + window.location.pathname);
   if (window.location.href.endsWith("#out_of_clicks") == false && $("#player_remaining_clicks").html() == "0")
    window.location.replace(window.location.origin + window.location.pathname + "#out_of_clicks");
}