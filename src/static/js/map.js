var map = null, proj4326 = null, projmerc = null, markers = null, vectorLayer = null, 
    controls = null, positionMarker=null;

function setupMap(){
    var urlPar = getUrlVars();
    if (urlPar['latitude'] != undefined && urlPar['longitude'] != undefined) {
        latitude = urlPar['latitude'];
        longitude = urlPar['longitude'];
    }
    map = createMap('map', latitude, longitude);
}

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
    setupMap();
    
    $(window).on('resize', fixMapSize());

    $("[data-toggle='buttons'] .btn").each(function(i, el) {
        var $button = $(el);
        $button.addClass("active");
    });

});
