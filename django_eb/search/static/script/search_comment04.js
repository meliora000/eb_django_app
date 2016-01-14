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

$('.postform').submit(function(e){
	comment = $(this).find('textarea').val();
	taste = $(this).find('.taste').text().split(" ")[1].split("/")[0];
	mood = $(this).find('.mood').text().split(" ")[1].split("/")[0];
	price = $(this).find('.price').text().split(" ")[1].split("/")[0];
	coffeeid =$(this).parent().parent().find('.coffeeID').text();
		$.ajax({
        url:'../comment/post/',
        type:'POST',
        data:{'comment':comment,'taste':taste,'coffeeid':coffeeid,'mood':mood,'price':price,'csrfmiddlewaretoken': csrftoken
        },
        success: function(response) {
        //alert("added successfully")
            },
    });
	e.preventDefault();
})


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});