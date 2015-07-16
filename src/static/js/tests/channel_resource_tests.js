var test_data_debug = {
    'GET':{
        url : '/instance/service/testservice/channel/558807a47ec8ff5da755ee49'
    },
    'PUT':{
        data: {'name': 'test_channel_GT-1290'},
        url : '/instance/service/testservice/channel/558807a47ec8ff5da755ee49'
    },
    'DELETE':{
        url : '/instance/service/testservice/channel/558807a47ec8ff5da755ee49'
    }
};
$.put = function(url, data, callback, type){
 
  if ( $.isFunction(data) ){
    type = type || callback,
    callback = data,
    data = {}
  }
 
  return $.ajax({
    url: url,
    type: 'PUT',
    success: callback,
    data: data,
    contentType: type
  });
}
$.delete = function(url, data, callback, type){
 
  if ( $.isFunction(data) ){
    type = type || callback,
        callback = data,
        data = {}
  }
 
  return $.ajax({
    url: url,
    type: 'DELETE',
    success: callback,
    data: data,
    contentType: type
  });
}

QUnit.test( test_data_debug.PUT.url + JSON.stringify(test_data_debug.PUT.data),
    function( assert ) { 
    var done = assert.async(); // Код необходим для того, чтобы делать в проверки в коллбэке
    var putCallbackFail = function() {
        assert.ok(false, 'put failed' );
        done();
    }; 
    var putCallbackSuccess = function() {
        assert.ok(true, 'put success' );
        done();
    };
    $.put(test_data_debug.PUT.url, test_data_debug.PUT.data )
        .fail(putCallbackFail).done(putCallbackSuccess);
    });

QUnit.test( test_data_debug.GET.url, function( assert ) {
    var done = assert.async(); // Код необходим для того, чтобы делать в проверки в коллбэке
    var getCallbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'get success' );
        done();
    };
    $.get(test_data_debug.GET.url, test_data_debug.GET.data )
        .fail(getCallbackFail).done(getCallbackSuccess);
 
});
  
// Запрос, требующий предварительной подготовки
QUnit.test( test_data_debug.DELETE.url, function( assert ) {
    var done = assert.async();
    
    var deleteCallbackFail = function() {
        // Подготовка данных не удалась - валим assert
        assert.ok(false, 'delete failed' );
        done();
    };
    var deleteCallbackSuccess = function() {
        assert.ok(true, 'delete success' );
        done();
    };
    $.delete(test_data_debug.DELETE.url)
        .fail(deleteCallbackFail).done(deleteCallbackSuccess);
});