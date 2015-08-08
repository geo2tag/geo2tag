function Geo2TagRequests(server, instance) {
    this.server = server;
    this.instance = instance;
};
Geo2TagRequests.prototype.getChannels = function(serviceName, callbacksuccess, callbackfail, substring, number, offset) {
    $.get(getUrlWithPrefix('/service/') + serviceName + '/channel', {'substring': substring, 'number': number, 'offset': offset})
    .fail(function(jqXHR, textStatus, errorThrown){ callbackfail(jqXHR, textStatus, errorThrown); })
    .done(function(data){ callbacksuccess(data); });
};

Geo2TagRequests.prototype.getPoints = function(serviceName, callbacksuccess, callbackfail, channel_ids, number, geometry, altitude_from, altitude_to, substring, date_from, date_to, offset, radius) { 
    $.ajax({
        type: "GET",
        url: getUrlWithPrefix('/service/') + serviceName + '/point',
        data: { 'channel_ids':channel_ids, 'number': number,'geometry': geometry, 'altitude_from': altitude_from, 'altitude_to': altitude_to, 'substring': substring,'date_from': date_from, 'date_to': date_to, 'offset': offset, 'radius': radius },
        traditional : true
    })
    .fail(function(jqXHR, textStatus, errorThrown){ callbackfail(jqXHR, textStatus, errorThrown) })
    .done(function(data){ callbacksuccess(data); });
};
