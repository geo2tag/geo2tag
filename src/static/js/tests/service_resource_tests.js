var test_data_service_resource = {
    'GET' : {url : '/' + getInstancePrefix() + '/service/testservice'},
    'PUT' : {
        url : '/' + getInstancePrefix() + '/service/testservice',
        data : {logSize : 10}
    },
    'DELETE' : {url : '/' + getInstancePrefix() + '/service/serviceToDelete'}
};

var serviceToDelete = {
        url : '/' + getInstancePrefix() + '/service',
        data : {
            'name' : 'serviceToDelete',
            'ownerId' : 'serviceListResourceTestOwnerId',
            'logSize' : 10
        }
    }

QUnit.test('GET' + test_data_service_resource.GET.url, function( assert ) {
    var done = assert.async();

    var callbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };

    var callbackOk = function() {
        assert.ok(true, 'went ok' );
        done();
    };

    $.get(test_data_service_resource.GET.url)
        .fail( callbackFail )
        .done( callbackOk )
});

QUnit.test('PUT' + test_data_service_resource.PUT.url + JSON.stringify(test_data_service_resource.PUT.data), function( assert ) {
    var done = assert.async();

    var callbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };

    var callbackOk = function() {
        assert.ok(true, 'went ok' );
        done();
    };

    $.put = function( url, data ) {
        return $.ajax({
            type: 'PUT',
            url: url,
            data : data
        });
    };

    $.put( test_data_service_resource.PUT.url, test_data_service_resource.PUT.data )
        .fail( callbackFail )
        .done( callbackOk )
});

QUnit.test('DELETE' + test_data_service_resource.DELETE.url, function( assert ) {
    var done = assert.async();


    $.post(serviceToDelete.url, serviceToDelete.data)
    .done(function(){

        var callbackFail = function() {
            assert.ok( false, 'get failed' );
            done();
        };

        var callbackOk = function() {
            assert.ok( true, 'went ok' );
            done();
        };

        $.delete = function( url ) {
            return $.ajax({
                type : 'DELETE',
                url : url
            });
        };

        $.delete( test_data_service_resource.DELETE.url )
        .fail( callbackFail )
        .done( callbackOk );

    })
    .fail(function(){
        assert.ok(false, 'Post of serviceToDelete failed' );
        done();    
    });
    
});
