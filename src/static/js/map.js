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
//    content.parent().width($(window).width())
    console.log('Window width = '+$(window).width());
    console.log('Content width = '+content.width());
    console.log('Content.parent width = '+content.parent().width());
    console.log('content.parent()');
    console.log(content.parent());
    map.invalidateSize();
}

function getLayer(url){
    l = new L.LayerJSON({url: url,
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
    return l;
}


$(document).ready(function (){
    var channel_layers_array = [];
    console.log(par[CHANNEL_IDS])
    for(var channel_id in par[CHANNEL_IDS]){
        layer = L.tileLayer({id: channel_id});
        console.log(layer)
        var baseMaps = {"channel_id" : layer}
        channel_layers_array.push(layer);
        L.control.layers(layer).addTo(map);
    }
    console.log(channel_layers_array)
    if(par.latitude != null && par.longitude != null)
        map = createMap('map', false, par.zoom, par.latitude, par.longitude);
    else
        map = createMap('map', true, par.zoom, channel_layers_array)
    $(window).on('resize', fixMapSize());
    var url = MakeUrlByChannelIds(par);

    if(par.refresh != 0){
        setInterval(function() {
                        //map.removeLayer(l);
                        refreshMap(url)}, par.refresh * 1000);
    }
    else
        refreshMap(url);
    
});

function refreshMap(url){
    l = getLayer(url);
    console.log(l)
    map.addLayer(l);
}

