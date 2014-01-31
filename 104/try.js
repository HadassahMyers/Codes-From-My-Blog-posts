var map=null;


window.onload = getLocation ;

function showMap(coords) {
	var googleLatAndLong = new google.maps.LatLng(coords.latitude,coords.longitude);
	var mapOptions	= {
		zoom: 10, 
		center: googleLatAndLong ,
		mapTypeId: google.maps.MapTypeId.ROADMAP	
	};//The option object specifying the options for the map
	var mapDiv = document.getElementById("map");
	map = new google.maps.Map(mapDiv,mapOptions);//API which gets the map
}




function getLocation() {
	if(navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(displayLocation); 
//The API calls the display location function with position object containing the positional parameters
	}
	else {
		alert("Doesnt support Geolocation");
	}
}
function displayLocation(position) {
	var latitude = position.coords.latitude ; 
	var longitude = position.coords.longitude ;

	var div = document.getElementById("Location");
	div.innerHTML = "You are at latitude: " + latitude + " Longitude: " + longitude;
	showMap(position.coords); 
	//showMap function takes in the positional parameters and displays the map
}


