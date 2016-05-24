var map;
var markerLayer = undefined;
var positionLayer = undefined;
var cookies, createMap, invalidateMapSizeWhenVisible;
var list_checked_layers = [];
var __indexOf = Array.prototype.indexOf || function(item) {
  for (var i = 0, l = this.length; i < l; i++) {
    if (this[i] === item) return i;
  }
  return -1;
};
var LOCATION = 'location';
var COORDINATES = 'coordinates'

cookies = window.NM.cookies;

function getMapIcon(channel_id){
    return "get_icon?channel_id=" + channel_id;
}

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

function setLayerWithCluster(){
    var getPointForMap = new Geo2TagRequests('map', 'map');
    var callbackSuccess = function (data) {
        var data_len = data.length;
        markers = new L.MarkerClusterGroup();
        for(var i = 0; i < data_len; i++){
            var mapIcon = L.icon({
                iconUrl: getMapIcon(data[i]['channel_id']['$oid'])});
            markers.addLayer(L.marker([
                data[i][LOCATION][COORDINATES][0],
                data[i][LOCATION][COORDINATES][1]],
                {icon: mapIcon}));
        }
        map.addLayer(markers);
        map['markers'] = markers;
        console.log('success set layer with cluster')
    };
    var callbackFail = function () {
        console.log('fail set layer with cluster')
    };
    getPointForMap.getPoints(par.serviceName, callbackSuccess, callbackFail, par.channel_ids, 1000);
}


function changeCheckboxListener(){
    $('input.leaflet-control-layers-selector').change(function() {
         var child_nodes_layer = $(this).parent()[0].childNodes[1];
         var child_nodes_span = $(child_nodes_layer)[0].childNodes[1];
         var channel_id = $(child_nodes_span)[0]['attributes']['id']['value'];
         if(this.checked){
             var flag = false;
             for(var i = 0; i < list_checked_layers.length; i++){
                 if(list_checked_layers[i] == channel_id){
                     flag = true;
                     break;
                 }
             }
             if(!flag)
                 list_checked_layers.push(channel_id);
         }
         else {
             for(var i = 0; i < list_checked_layers.length; i++){
                 if(list_checked_layers[i] == channel_id){
                     list_checked_layers.splice(i, 1);
                     break;
                 }
             }
         }
    });
}

function checkCheckboxOnControl(){
    for(var i = 0; i < list_checked_layers.length; i++){
        $('input.leaflet-control-layers-selector').each(function(){
            var span = $(this).parent()[0].childNodes[1].childNodes[1];
            if($(span)[0]){
                var id = $(span)[0]['id'];
                if(id == list_checked_layers[i])
                    $(this).trigger('click');
            }
        });
    }
}

function checkAllCheckBoxes(){
    $('input.leaflet-control-layers-selector').each(function(){
        var span = $(this).parent()[0].childNodes[1].childNodes[1];
            if($(span)[0]){
                $(this).trigger('click');
            }
    });
}

function deleteClusterFromMap(){
    map['markers'].clearLayers();
}

function deleteOverlayMap(){
    for(var key in map['control']._layers){
        if(map['control']._layers[key].overlay){
            map['control'].removeLayer(map['control']._layers[key].layer)
       }
    }
    map.eachLayer(function(l){
        if(l._hashUrl)
            map.removeLayer(l);
    });
}

function refreshMapWithClustering(){
    deleteClusterFromMap();
    setLayerWithCluster();
}

function refreshMapWithoutClustering(){
    deleteOverlayMap();
    map['control'] = setOverlayMaps(map['control']);
    checkCheckboxOnControl();
    changeCheckboxListener();
}

function getLayerForChannelId(channel_id, url){
    var layer = new L.LayerJSON({url: url,
         propertyLoc: ['location.coordinates.0','location.coordinates.1'],
         buildPopup: function(data) {
             return data.json.name || null;
         },
         buildIcon: function(data, title) {
             return new L.Icon({
                 iconUrl : getMapIcon(channel_id)
             });
         }
    });
    return layer;
}

function addNewControlToMap(layers, overlayMaps){
    var control = new L.Control.Layers(layers, overlayMaps)
    map.addControl(control);
    map['control'] = control;
}

function getLayers(){
    var layers = {
        'Яндекс': new L.Yandex(),
        'Google карта': new L.Google('ROADMAP'),
        'Google гибрид': new L.Google('HYBRID'),
        'Google спутник': new L.Google(),
        'Open street maps': new L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png')
    };
    return layers;
}

function getLogoChannelId(channel_id){
    return "<img src = '/instance/service/testservice/get_icon?channel_id="  +  channel_id + "' id='" + channel_id + "'/>" + channel_id;
}

function getOverlayMaps(){
    var overlayMaps = {};
    for(var i = 0; i < par[CHANNEL_IDS].length; i++){
        var channel_id = par[CHANNEL_IDS][i];
        var logo_channel_id = getLogoChannelId(channel_id);
        var url = MakeUrlForChannelId(par, channel_id);
        overlayMaps[logo_channel_id] = getLayerForChannelId(channel_id, url);
    }
    return overlayMaps;
}

function setOverlayMaps(control){
    for(var i = 0; i < par[CHANNEL_IDS].length; i++){
        var channel_id = par[CHANNEL_IDS][i];
        var url = MakeUrlForChannelId(par, channel_id);
        control.addOverlay(getLayerForChannelId(channel_id, url), getLogoChannelId(channel_id));
    }
    return control;
}

/**
# Invalidates map size when map tab is opened
*/

invalidateMapSizeWhenVisible = function(map) {
    return setTimeout(invalidateMapSizeWhenVisible, 300, map);
};


createMap = function(elementId, locate, zoom, overlayMaps, lat, lon, clustering) {
  var layers, mapType;
  if (elementId == null) {
    elementId = 'map';
  }
  map = L.map(elementId, {
    center: [lat, lon],
    zoom: zoom
  });
  if (locate == true){
      function onLocationFound(e) {
          map.panTo(e.latlng);
      }

      function onLocationError(e) {
          console.log(e.message);
      }

      map.on('locationfound', onLocationFound);
      map.on('locationerror', onLocationError);
      map.locate({setView: true, maxZoom: 18});
  }
  var layers = getLayers();
  map.invalidateSize();
  if(!clustering){
      console.log('---------------------')
      addNewControlToMap(layers, overlayMaps);
      changeCheckboxListener();
      checkAllCheckBoxes();
  }
  else{
      console.log('Clustering is turned on');
      map.addControl(new L.Control.Layers(layers));
      setLayerWithCluster();
  }
  mapType = cookies.readCookie('maptype');
  if (mapType === void 0 || layers[mapType] === void 0) {
    cookies.createCookie('maptype', 'Яндекс');
    if(cookies.readCookie('maptype') == ''){
        map.addLayer(layers['Яндекс'])
    }
  }
  if(cookies.readCookie('maptype') == 'Яндекс' || cookies.readCookie('maptype') == 'Google карта' || cookies.readCookie('maptype') == 'Google гибрид' ||  cookies.readCookie('maptype') == 'Google спутник' || cookies.readCookie('maptype') == 'Open street maps') {
     console.log("maptype = " + cookies.readCookie('maptype'))
     map.addLayer(layers[cookies.readCookie('maptype')]);
  }
  else
     map.addLayer(layers['Яндекс']);
  return map;
};

window.NM.maps = {
  createMap: createMap,
  invalidateMapSizeWhenVisible: invalidateMapSizeWhenVisible
};
