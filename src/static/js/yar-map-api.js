/*
= require leaflet
= require L.Control.Zoomslider
= require Yandex
= require Google
= require modules
= require cookies
*/
var map;
var markerLayer = undefined;
var positionLayer = undefined;
var categories, centerMapOnMarkers, cookies, createMap, createMarkersForMap, createMiniMap, createPopupTemplateForMarker, createSimpleMarkersForMap, disableMiniMapHandlers, embraceMarkers, findCategory, getCategoryName, getColoredIcon, invalidateMapSizeWhenVisible, leafletImages, makeMarker;
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
  if ($('.location-tab').is(':visible')) {
    return map.invalidateSize();
  } else {
    return setTimeout(invalidateMapSizeWhenVisible, 300, map);
  }
};

function getUrlVars()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars[hash[0]] = hash[1];
    }
    return vars;
}


createMap = function(elementId, lat, lon) {
  var layers, mapType;
  if (elementId == null) {
    elementId = 'map';
  }
  if (lat == undefined || lon == undefined) {
    lat = 63.377;
    lon = 28.938 ;
  }
  if (location.search.indexOf('?map') !== -1) {
    $('#objects').hide();
    $('#page-indicators').hide();
    $('#objects-on-map').show();
  }
  $('#objects-on-map').on('refreshMap', function() {
    return map.invalidateSize(false);
  });
  map = L.map(elementId, {
    center: [lat, lon],
    zoom: 12
  });
  function onLocationFound(e) {
      drawPositionMarker(e.latlng.lat, e.latlng.lng, map, true);
      latitude = e.latlng.lat;
      longitude = e.latlng.lng;
  }

  function onLocationError(e) {
      console.log(e.message);
  }

  map.on('locationfound', onLocationFound);
  map.on('locationerror', onLocationError);
  map.locate({setView: true, maxZoom: 18});
  map.invalidateSize();
  layers = {
    'Яндекс': new L.Yandex(),
    'Google карта': new L.Google('ROADMAP'),
    'Google гибрид': new L.Google('HYBRID'),
    'Google спутник': new L.Google(),
    'Open street maps': new L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png')
  };
  map.addControl(new L.Control.Layers(layers));
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

  console.log('CM latitude' + latitude+", longitude" + longitude);

  //createMarkersForMap(map, objects);

  return map;
};




makeMarker = function(markerCoordinates, icon, drag) {
  if (typeof(icon) === 'undefined' )
    var icon = getIconByIndex(0);
  if (drag === undefined)
    drag = true;

  var marker;
  marker = L.marker(markerCoordinates, {draggable:drag});
  marker.setIcon(icon);
  return marker;
};

/**
# Creates html template for marker popup
*/

createSimpleMarkersForMap = function(map, objects) {
  var markerLayer;
  markerLayer = new L.layerGroup();
  objects.forEach(function(object, index) {
    if (object.latitude === void 0 || object.longitude === void 0) {
      return;
    }
    return makeMarker([object.latitude, object.longitude]).addTo(markerLayer);
  });
  return map.addLayer(markerLayer);
};
/**
# Fill specified map with the markers for objects
# @param{Leaflet.Map} map: map to add markers to
# @param{Array} objects: list of objects that should be displayed on the map
*/
createMarkersForMap = function(map, objects) {
  if (markerLayer != undefined)
      map.removeLayer(markerLayer);
  markerLayer = new L.layerGroup();
  objects.forEach(function(object, index) {
    var marker;
    if (object.latitude === void 0 || object.longitude === void 0) {
      return;
    }
    marker = new L.marker([object.latitude, object.longitude]);
    marker.index = index;
    marker.on('click', function() {
      if (marker.getPopup() !== void 0) {
        return function() {
          return marker.openPopup();
        };
      }
      return createPopupTemplateForMarker(object.name[0],  object._id, marker);
    });
    marker.setIcon(getColoredIcon(object.rubrik));
    return marker.addTo(markerLayer);
  });
  return map.addLayer(markerLayer);
};
embraceMarkers = function(map, markersFrame) {
  if ($(map.getContainer()).is(':visible')) {
    return map.fitBounds(markersFrame, {
      padding: [40, 40]
    });
  } else {
    return setTimeout(embraceMarkers, 300, map, markersFrame);
  }
};
/**
# Centers map on markers and binds embraceMarkers event
*/
centerMapOnMarkers = function(map, objects) {
  var index, lat, lon, maxLat, maxLon, minLat, minLon;
  if (location.search.indexOf('latitude') !== -1 || objects.length === 0) {
    return;
  }
  minLat = 90;
  maxLat = -90;
  minLon = 180;
  maxLon = -180;
  for (index in objects) {
    if (objects[index].latitude === void 0 || objects[index].longitude === void 0) {
      continue;
    }
    lat = objects[index].latitude;
    lon = objects[index].longitude;
    if (lat < minLat) {
      minLat = lat;
    }
    if (lat > maxLat) {
      maxLat = lat;
    }
    if (lon < minLon) {
      minLon = lon;
    }
    if (longitude > maxLon) {
      maxLon = lon;
    }
  }
  $(map.getContainer()).on('embraceMarkers', function() {
    return embraceMarkers(map, [[minLat, minLon], [maxLat, maxLon]]);
  });
  if ($(map.getContainer()).is(':visible')) {
    return $(map.getContainer()).trigger('embraceMarkers');
  }
};
/**
# Disables mini map handlers
*/
disableMiniMapHandlers = function(miniMap) {
  miniMap.dragging.disable();
  miniMap.touchZoom.disable();
  miniMap.doubleClickZoom.disable();
  return miniMap.scrollWheelZoom.disable();
};
/**
# Creates mini map to display in the "object on map" block on the sidebar
*/
createMiniMap = function() {
  var map;
  map = L.map('mini-map').setView([55.75222, 37.61556], 10, {
    zoomControl: false
  });
  map.addLayer(new L.Yandex());
  disableMiniMapHandlers(map);
  return map;
};
/**
# Get category name by id
*/
getCategoryName = function(categoryId, scope) {
  var category, name, _i, _len;
  if (scope == null) {
    scope = categories;
  }
  for (_i = 0, _len = scope.length; _i < _len; _i++) {
    category = scope[_i];
    if (category.id === categoryId) {
      return category.name;
    }
    if ((__indexOf.call(scope, 'subcategories') >= 0)) {
      name = getCategoryName(categoryId, scope.subcategories);
      if (name !== '') {
        return name;
      }
    }
  }
  return '';
};
window.NM.maps = {
  createMap: createMap,
  createMarkersForMap: createMarkersForMap,
  createSimpleMarkersForMap: createSimpleMarkersForMap,
  centerMapOnMarkers: centerMapOnMarkers,
  createMiniMap: createMiniMap,
  makeMarker: makeMarker,
  getCategoryName: getCategoryName,
  invalidateMapSizeWhenVisible: invalidateMapSizeWhenVisible
};
