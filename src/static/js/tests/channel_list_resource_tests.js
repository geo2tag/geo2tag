var channel_list_resource_tests = {
    'GET':{
        data:{'number':2,'offset':1},
        url : '/instance/service/testservice/channel'
    },
    'POST':{
        data:{'name': 'tes t_name', 'json': "{'1': 2, '2': '4'}"},
        url : '/instance/service/testservice/channel'
    }
};
QUnit.test( 'GET ' + channel_list_resource_tests.GET.url + JSON.stringify(channel_list_resource_tests.GET.data), function( assert ) {
    var done = assert.async(); 
    var getCallbackFail = function() {
        assert.ok(false, 'GET failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'GET success' );
        done();
    };
    $.get(channel_list_resource_tests.GET.url, channel_list_resource_tests.GET.data )
        .fail(getCallbackFail).done(getCallbackSuccess);
 
});
QUnit.test( 'POST ' + channel_list_resource_tests.POST.url + JSON.stringify(channel_list_resource_tests.POST.data), function( assert ) {
    var done = assert.async(); 
    var getCallbackFail = function() {
        assert.ok(false, 'POST failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'POST success' );
        done();
    };
    $.post(channel_list_resource_tests.POST.url, channel_list_resource_tests.POST.data )
        .fail(getCallbackFail).done(getCallbackSuccess);
 
});

