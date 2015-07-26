var test_data_point_resource = {
    'GET':{
        url : '/instance/service/testservice/point/55282f3b5c0dd1178d37f7a6'
    },
    'PUT':{
        data: {'alt': 5},
        url : '/instance/service/testservice/point/55282f3b5c0dd1178d37f7a6'
    },
   'DELETE':{
        url : '/instance/service/testservice/point/55282f3b5c0dd1178d37f7a6'
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
        .fail(deleteCallbackFail).done(deleteCallbackSuccess);
});