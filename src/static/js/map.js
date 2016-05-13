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

function getLayerForChannelId(channel_id, url){
    var layer = new L.LayerJSON({url: url,
         propertyLoc: ['location.coordinates.0','location.coordinates.1'],
         buildPopup: function(data) {
             return data.json.name || null;
         },
         buildIcon: function(data, title) {
             var url_icon = "get_icon?channel_id=" + channel_id;
             return new L.Icon({
                 iconUrl : url_icon
             });
         }
     });
     return layer;
}

function getOverlayMaps(){
    overlayMaps = {}
    for(var i = 0; i < par[CHANNEL_IDS].length; i++){
        channel_id = par[CHANNEL_IDS][i];
        url = MakeUrlForChannelId(par, channel_id);
        overlayMaps[channel_id] = getLayerForChannelId(channel_id, url);
    }
}


$(document).ready(function (){
    overlayMaps = getOverlayMaps();
    if(par.latitude != null && par.longitude != null)
        map = createMap('map', false, par.zoom, overlayMaps, par.latitude, par.longitude);
    else
        map = createMap('map', true, par.zoom, overlayMaps)
    $(window).on('resize', fixMapSize());
    var control = new L.Control.Layers(layers, overlayMaps)
    map.addControl(control);
    refreshMap(url);
    if(par.refresh != 0){
        setInterval(function() {
                                       
                   refreshMap(url)}, par.refresh * 1000);
    }
});

function refreshMap(url){
    overlayMapshttp://leafletjs.com/reference.html#control-layers-addoverlay = getOverlayMaps();
    addOverlay()
}

