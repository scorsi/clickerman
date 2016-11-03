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