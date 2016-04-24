function getUrlPage(){
    return window.location.toString();
}

var NUMBER_VAL = 1000;
var ZOOM_VAL = 14;

function getArgsQueryForMap(url, channel_ids){ // return json
    var uri = new URI(url);
    var params = uri.search();
    var SERVICE = 'service/';
    var MAP = '/map';
    var ZOOM = 'zoom';
    var NUMBER = 'number';
    var SERVICE_NAME_FIELD = 'serviceName';
    var CHANNEL_IDS = 'channel_ids'
    var index_beg = url.indexOf(SERVICE) + SERVICE.length;
    var index_end = url.indexOf(MAP);
    var SERVICE_NAME = url.substring(index_beg, index_end)
    result = URI.parseQuery(params);
    result[SERVICE_NAME_FIELD] = SERVICE_NAME;
    if(result[NUMBER] == undefined)
        result[NUMBER] = NUMBER_VAL;
    if(result[ZOOM] == undefined)
        result[ZOOM] = ZOOM_VAL;
    if(channel_ids.length != 0)
        result[CHANNEL_IDS] = channel_ids
    else if(result[CHANNEL_IDS] != undefined)
        result[CHANNEL_IDS] = JSON.parse(result[CHANNEL_IDS])
    return result;
}
