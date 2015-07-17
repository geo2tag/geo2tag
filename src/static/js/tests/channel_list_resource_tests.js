var channel_list_resource_tests = {
    'GET':{
        url : '/instance/service/testservice/channel'
    }
};
QUnit.test( channel_list_resource_tests.GET.url, function( assert ) {
    var done = assert.async(); 
    var getCallbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'get success' );
        done();
    };
    $.get(channel_list_resource_tests.GET.url, channel_list_resource_tests.GET.data )
        .fail(getCallbackFail).done(getCallbackSuccess);
 
});
