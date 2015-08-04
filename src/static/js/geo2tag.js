function Geo2TagRequests(server, instance) {
	this.server = server;
	this.instance = instance;

	this.getChannels = function(serviceName, callback, substring, number, offset) {
		$.get(getUrlWithPrefix('/service/') + serviceName + '/channel', {'substring': substring, 'number': number, 'offset': offset})
        .done(callback);
	};
};