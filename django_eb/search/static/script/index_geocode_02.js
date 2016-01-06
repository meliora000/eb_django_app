function initMap() {
	//Create Default Map
	var map = new google.maps.Map(document.getElementById('status'), {
		center: {lat: -34.397, lng: 150.644},
		zoom: 17,
	});
	var geocoder = new google.maps.Geocoder();
	var geocoder1 = new google.maps.Geocoder;
	var infowindow = new google.maps.InfoWindow;


	// Option(1) Find current location

	//If could find location
	if (navigator.geolocation) {
	  //Get current location
	  navigator.geolocation.getCurrentPosition(function(position) {
	  var pos = {
	  lat: position.coords.latitude,
	  lng: position.coords.longitude
	  };
	  //Implement on Map
	  geocodeLatLng(geocoder1, map, infowindow,pos);
	}, function() {
	handleLocationError(true, infoWindow, map.getCenter());
	});
	} else {
	// Browser doesn't support Geolocation
	handleLocationError(false, infoWindow, map.getCenter());
	}

	// END-Option(1)

	// Option(2) When user input data
	// by Press Enter
	// find Address
	document.getElementById('address').addEventListener('keydown',function(e){
		if(e.keyCode==13) {
			geocodeAddress(geocoder, map, infowindow);
			event.preventDefault();
			return false;
		}
	});
	}

	function geocodeAddress(geocoder, resultsMap,info) {
	  var address = document.getElementById('address').value;
	  geocoder.geocode({'address': address}, function(results, status) {
		if (status === google.maps.GeocoderStatus.OK) {
			var pos = {
				lat:results[0].geometry.location.lat(),
				lng:results[0].geometry.location.lng()
			}
		  geocodeLatLng(geocoder,resultsMap,info,pos);
	    }
		else {
		  alert('올바른 주소를 입력해 주세요');
		}
	  });
	}

	function handleLocationError(browserHasGeolocation, infoWindow, pos) {
	infoWindow.setPosition(pos);
	infoWindow.setContent(browserHasGeolocation ?
	'Error: The Geolocation service failed.' :
	'Error: Your browser doesn\'t support geolocation.');
	}

	function setAddress(add,loc){
	  document.getElementById('address').value=add+","+loc.lat+","+loc.lng;
	}

	function geocodeLatLng(geocoder, map, infowindow,latlng) {
		map.setCenter(latlng)
	  geocoder.geocode({'location': latlng}, function(results, status) {
		if (status === google.maps.GeocoderStatus.OK) {
		  if (results[1]) {
			var marker = new google.maps.Marker({
			  position: latlng,
			  map: map,
	  });
	  infowindow.setContent(results[1].formatted_address);
	  setAddress(results[1].formatted_address,latlng);
	  infowindow.open(map, marker);
	  saveonBrowser(results[1].formatted_address,latlng);

	} else {
	window.alert('No results found');
	}
	} else {
	window.alert('Geocoder failed due to: ' + status);
	}
	});

}

	function saveonBrowser(add,loc){
		localStorage.setItem('address',add);
		localStorage.setItem('lat',loc.lat);
		localStorage.setItem('lng',loc.lng);
	}