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
               url: "/instance/service/testservice/point?number=2000&channel_ids=" + channelId,
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

$(document).ready(function(){
    var countChannels = 0, countPoints = 0;
    queryChannelsAndPoints(updateCounts, countChannels, countPoints, getServiceName());
});
