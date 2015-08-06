function Geo2TagRequests(server, instance) {
    this.server = server;
    this.instance = instance;
};
Geo2TagRequests.prototype.getChannels = function(serviceName, callbacksuccess, callbackfail, substring, number, offset) {
    $.get(getUrlWithPrefix('/service/') + serviceName + '/channel', {'substring': substring, 'number': number, 'offset': offset})
    .fail(function(jqXHR, textStatus, errorThrown){ callbackfail(jqXHR, textStatus, errorThrown) })
    .done(callbacksuccess(data));
};

Geo2TagRequests.prototype.getPoints = function(serviceName, callbacksuccess, callbackfail, channel_ids, number, geometry, altitude_from, altitude_to, substring, date_from, date_to, offset, radius) { 
    $.get(getUrlWithPrefix('/service/') + serviceName + '/point', {'channel_ids': channel_ids, 'number': number,'geometry': geometry, 'altitude_from': altitude_from, 'altitude_to': altitude_to, 'substring': substring,'date_from': date_from, 'date_to': date_to, 'offset': offset, 'radius': radius})
    .fail(function(jqXHR, textStatus, errorThrown){ callbackfail(jqXHR, textStatus, errorThrown) })
    .done(callbacksuccess(data));
    /*$.ajax({
        type: "GET",
        traditional: true,
        url: getUrlWithPrefix('/service/') + serviceName + '/point',
        data: { channel_ids:channel_ids , 'number': number,'geometry': geometry, 'altitude_from': altitude_from, 'altitude_to': altitude_to, 'substring': substring,'date_from': date_from, 'date_to': date_to, 'offset': offset, 'radius': radius },
        success: function(result)
        {
        	console.log(result);
        },
        error: function(XMLHttpRequest, textStatus, errorThrown)
        {

        }
});*/
};
