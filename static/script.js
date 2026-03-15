function getDermatologists(){

navigator.geolocation.getCurrentPosition(function(pos){

let lat=pos.coords.latitude;
let lng=pos.coords.longitude;

fetch(`/dermatologists?lat=${lat}&lng=${lng}`)
.then(res=>res.json())
.then(data=>{

let list=document.getElementById("dermatologist-list");

data.results.forEach(doc=>{

list.innerHTML+=`
<div class="dermatologist-card">

<h4>${doc.name}</h4>

<p>${doc.vicinity}</p>

<p>⭐ ${doc.rating}</p>

<a href="https://www.google.com/maps/search/?api=1&query=${doc.name}" target="_blank">

<button>Directions</button>

</a>

</div>
`;

});

});

});

}