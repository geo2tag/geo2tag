function queryChannelsAndPoints(callBack, countChannels, countPoints, serviceName){
    $.ajax({
       type: "GET",
       url: getUrlWithPrefix('/service/') + serviceName + "/channel?number=2000",
       success: function(channels){
         countChannels = channels.length;
         $.each(channels, function(index){
            var channelId = this._id.$oid;
            $.ajax({
               type: "GET",
               url: getUrlWithPrefix("/service/) + serviceName + "/point?number=2000&channel_ids=" + channelId,
               success: function(points){
                 countPoints += points.length;
                 if (index == channels.length - 1) {
                    return callBack(countPoints, countChannels);
                 }
                }
            });
         });
       }
     });
}
function updateCounts(countPoints, countChannels){
    $('.channels-count').text(countChannels);
    $('.points-count').text(countPoints);
}

function getServiceName(){
    var url_service = location.href;
    var service_str_const = 'service/';
    var length_service_str_const = service_str_const.length;
    var service_str_index = url_service.indexOf(service_str_const);
    var result = url_service.substring(service_str_index + length_service_str_const);
    return result;
}

$(document).ready(function(){
    var countChannels = 0, countPoints = 0;
    queryChannelsAndPoints(updateCounts, countChannels, countPoints, getServiceName());
});
