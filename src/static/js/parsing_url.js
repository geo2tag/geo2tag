function getUrlPage(){
    return window.location.toString();
}

function getArgsQuery(url){ // return json
    var uri = new URI(url);
    var params = uri.search();
    var SERVICE = 'service/';
    var MAP = '/map';
    var ZOOM = 'zoom';
    var SERVICE_NAME_FIELD = 'serviceName';
    var index_beg = url.indexOf(SERVICE) + SERVICE.length;
    var index_end = url.indexOf(MAP);
    var SERVICE_NAME = url.substring(index_beg, index_end)
    result = URI.parseQuery(params);
    result[SERVICE_NAME_FIELD] = SERVICE_NAME;
    if(result[ZOOM] == undefined)
        result[ZOOM] = 14;
    console.log(result)
    return result;
}
