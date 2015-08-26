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
    var markers = new L.MarkerClusterGroup();
    markers.addLayer(L.marker([59.57, 30.19]));
    markers.addLayer(L.marker([59.82, 30.69]));
    markers.addLayer(L.marker([59.22, 31.19]));
    map.addLayer(markers);
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
        for(var i = 0; i < len; i++ ){
            var text = "<b>" + data[i]['_id']['$oid'] + "</b>";
            L.marker([data[i][LOCATION][COORDINATES][0], data[i][LOCATION][COORDINATES][1]], {icon: mapIcon}).addTo(map)
            .bindPopup(text).openPopup();
        }
    };
    var callbackFail = function () {

    };
    var getPointForMap = new Geo2TagRequests('map', 'map');
    getPointForMap.getPoints(par[SERVICE_NAME], callbackSuccess, callbackFail, par[CHANNEL_IDS], 1000);
});
