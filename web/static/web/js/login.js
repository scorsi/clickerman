$(document).ready()
{
	var 		cur_window;
	var 		windows;
	var 		window_titles;

	windows = ["#start_panel", "#login_panel", "#email_panel", "#signin_panel"];
	window_titles = ["Mode de Connexion", "Connexion", "Email envoyé", "Créer un compte"];
	cur_window = windows[0];

	function	switch_window(window_title, next_window, focus_element)
	{
		var		speed;

		speed = 400;
		$("#window_title > span").stop().fadeOut(speed, function()
		{
			$("#window_title > span").html(window_title);
			$("#window_title > span").stop().fadeIn(speed);
		});
		$(cur_window).stop().fadeOut(speed, function()
		{
			$(next_window).stop().fadeIn(speed);
			if (focus_element != null)
				$(focus_element).focus();
		});
		cur_window = next_window;
	}

	$("#signin_button").click(function()
	{ switch_window(window_titles[3], windows[3], null); });

	$("#password_lost").click(function()
	{ switch_window(window_titles[2], windows[2], null); });

	$(".back_to_login").click(function()
	{ switch_window(window_titles[0], windows[0], null); });

	function	check_email()
	{
		return (true);
	}

	$("#form_email").submit(function(e)
	{
		e.preventDefault();
		console.log($("#email_user").val());
		if (check_email() == true)
		{			
			$("#id_useremail").val($("#email_user").val());
			switch_window(window_titles[1], windows[1], "#id_password");
		}
		else
		{

			switch_window(window_titles[3], windows[3]);
		}
	});
};