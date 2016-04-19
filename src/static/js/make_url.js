function MakeUrlByChannelIds(par){
    var POINT = 'point';
    var NUMBER = 'number';
    var CHANNEL_IDS = 'channel_ids';
    var SERVICE_NAME = 'serviceName';
    var jsoolayer_additive = "&lat1={lat1}&lat2={lat2}&lon1={lon1}&lon2={lon2}";
    var url = getUrlWithPrefix('/service/') + par[SERVICE_NAME];
    var str_channel_ids = '';
    if(par[CHANNEL_IDS] != undefined){
        for(var i = 0;i<par[CHANNEL_IDS].length;i++){
            str_channel_ids += '&' + CHANNEL_IDS +'=' + par[CHANNEL_IDS][i];
        }
    }
    url = url + '/' + POINT + '?' + NUMBER + '=' + par[NUMBER] + str_channel_ids + jsoolayer_additive;
    console.log(url);
    return url;
}

