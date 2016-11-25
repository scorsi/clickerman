var 		submit = 0;
function 	show_submitbar()
{
	$(".submit_bar").slideDown();
	submit = 1;
}

$(document).ready(function()
{
	$(".form_field").bind("change", function() {
		show_submitbar();
	});

	$("#form_profile").submit(function()
	{
		if (submit == 1)
			return true;
		else
			return false;
	});
});
