var test_data_point_resource = {
    'GET':{
        url : '/instance/service/testservice/point/55282f3b5c0dd1178d37f7a6'
    },
    'PUT':{
        data: {'alt': 5},
        url : '/instance/service/testservice/point/55282f3b5c0dd1178d37f7a6'
    },
   'POST':{
        data:{'lat':1.1, 'lon':1.1,  'alt':1.1,  'json':{'a':'b'}, 'channel_id':'556721a521217f1bd2744202'},
        url : '/instance/service/testservice/point'
    },
    'FIND':{
        data:{'number':1,'channel_ids':'556721a521217f1bd2744202'},
        url : '/instance/service/testservice/point'
    },
   'DELETE':{
        url : '/instance/service/testservice/point/556721a521217f1bd2744202'
    }
};

QUnit.test( 'PUT ' + test_data_point_resource.PUT.url + JSON.stringify(test_data_point_resource.PUT.data), function( assert ) {
    var done = assert.async();
    var putCallbackFail = function() {
        assert.ok(false, 'Point resource put failed' );
        done();
    };
    var putCallbackSuccess = function() {
        assert.ok(true, 'Point resource put success' );
        done();
    };
    $.put(test_data_point_resource.PUT.url, test_data_point_resource.PUT.data )
        .fail(putCallbackFail).done(putCallbackSuccess);
});

QUnit.test( 'GET ' + test_data_point_resource.GET.url, function( assert ) {
    var done = assert.async();
    var getCallbackFail = function() {
        assert.ok(false, 'Point resource get failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'Point resource get success' );
        done();
    };
    $.get(test_data_point_resource.GET.url, test_data_point_resource.GET.data )
        .fail(getCallbackFail).done(getCallbackSuccess);
});

QUnit.test( 'POST ' + test_data_point_resource.POST.url + JSON.stringify(test_data_point_resource.POST.data), function( assert ) {
    var done = assert.async();
    var postCallbackFail = function() {
        assert.ok(false, 'POST failed' );
        done();
    };
    var postCallbackSuccess = function(data) {
        assert.ok(true, data );
        done();
    };
    $.post(test_data_point_resource.POST.url,JSON.stringify([test_data_point_resource.POST.data]))
        .done(postCallbackSuccess).fail(postCallbackFail);
});

QUnit.test( 'GET ' + test_data_point_resource.FIND.url + JSON.stringify(test_data_point_resource.FIND.data), function( assert ) {
    var done = assert.async();
    var getCallbackFail = function() {
        assert.ok(false, 'GET failed' );
        done();
    };
    var getCallbackSuccess = function(data,a,b) {
        assert.ok(true, data );
        done();
    };
    $.get(test_data_point_resource.FIND.url, test_data_point_resource.FIND.data )
        .fail(getCallbackFail).done(getCallbackSuccess).error(function(xhr, error, statusText){
        assert.ok(false,statusText);
       });

});

QUnit.test( 'DELETE ' + test_data_point_resource.DELETE.url, function( assert ) {
    var done = assert.async();
    
    var deleteCallbackFail = function() {
        assert.ok(false, 'Point resource delete failed' );
        done();
    };
    var deleteCallbackSuccess = function() {
        assert.ok(true, 'Point resource delete success' );
        done();
    };
    $.delete(test_data_point_resource.DELETE.url)
        .fail(deleteCallbackFail).done(deleteCallbackSuccess).error(function(a,b,c){
assert.ok(false, c);
});
});


