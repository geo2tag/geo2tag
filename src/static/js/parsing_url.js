function getUrlPage(){
    return window.location.toString();
}

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
    var REFRESH = 'refresh'
    var LONGITUDE = 'longitude'
    var LATITUDE = 'latitude'
    var CLUSTERING = 'clustering'

    var NUMBER_VAL = 1000;
    var ZOOM_VAL = 14;
    var REFRESH_VAL = 30;
    var LATITUDE_VAL = 63.377;
    var LONGITUDE_VAL = 28.938;    
    var CLUSTERING_VAL_FALSE = false;
    var CLUSTERING_VAL_TRUE = true;

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
    if(result[REFRESH] == undefined)
        result[REFRESH] = REFRESH_VAL;
    if(result[LATITUDE] == undefined)
        result[LATITUDE] = LATITUDE_VAL;
    if(result[LONGITUDE] == undefined)
        result[LONGITUDE] = LONGITUDE_VAL;
    if(result[CLUSTERING] == undefined || result[CLUSTERING] == 0)
        result[CLUSTERING] = CLUSTERING_VAL_FALSE;
    else
        result[CLUSTERING] = CLUSTERING_VAL_TRUE;
    return result;
}
