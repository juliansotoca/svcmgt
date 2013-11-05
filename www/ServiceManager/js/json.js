var services={"services":[
        {
			"service": "service1",
            "backend":"serverX",
            "backup":"serverY",
            "frontedns": [
				"fend1",
				"fend2",
				"fend3"
			],
			"bbdd": [
				"bbdd1",
				"bbdd2"
			],
			"other": "N/A"
        },
        {
			"service": "service2",
            "backend":"serverW",
            "backup":"serverZ",
            "frontedns":["fend4", "fend3"],
            "bbdd": [
				"bbdd3",
				"bbdd4"
			],
            "other": "N/A"
        },

]}
//var services = '[{"service":"service1","ID":"1"}, {"service":"service2","ID":"2"}]';
var jsonp = '[{"Language":"jQuery","ID":"1"}, {"Language":"C#","ID":"2"}]';
var lang = '';

