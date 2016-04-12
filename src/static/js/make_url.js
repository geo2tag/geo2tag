function MakeUrlByChannelIds(service_name,channel_ids,number_point){
    var POINT = 'point';
    var NUMBER = 'number';
    var CHANNEL_IDS = 'channel_ids';
    var url = getUrlWithPrefix('/service/') + service_name;
    var str_channel_ids = '';
    if(channel_ids != undefined){
        for(var i = 0;i<channel_ids.length;i++){
            str_channel_ids += '&' + CHANNEL_IDS +'=' + channel_ids[i];
        }
    }
    url = url + '/' + POINT + '?' + NUMBER + '=' + number_point + str_channel_ids;
    console.log(url)
    return url;
}
