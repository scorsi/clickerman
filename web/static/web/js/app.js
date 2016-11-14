function 	select_generator(id, start, end)
{
	var 	count;

	count = start;
	if (count <= end)
	{
		while (count <= end)
		{
			$(id).append("<option value=" + count +">" + count + "</option>");
			count++;
		}
	}
	else
	{
		while (count >= end)
		{
			$(id).append("<option value=" + count +">" + count + "</option>");
			count--;
		}
	}
}

function 	select_update_color(object) {
	$(object).css('color','#f60');
};

function 	scrollTo(id)
{
	if ($(id).length != 0)
	{
		$('html, body').stop().animate({
			scrollTop: $(id).offset().top + 1
		}, 500, 'swing');
		return false;
	}
}

$(document).ready()
{
	$('a').click(function(){
		scrollTo($(this).attr('href'));
	});
}