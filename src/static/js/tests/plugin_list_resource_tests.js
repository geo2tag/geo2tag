var test_data_plugin_list_resource = {
    'GET':{
        url : '/' + getInstancePrefix() + '/plugin'
    }
};

QUnit.test( 'GET ' + test_data_plugin_list_resource.GET.url, function( assert ) {
    var done = assert.async();
    var getCallbackFail = function() {
        assert.ok(false, 'Get all plugins with status resource get failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'Get all plugins with status resource get success' );
        done();
    };
    $.get(test_data_plugin_list_resource.GET.url, test_data_plugin_list_resource.GET.data )
        .fail(getCallbackFail).done(getCallbackSuccess);
});
