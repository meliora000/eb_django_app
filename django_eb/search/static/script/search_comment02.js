$('.taste_box').mousemove(function(e){
		var offset = $(this).offset();
		var x = e.clientX - offset.left;
		var y = e.clientY - offset.top;
		var size = x+20 + "px "
		if(x>=10 && x<=130){
			$(this).css({
				'width':size
		});
		rate= parseInt(((x+22)/30)*10)/10
		$(this).parent().find(".taste").text("맛: "+rate+"/5.0");
		}
		
});

$('.mood_box').mousemove(function(e){
		var offset = $(this).offset();
		var x = e.clientX - offset.left;
		var y = e.clientY - offset.top;
		var size = x+20 + "px "
		if(x>=10 && x<=130){
			$(this).css({
				'width':size
		});
		rate= parseInt(((x+22)/30)*10)/10
		$(this).parent().find(".mood").text("분위기: "+rate+"/5.0");
		}
		
});


$('.price_box').mousemove(function(e){
		var offset = $(this).offset();
		var x = e.clientX - offset.left;
		var y = e.clientY - offset.top;
		var size = x+20 + "px "
		if(x>=10 && x<=130){
			$(this).css({
				'width':size
		});
		rate= parseInt(((x+22)/30)*10)/10
		$(this).parent().find(".price").text("가격: "+rate+"/5.0");
		}
		
});

