var map = null, proj4326 = null, projmerc = null, markers = null, vectorLayer = null, 
    controls = null, positionMarker=null;

function getRadius(){
  var km = $( "#SliderSingle" ).attr("value")*1000;
  console.log('Radius == '+km);
  return km;
}


function setupMap(){
    var urlPar = getUrlVars();
    if (urlPar['latitude'] != undefined && urlPar['longitude'] != undefined) {
        latitude = urlPar['latitude'];
        longitude = urlPar['longitude'];
    }
    map = createMap('map', latitude, longitude);
}


function refreshRubrikAndClassFilter(objectsToDraw){
    var filters = $('input[type=checkbox]');
    var rubriks = [];
    for (var i = 0; i < filters.length; i++){
        var filter = filters[i];
        if ($(filter).prop('checked') == true){
            var rubrik = $(filter).attr('rubrik');
            rubriks.push(rubrik);
            console.log(rubrik);
        }
    }
    var className = $('#classSelector').val();
    console.log(className + '\nclassName');
    drawMarkersForRubriksAndClass(rubriks, className, objectsToDraw);

}

function drawMarkersForRubriksAndClass(rubriks, className, objectsToDraw){
    var filteredObjects = [];
    if (positionMarker != null)
        addPositionMarker(latitude, longitude);
    for (var i=0; i < objectsToDraw.length; i++){
        var object = objectsToDraw[i];
        if ('rubrik' in object && 
            $.inArray(object.rubrik, rubriks) > -1 &&
            'class' in object && 
            (className == '' || object['class'] == className)){

            filteredObjects.push(object);
        }
            
    }
    createMarkersForMap(map, filteredObjects); 
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
    $('input[type=checkbox]').change(function(){
        refreshRubrikAndClassFilter(objects);
    });
    $('#classSelector').on('change', function(){
        refreshRubrikAndClassFilter(objects);
    });

    $(window).on('resize', fixMapSize());

    $("[data-toggle='buttons'] .btn").each(function(i, el) {
        var $button = $(el);
        $button.addClass("active");
    });

});
