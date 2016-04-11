function MakeUrlByChannelIds(service_name,channel_ids,number_point,zoom,latitude,longitude){
    var POINT = 'point';
    var NUMBER = 'number';
    var CHANNEL_IDS = 'channel_ids';
    var url = getUrlWithPrefix('/service/') + service_name;
    var str_channel_ids = '';
    for(var i = 0;i<channel_ids.length;i++){
        str_channel_ids += '&' + CHANNEL_IDS +'=' + channel_ids[i];
    }
    url = url + '/' + POINT + '?' + NUMBER + '=' + number_point + str_channel_ids;
    return url  + "&lat1={lat1}&lat2={lat2}&lon1={lon1}&lon2={lon2}";
}