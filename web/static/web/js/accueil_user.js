$(document).ready(function()
{
	$(".product-img").mouseenter(function(){
		$(this).find(".hover-info").stop().fadeIn(200);
		$(this).find(".initial-info").stop().fadeOut(200);
	});
	$(".product-img").mouseleave(function(){
		$(this).find(".hover-info").stop().fadeOut(200);
		$(this).find(".initial-info").stop().fadeIn(200);
	});
	$(".product-img").focusin(function(){
		$(this).find(".hover-info").stop().fadeIn(200);
		$(this).find(".initial-info").stop().fadeOut(200);
	});
	$(".product-img").focusout(function(){
		$(this).find(".hover-info").stop().fadeOut(200);
		$(this).find(".initial-info").stop().fadeIn(200);
	});
});