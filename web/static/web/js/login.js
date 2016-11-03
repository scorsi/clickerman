$(document).ready()
{
	var 		switch_speed;
	var 		cur_window;
	var 		num_window;
	var 		windows;
	var 		window_titles;
	var 		cur_userform;
	var 		num_userform;
	var 		userforms;
	var 		userform_titles;
	var 		cur_enterpriseform;
	var 		num_enterpriseform;
	var 		enterpriseforms;
	var 		enterpriseform_titles;

	switch_speed = 400;
	num_userform = 0;
	userforms = ["#form_create_user_1", "#form_create_user_2", "#form_create_user_3"];
	userform_titles = ["Informations générales", "Adresse (2/3)", "Mot de passe"];
	cur_userform = userforms[0];
	num_enterpriseform = 0;
	enterpriseforms = ["#form_create_enterprise_1", "#form_create_enterprise_2", "#form_create_enterprise_3", "#form_create_enterprise_4"];
	enterpriseform_titles = ["Informations générales", "Responsable du compte", "Mot de passe", "Mot de passe"];
	cur_enterpriseform = enterpriseforms[0];
	num_window = 0;
	windows = ["#start_panel", "#choose_signin", "#login_panel", "#email_panel", "#signin_user_panel", "#signin_enterprise_panel"];
	window_titles = ["Mode de Connexion", "Type de compte", "Connexion", "Email envoyé", userform_titles[0], enterpriseform_titles[0]];
	cur_window = windows[0];


	function	switch_window_type(next_window, focus_element, cur_element, type)
	{
		$(cur_element).stop().fadeOut(switch_speed, function()
		{
			$(next_window).stop().fadeIn(switch_speed);
			if (focus_element != null)
				$(focus_element).focus();
		});
		if (type == 1)
			cur_window = next_window;
		else if (type == 2)
			cur_userform = next_window;
		else
			cur_enterpriseform = next_window;
	}

	function	switch_window(window_title, next_window, focus_element, type)
	{
		$("#window_title > span").stop().fadeOut(switch_speed, function()
		{
			$("#window_title > span").html(window_title);
			$("#window_title > span").stop().fadeIn(switch_speed);
		});
		if (type == 1)
			switch_window_type(next_window, focus_element, cur_window, type);
		else if (type == 2)
			switch_window_type(next_window, focus_element, cur_userform, type);
		else if (type == 3)
			switch_window_type(next_window, focus_element, cur_enterpriseform, type);
	}

	$("#signin_button").click(function()
		{ switch_window(window_titles[4], windows[4], null, 1); });

	$("#password_lost").click(function()
		{ switch_window(window_titles[3], windows[3], null, 1); });

	$(".back_to_login").click(function()
		{ switch_window(window_titles[0], windows[0], null, 1); });

	$("#choose_user").click(function()
		{ switch_window(window_titles[4], windows[4], "#create_user_lastname", 1); });

	$("#choose_entreprise").click(function()
		{ switch_window(window_titles[5], windows[5], "#create_enterprise_name", 1); });


	manage_date_select();
	function 	manage_date_select()
	{
		var 	months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
		var 	cur_year = new Date().getFullYear();

		select_generator("#create_user_bd_day", 1, 31);
		select_generator("#create_user_bd_year", cur_year, 1905);
	}

	function	check_email()
	{
		return (true);
	}

	$("form").submit(function(e)
	{
		e.preventDefault();
	});

	$("#form_create_user_1").submit(function(e)
	{
		e.preventDefault();
		switch_window(userform_titles[1], userforms[1], "#create_user_address", 2);
	});

	$("#form_create_user_2").submit(function(e)
	{
		e.preventDefault();
		switch_window(userform_titles[2], userforms[2], "#create_user_password1", 2);
	});

	$("#form_create_enterprise_1").submit(function(e)
	{
		e.preventDefault();
		switch_window(enterpriseform_titles[1], enterpriseforms[1], "#create_enterprise_profile_lastname", 3);
	});

	$("#form_create_enterprise_2").submit(function(e)
	{
		e.preventDefault();
		switch_window(enterpriseform_titles[2], enterpriseforms[2], "#create_user_password1", 3);
	});

	$("#form_email").submit(function(e)
	{
		e.preventDefault();
		$("input[type='email']").each(function(){ $(this).val($("#email_user").val()); });
		if (check_email() == true)
		{
			switch_window(window_titles[1], windows[1], "#id_password", 1);
		}
		else
		{
			switch_window(window_titles[4], windows[4], 1);
		}
	});


};