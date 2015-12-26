requirejs.config({
	baseUrl: "js",
	paths: {
		jquery: "https://code.jquery.com/jquery-1.11.3",
		knockout: "https://cdnjs.cloudflare.com/ajax/libs/knockout/3.4.0/knockout-debug",
	}
});

require(["main"])
