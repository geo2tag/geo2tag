var map = null, proj4326 = null, projmerc = null, markers = null, vectorLayer = null, 
    controls = null, positionMarker=null, l=null;
var CHANNEL_IDS = 'channel_ids';

$(document).ready(function (){
    if(!par.clustering){
        var overlayMaps = getOverlayMaps();
        map = createMap('map', false, par.zoom, overlayMaps, par.latitude, par.longitude, par.clustering);
    }
    else
        map = createMap('map', false, par.zoom, undefined, par.latitude, par.longitude, par.clustering);    
    $(window).on('resize', fixMapSize());
    console.log(par)
    if(par.refresh != 0){
        if(!par.clustering)
            setInterval(function() {
                refreshMapWithoutClustering()}, par.refresh * 1000);
        else
            setInterval(function() {
                refreshMapWithClustering()}, par.refresh * 1000);
    }
});

