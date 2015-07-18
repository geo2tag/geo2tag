var test_data_debug = {
    'GET':{
        url : '/instance/service/testservice/channel/558807a47ec8ff5da755ee49'
    },
    'PUT':{
        data: {'name': 'test_channel_GT-1389_2'},
        url : '/instance/service/testservice/channel/558807a47ec8ff5da755ee49'
    },
    'DELETE':{
        url : '/instance/service/testservice/channel/558807a47ec8ff5da755ee49'
    }
};

QUnit.test( 'PUT' + test_data_debug.PUT.url + JSON.stringify(test_data_debug.PUT.data),
    function( assert ) { 
    var done = assert.async();
    var putCallbackFail = function() {
        assert.ok(false, 'ChannelResource put failed' );
        done();
    }; 
    var putCallbackSuccess = function() {
        assert.ok(true, 'ChannelResource put success' );
        done();
    };
    $.put(test_data_debug.PUT.url, test_data_debug.PUT.data )
        .fail(putCallbackFail).done(putCallbackSuccess);
    });

QUnit.test('GET' + test_data_debug.GET.url, function( assert ) {
    var done = assert.async();
    var getCallbackFail = function() {
        assert.ok(false, 'ChannelResource get failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'ChannelResource get success' );
        done();
    };
    $.get(test_data_debug.GET.url, test_data_debug.GET.data )
        .fail(getCallbackFail).done(getCallbackSuccess);
 
});

QUnit.test('DELETE' + test_data_debug.DELETE.url, function( assert ) {
    var done = assert.async();
    
    var deleteCallbackFail = function() {
        assert.ok(false, 'ChannelResource delete failed' );
        done();
    };
    var deleteCallbackSuccess = function() {
        assert.ok(true, 'ChannelResource delete success' );
        done();
    };
    $.delete(test_data_debug.DELETE.url)
        .fail(deleteCallbackFail).done(deleteCallbackSuccess);
});