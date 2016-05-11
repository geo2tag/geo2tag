var map = null, proj4326 = null, projmerc = null, markers = null, vectorLayer = null, 
    controls = null, positionMarker=null, l=null;
var CHANNEL_IDS = 'channel_ids'

function fixMapSize(){
    var content = $("#map");
    var viewHeight = $(window).height() - content.offset().top;
    console.log('Window width = '+$(window).width());
    if(viewHeight < 0)
        viewHeight = viewHeight + 300;
    content.height(viewHeight);
    console.log('Window width = '+$(window).width());
    console.log('Window width = '+$(window).width());
    console.log('Content width = '+content.width());
    console.log('Content.parent width = '+content.parent().width());
    console.log('content.parent()');
    console.log(content.parent());
    map.invalidateSize();
}

function getLayer(url){
    var layer = new L.LayerJSON({url: url,
        propertyLoc: ['location.coordinates.0','location.coordinates.1'],
        buildPopup: function(data) {
            return data.json.name || null;
        },
        buildIcon: function(data, title) {
            var url_icon = "get_icon?channel_id=" + data.channel_id.$oid
            return new L.Icon({
                iconUrl : url_icon
            });
        }
    });
    return layer;
}

function deleteLastLayer(){
    var layers = map.eachLayer(function(l){})
    var del_layer;
    for(layer in layers._layers){
        if (layer._hashUrl == url)
            del_layer = layer._leaflet_id;
            break;
    }
    if(del_layer != undefined){
        map.removeLayer(del_layer);
    }
}


$(document).ready(function (){
    if(par.latitude != null && par.longitude != null)
        map = createMap('map', false, par.zoom, par.latitude, par.longitude);
    else
        map = createMap('map', true, par.zoom, par[CHANNEL_IDS])
    $(window).on('resize', fixMapSize());
    url = MakeUrlByChannelIds(par);
    refreshMap(url);
    if(par.refresh != 0){
        setInterval(function() {
                   deleteLastLayer()
                   refreshMap(url)}, par.refresh * 1000);
    }
});

function refreshMap(url){
    var layer = getLayer(url);
    map.addLayer(layer);
}

