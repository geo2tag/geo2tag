$(document).ready(function(){
	var countChannels = 0, countPoints = 0;
	$.ajax({
	   type: "GET",
	   url: "/instance/service/testservice/channel?number=2000",
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
					return updateCounts();
			     }
			    }
			});
	     });
	   }
	 });
	function updateCounts(){
		$('.channels-count').text(countChannels);
		$('.points-count').text(countPoints);
	}
});