var map;
var markerLayer = undefined;
var positionLayer = undefined;
var cookies, createMap, invalidateMapSizeWhenVisible;
var __indexOf = Array.prototype.indexOf || function(item) {
  for (var i = 0, l = this.length; i < l; i++) {
    if (this[i] === item) return i;
  }
  return -1;
};
cookies = window.NM.cookies;

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

function getOverlayMaps(){
    var overlayMaps = {};
    for(var i = 0; i < par[CHANNEL_IDS].length; i++){
        var channel_id = par[CHANNEL_IDS][i];
        var logo_channel_id = "<img src = '/instance/service/testservice/get_icon?channel_id="  +  channel_id + "'/>" + channel_id ;
        var url = MakeUrlForChannelId(par, channel_id);
        overlayMaps[logo_channel_id] = getLayerForChannelId(channel_id, url);
    }
    return overlayMaps;
}

function setOverlayMaps(control){
    for(var i = 0; i < par[CHANNEL_IDS].length; i++){
        var channel_id = par[CHANNEL_IDS][i];
        var url = MakeUrlForChannelId(par, channel_id);
        control.addOverlay(getLayerForChannelId(channel_id, url), channel_id);
    }
    return control;
}

function redrawOverlayMaps(overlayMaps){
    for(var layer_name in overlayMaps){
        console.log(overlayMaps[layer_name])
        overlayMaps[layer_name]._layers.redraw();
    }
}

/**
# Invalidates map size when map tab is opened
*/

invalidateMapSizeWhenVisible = function(map) {
    return setTimeout(invalidateMapSizeWhenVisible, 300, map);
};


createMap = function(elementId, locate, zoom, overlayMaps, lat, lon) {
  var layers, mapType;
  if (elementId == null) {
    elementId = 'map';
  }
  if (lat == undefined || lon == undefined) {
    lat = 63.377;
    lon = 28.938 ;
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
  addNewControlToMap(layers, overlayMaps);
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
