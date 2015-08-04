function Geo2TagRequests(server, instance) {
	this.server = server;
	this.instance = instance;

	this.getChannels = function(serviceName, callback, substring, number, offset) {
		$.get(getUrlWithPrefix('/service/') + serviceName + '/channel', {'substring': substring, 'number': number, 'offset': offset})
        .done(callback(data));
	};

	this.getPoints = function(serviceName, callback, channel_ids, number, geometry, altitude_from, 
		                      altitude_to, substring, date_from, date_to, offset, radius) {
		$.get(getUrlWithPrefix('/service/') + serviceName + '/point', {'channel_ids': channel_ids, 'number': number, 
			                  'geometry': geometry, 'altitude_from': altitude_from, 'altitude_to': altitude_to, 'substring': substring,
			                  'date_from': date_from, 'date_to': date_to, 'offset': offset, 'radius': radius})
        .done(callback(data));
	};
};