function 	square_aspect(img)
{
	var 	width;
	var 	height;
	var 	padding;

	width = $(img).width();
	height = $(img).height();
	padding = (((width - height) / width) * 50) + "%";
	console.log(padding);
	$(img).css({"padding-top" : padding, "padding-bottom" : padding});
}

function 	format_number(num)
{
	var 	convert;
	var 	count;
	var 	check;

	back = num.toString();
	count = back.length;
	check = 0;
	while (count != 0)
	{
		if (check == 3)
		{
			back = back.substring(0, count) + ',' + back.substring(count, back.length);
			check = 0;
		}
		check++;
		count--;
	}
	return (back)
}


/* ----------------------------------------------------------
FUNCTION TO MANAGE RANDOM PRINT AND SCALE ANIMATION OF CIRCLE
-----------------------------------------------------------*/
var 	animation_scale;
var 	timer;
var 	cur_score = 0;

animation_scale = document.getElementById("circle-border");
document.getElementById("circle-border").addEventListener("mousedown", function(evt)
{
	var 	mouseX;
	var 	mouseY;
	var 	score;
	var 	random_num;

	if (evt.pageX)
	{
		mouseX = evt.pageX;
		mouseY = evt.pageY;
	}
	else if (evt.clientX)
	{
		MouseX = evt.clientX + ((document.documentElement.scrollLeft) ? document.documentElement.scrollLeft : document.body.scrollLeft);
		MouseY = evt.clientY + ((document.documentElement.scrollTop) ? document.documentElement.scrollTop : document.body.scrollTop);
	}
	random_num = generate_num();
	score = format_number(random_num);
	create_text(score, mouseX, mouseY);
	clearTimeout(timer);
	$(animation_scale).css({"-webkit-animation-play-state" : "paused", "animation-play-state" : "paused"});
	timer = setTimeout(function()
	{
		$(animation_scale).css({"-webkit-animation-play-state" : "running", "animation-play-state" : "runnning"});
	}, 250);
	clear_queue();
	if (random_num > cur_score)
	{	
		$('#player_score').html(score);
		shine_text();
		cur_score = random_num;
	}
});

function 	generate_num()
{
	var 	a;
	var 	random;

	a = Math.random();
	if (a < 0.1)
		random = Math.floor((Math.random() * 100000) + 0);
	else if (a < 0.2)
		random = Math.floor((Math.random() * 200000) + 0);
	else if (a < 0.3)
		random = Math.floor((Math.random() * 300000) + 0);
	else if (a < 0.4)
		random = Math.floor((Math.random() * 400000) + 0);
	else if (a < 0.5)
		random = Math.floor((Math.random() * 500000) + 0);
	else if (a < 0.6)
		random = Math.floor((Math.random() * 600000) + 0);
	else if (a < 0.7)
		random = Math.floor((Math.random() * 700000) + 0);
	else if (a < 0.8)
		random = Math.floor((Math.random() * 800000) + 0);
	else if (a < 0.9)
		random = Math.floor((Math.random() * 1000000) + 0);

	return 	(random);
}

function 	shine_text()
{
	var 	element = document.getElementById("player_score");

	$('#player_score').removeClass("shine");
	void element.offsetWidth;
	$('#player_score').addClass("shine");
}

/* -----------------------------
FUNCTIONS TO PRINT RANDOM NUMBER
------------------------------*/
function create_text(text, mouseX, mouseY)
{
	var 	score;
	var 	node;

	node = document.createTextNode(text);
	score = document.createElement("p");
	score.appendChild(node);
	score.className += "text_dissapear";
	score.style.left = mouseX + 'px';
	score.style.top = mouseY - 40 + 'px';
	$(score).appendTo($("#text-container"));
}

function 	clear_queue()
{
	var 	data_array;
	var		count;

	$('.text_dissapear').each(function()
	{
		if ($(this).css("opacity") <= 0.1)
			$(this).remove();
		count = count - 1;
	});
}


$(window).resize(function(){
	square_aspect("#circle-btn");
})

$(document).ready(function(){
	square_aspect("#circle-btn");
});