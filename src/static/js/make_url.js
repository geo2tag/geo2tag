function MakeUrlForChannelId(par, channel_id){
    var POINT = 'point';
    var NUMBER = 'number';
    var CHANNEL_IDS = 'channel_ids';
    var SERVICE_NAME = 'serviceName';
    var jsoolayer_additive = "&lat1={lat1}&lat2={lat2}&lon1={lon1}&lon2={lon2}";
    var PATH = getUrlWithPrefix('/service/' + par[SERVICE_NAME] + '/' + POINT);
    var uri = new URI({
        path: PATH
    });
    uri.addSearch({'number': par[NUMBER], 'channel_ids': channel_id});
    url = uri.toString() + jsoolayer_additive;
    return url;
}

