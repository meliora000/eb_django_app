var map;
var des;
var myLatLng;
function initMap() {
    setTable();
    function setTable(){
    	winx = Math.floor($("#map").width()/320);
    	$("#recommend").width(winx*320 + (winx-1) *(20));
    	//s = "#box:nth-child("+wiwnx+"n+"+winx+")"
		$('#box:nth-child(1n)').css({"margin-right":20})
    	$("#box:nth-child("+winx+"n)").css({"margin-right":0})

    }
	$(window).resize(function(){
        $(".text").text($(this).width() + "< {} >" + $(this).height() + " :: >>" + winx)
        setTable()
		map.setCenter(myLatLng);
	});
function nullanimate(){
	for(i=0; i<markers.length;i++){
		markers[i].setAnimation(null)
	}
}
$("button.e").click(function(e){
        e.stopPropagation();
		//$(this).parent().parent().parent().animate({"left" : -320 })
		$(this).parent().parent().find('.posting').animate({"bottom":0})
});

$('html').click(function() {
    $('.posting').animate({"bottom":-320});
});
$(".posting").click(function(e){
   e.stopPropagation();
})
    $("button.b").click(function(){
    x = $(this).parent().parent().parent().parent().index();
    latlng = $(this).parent().parent().find('.latlng').text().split(",")
	coffeelat = parseFloat(latlng[0]);
	coffeelng = parseFloat(latlng[1]);
	coffeelat = Math.abs((coffeelat + myLatLng.lat)/2)
	coffeelng = Math.abs((coffeelng + myLatLng.lng)/2)

	map.setCenter({lat:coffeelat,lng:coffeelng})



    nullanimate();
    $('html, body').animate({
    	scrollTop:0},300);
    markers[x].setAnimation(google.maps.Animation.BOUNCE);
});
 $("button.left").click(function(){
		$(this).parent().parent().animate({"left" : 0 })

});
	var fulladdress = document.getElementsByClassName("addAndloc")[0].innerHTML.split(",");
	var add = fulladdress[0]
	var lati = parseFloat(fulladdress[1]);
    var lngo = parseFloat(fulladdress[2]);
	myLatLng = {lat: lati, lng: lngo};
	 var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 17,
    center: myLatLng,
  });

  marker = new google.maps.Marker({
    map: map,
    draggable: true,
    animation: google.maps.Animation.DROP,
    position: myLatLng,
    title:"You are HERE",
  });

  marker.addListener('click', toggleBounce);

	var info = document.getElementById("memo").innerHTML;
	var datas = info.split(",");
	var dataL = datas.length;
	var ul = document.getElementById("lists");
	var markers= [];
  for(i = 0; i <dataL; i++){
		var d = datas[i].split('-');
		cname = d[0];
		clat = parseFloat(d[1]);
		clng = parseFloat(d[2]);


		m = new google.maps.Marker({
			position: {lat: clat, lng: clng},
			map:map,
			title:cname,
			icon:"http://joseph92.dothome.co.kr/coffee.png",
	});
	markers.push(m);
}
function toggleBounce() {
  if (marker.getAnimation() !== null) {
    marker.setAnimation(null);
  } else {
    marker.setAnimation(google.maps.Animation.BOUNCE);
  }
}
$('.a').click(function(){
        var coffeeid = $(this).parent().parent().find('.coffeeID').text()
       $.ajax({
        url:'../favorite/post/',
        type:'POST',
        data:{'hello':coffeeid,'csrfmiddlewaretoken': csrftoken
        },
        success: function(response) {
        alert(response.message)
            },
    });
})


}

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


