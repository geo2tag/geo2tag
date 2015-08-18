var test_rout_map_resource = {
    'GET' : {url : getUrlWithPrefix('/service/testservice/map')}
};

QUnit.test('GET' + test_rout_map_resource.GET.url, function( assert ) {
    var done = assert.async();

    var callbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };

    var callbackOk = function() {
        assert.ok(true, 'went ok' );
        done();
    };

    $.get(test_rout_map_resource.GET.url)
        .fail( callbackFail )
        .done( callbackOk )
});
