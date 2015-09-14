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
    var path_marker = '../../../static/img';
    var COORDINATES = 'coordinates'
    var LOCATION = 'location'
    var SERVICE_NAME ='serviceName'
    var CHANNEL_IDS = 'channel_ids'
    var mapIcon = L.icon({
        iconUrl: path_marker + '/marker-icon.png',
        shadowUrl: path_marker + '/marker-shadow.png',
        popupAnchor:  [11, 0]
    });
    var callbackSuccess = function (data) {
        var len = data.length;
        var markers = new L.MarkerClusterGroup();
        for(var i = 0; i < len; i++ ){
            var text = getPointPopupHtml(data[i]);
            markers.addLayer(L.marker([data[i][LOCATION][COORDINATES][0], data[i][LOCATION][COORDINATES][1]], {icon: mapIcon}).bindPopup(text).openPopup());
        }
        map.addLayer(markers);
    };
    var callbackFail = function () {

    };
    var getPointForMap = new Geo2TagRequests('map', 'map');
    getPointForMap.getPoints(par[SERVICE_NAME], callbackSuccess, callbackFail, par[CHANNEL_IDS], 1000);
});
