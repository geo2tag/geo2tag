function getUrlPage(){
    return window.location.toString();
}

function getArgsQueryForMap(url, channel_ids){ // return json
    var uri = new URI(url);
    var params = uri.search();
    var SERVICE = 'service/';
    var MAP = '/map';
    var ZOOM = 'zoom';
    var SERVICE_NAME_FIELD = 'serviceName';
    var CHANNEL_IDS = 'channel_ids'
    var index_beg = url.indexOf(SERVICE) + SERVICE.length;
    var index_end = url.indexOf(MAP);
    var SERVICE_NAME = url.substring(index_beg, index_end)
    result = URI.parseQuery(params);
    console.log(result)
    result[SERVICE_NAME_FIELD] = SERVICE_NAME;
    if(result[ZOOM] == undefined)
        result[ZOOM] = 14;
    if(channel_ids.length != 0)
        result[CHANNEL_IDS] = channel_ids
    else
        result[CHANNEL_IDS] = JSON.parse(result[CHANNEL_IDS])
    console.log(result)
    return result;
}
