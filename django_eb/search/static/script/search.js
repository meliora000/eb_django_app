var map;
var des;
var myLatLng;
function initMap() {
function nullanimate(){
	for(i=0; i<markers.length;i++){
		markers[i].setAnimation(null)
	}
}
$("button.e").click(function(){
		$(this).parent().parent().parent().animate({"left" : -320 })
});
    $("button.b").click(function(){
    x = $(this).parent().parent().parent().parent().index();
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
}


