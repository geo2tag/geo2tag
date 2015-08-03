function Geo2TagRequests(server, instance) {
	this.server = server;
	this.instance = instance;

	this.getChannels = function(serviceName, callback, getParams) {
		$.get(getUrlWithPrefix('/service/') + serviceName + '/channel?' + getParams)
        .done(callback);
	};
};