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
});
