var map = null, proj4326 = null, projmerc = null, markers = null, vectorLayer = null, 
    controls = null, positionMarker=null;

function fixMapSize(){
    var content = $("#map");
    var viewHeight = $(window).height() - content.offset().top;
    console.log('Window width = '+$(window).width());
    if(viewHeight < 0)
        viewHeight = viewHeight + 300;
    content.height(viewHeight);
    console.log('Window width = '+$(window).width());
//    content.parent().width($(window).width())
    console.log('Window width = '+$(window).width());
    console.log('Content width = '+content.width());
    console.log('Content.parent width = '+content.parent().width());
    console.log('content.parent()');
    console.log(content.parent());
    map.invalidateSize();
}

$(document).ready(function (){
    if(par.latitude != null && par.longitude != null)
        map = createMap('map', false, par.zoom, par.latitude, par.longitude);
    else
        map = createMap('map', true, par.zoom)
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
    var url = MakeUrlByChannelIds(par);
    var l = new L.LayerJSON({url: url,
        propertyLoc: ['location.coordinates.0','location.coordinates.1'],
        buildPopup: function(data) {
            return data.json.name || null;
        } 
    }); 
    map.addLayer(l);
});
