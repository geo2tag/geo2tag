var map = null, proj4326 = null, projmerc = null, markers = null, vectorLayer = null, 
    controls = null, positionMarker=null, l=null;
var CHANNEL_IDS = 'channel_ids';
var layers_checked_list = []

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


$(document).ready(function (){
    var overlayMaps = getOverlayMaps();
    if(par.latitude != null && par.longitude != null)
        map = createMap('map', false, par.zoom, overlayMaps, par.latitude, par.longitude);
    else
        map = createMap('map', true, par.zoom, overlayMaps)
    $(window).on('resize', fixMapSize());
    map.on('overlayadd', function(l){
        layers_checked_list.push(l._leaflet_id);
        console.log('---- ', l)
    })
    map.on('overlayremove', function(l){
     //   layers_checked_list.push(l._leaflet_id);
        console.log('---- ', layers_checked_list)
    })
    refreshMap(overlayMaps);
    if(par.refresh != 0){
        setInterval(function() {
               refreshMap(url)}, par.refresh * 1000);
    }
});

function refreshMap(overlayMaps){    
    
    for(var key in map['control']._layers){
        if(map['control']._layers[key].overlay){
            map['control'].removeLayer(map['control']._layers[key].layer)
       } 
    }
    map.eachLayer(function(l){
        if(l._hashUrl)
            map.removeLayer(l);
    });    
    map['control'] = setOverlayMaps(map['control']);
}

