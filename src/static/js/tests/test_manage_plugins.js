var test_data_plugins_resource = {
    'GET':{
        url : getUrlWithPrefix('/manage_plugins?test_plugin=True&testPlugin1=False')
    }
}
QUnit.test( 'GET ' + test_data_plugins_resource.GET.url, function( assert ) {
    var done = assert.async();
    var getCallbackFail = function() {
        assert.ok(false, 'Manage plugins get failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'Manage plugins get success' );
        done();
    };
    $.get(test_data_plugins_resource.GET.url)
        .fail(getCallbackFail).done(getCallbackSuccess);
});