var map = null, proj4326 = null, projmerc = null, markers = null, vectorLayer = null, 
    controls = null, positionMarker=null, l=null;
var CHANNEL_IDS = 'channel_ids';

$(document).ready(function (){
    var overlayMaps = getOverlayMaps();
    if(par.latitude != null && par.longitude != null)
        map = createMap('map', false, par.zoom, overlayMaps, par.latitude, par.longitude);
    else
        map = createMap('map', true, par.zoom, overlayMaps)
    changeCheckboxListener();
    $(window).on('resize', fixMapSize());
    if(par.refresh != 0){
        setInterval(function() {
               refreshMap(url)}, par.refresh * 1000);
    }
});

