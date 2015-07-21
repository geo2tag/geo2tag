var test_data = {
    'GET' : {url : '/instance/service/testservice'},
    'PUT' : {
        url : '/instance/service/testservice',
        data : {logSize : 10}
    },
    'DELETE' : {url : '/instance/service/testservice'}
};


QUnit.test('GET' + test_data.GET.url, function( assert ) {
    var done = assert.async();

    var callbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };

    var callbackOk = function() {
        assert.ok(true, 'went ok' );
        done();
    };

    $.get(test_data.GET.url)
        .fail( callbackFail )
        .done( callbackOk )
});

QUnit.test('PUT' + test_data.PUT.url + JSON.stringify(test_data.PUT.data), function( assert ) {
    var done = assert.async();

    var callbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };

    var callbackOk = function() {
        assert.ok(true, 'went ok' );
        done();
    };

    $.put = function( url, data) {
        return $.ajax({
            type: 'PUT',
            url: url,
            data : data
        });
    };

    $.put(test_data.PUT.url, test_data.PUT.data)
        .fail( callbackFail )
        .done( callbackOk )
});

QUnit.test('DELETE' + test_data.DELETE.url, function( assert ) {
    var done = assert.async();

    var callbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };

    var callbackOk = function() {
        assert.ok(true, 'went ok' );
        done();
    };

    $.delete = function( url) {
        return $.ajax({
            type: 'DELETE',
            url: url
        });
    };

    $.delete(test_data.DELETE.url)
        .fail( callbackFail )
        .done( callbackOk )
});