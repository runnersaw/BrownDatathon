
var map = new Datamap({
	element: document.getElementById('container'),
	projection: 'mercator',
	responsive: true,
	scope: "world"
});

var bubbles = [];
var arcs = [];

function draw_bubble(country, radius) {
	bubbles.push({
		radius: radius,
		centered: country,
	});
	map.bubbles(bubbles);
}

function draw_arc_country(origin, destination, width) {
	o = getCountryLocation(origin);
	d = getCountryLocation(destination);
	if (!o || !d) {
		console.log('nope');
		return;
	}
	console.log(origin);
	console.log(o, d);
	draw_arc(o[0], o[1], d[0], d[1], width);
}

function draw_arc(origin_lat, origin_long, destination_lat, destination_long, width) {
	arcs.push({
		origin: {
			latitude: origin_lat,
			longitude: origin_long
		},
		destination: {
			latitude: destination_lat,
			longitude: destination_long
		},
		options: {
			strokeWidth: width
		}
	});
	map.arc(arcs, {strokeWidth: width, arcSharpness: 1.4});
}

draw_bubble('USA', 15);
draw_bubble('BRA', 8);
draw_arc_country('brazil', 'us', 2);
draw_arc_country('france', 'Italy', 5);


