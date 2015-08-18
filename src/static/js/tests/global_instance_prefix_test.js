var global_instance_prefix_data = {
        url : '/' + getInstancePrefix() + '/login',
        INSTANCE_PREFIX : 'instance'
};
QUnit.test( 'getInstancePrefix()' + global_instance_prefix_data.url, function( assert ) {
    var done = assert.async();

    var getCallbackFail = function() {
        assert.ok(
            typeof getInstancePrefix !== 'undefined' &&
            typeof getInstancePrefix === 'function' &&
            getInstancePrefix() == global_instance_prefix_data.INSTANCE_PREFIX,
            'Function don\'t exist or failed'
            );
        done();
    };

    var getCallbackSuccess = function() {
        assert.ok(
            typeof getInstancePrefix !== 'undefined' &&
            typeof getInstancePrefix === 'function' &&
            getInstancePrefix() == global_instance_prefix_data.INSTANCE_PREFIX,
            'Function exists and succeeded'
            );
        done();
    };

    $.get(global_instance_prefix_data.url)
        .fail(getCallbackFail).done(getCallbackSuccess);
})