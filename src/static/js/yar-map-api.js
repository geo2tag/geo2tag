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
/**
# Invalidates map size when map tab is opened
*/
invalidateMapSizeWhenVisible = function(map) {
    return setTimeout(invalidateMapSizeWhenVisible, 300, map);
};


createMap = function(elementId, locate, zoom, channel_layers, lat, lon) {
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
  map.invalidateSize();
  layers = {
    'Яндекс': new L.Yandex(),
    'Google карта': new L.Google('ROADMAP'),
    'Google гибрид': new L.Google('HYBRID'),
    'Google спутник': new L.Google(),
    'Open street maps': new L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png')
  };
  var overlayMaps = {};
  console.log(channel_layers)
  for(var i = 0; i < channel_layers.length; i++){
      overlayMaps[channel_layers[i]] = new L.Google('ROADMAP')
  }
  console.log(overlayMaps)
  map.addControl(new L.Control.Layers(layers, overlayMaps));
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
