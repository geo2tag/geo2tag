var map = null, proj4326 = null, projmerc = null, markers = null, vectorLayer = null, 
    controls = null, positionMarker=null;

function fixMapSize(){
    var content = $("#map");
    var viewHeight = $(window).height() - content.offset().top;
    if(viewHeight < 0)
        viewHeight = viewHeight + 300;
    content.height(viewHeight);
    content.parent().width($(window).width())
    map.invalidateSize();
}

$(document).ready(function (){
    map = createMap('map', true);

    $(window).on('resize', fixMapSize());
    var callbackSuccess = function (data) {
        var len = data.length;
        for(var i = 0; i < len; i++ ){
            var text = "<b>" + data[i]['_id']['$oid'] + "</b>";
            L.marker([data[i]['location']['coordinates'][0], data[i]['location']['coordinates'][1]]).addTo(map)
            .bindPopup(text).openPopup();
        }
    };
    var callbackFail = function () {

    };
    var getPointForMap = new Geo2TagRequests('test', 'test');
    getPointForMap.getPoints(par['serviceName'], callbackSuccess, callbackFail, par['channel_ids'], 1000);
});
