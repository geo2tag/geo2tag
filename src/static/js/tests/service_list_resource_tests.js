var test_data_service_list_resource = {
    'GET' : {
        url : getUrlWithPrefix('/service'),
        data : {
            'number' : 0,
            'offset' : 0
        }
    },
    'POST' : {
        url : getUrlWithPrefix('/service'),
        data : {
            'name' : 'serviceListResourceTestName',
            'ownerId' : 'serviceListResourceTestOwnerId',
            'logSize' : 10
        }
    }
};

QUnit.test( 'GET' + test_data_service_list_resource.GET.url + JSON.stringify(test_data_service_list_resource.GET.data), function( assert ) {
    var done = assert.async();

    var callbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };

    var callbackOk = function() {
        assert.ok(true, 'went ok' );
        done();
    };

    $.get(test_data_service_list_resource.GET.url, test_data_service_list_resource.GET.data)
        .fail( callbackFail )
        .done( callbackOk )
});

QUnit.test( 'POST' + test_data_service_list_resource.POST.url + JSON.stringify(test_data_service_list_resource.POST.data), function( assert ) {
    var done = assert.async();

    var callbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };

    var callbackOk = function() {
        $.delete( test_data_service_list_resource.POST.url +'/'+ test_data_service_list_resource.POST.data.name);
        assert.ok(true, 'went ok' );
        done();
    };

    $.post(test_data_service_list_resource.POST.url, test_data_service_list_resource.POST.data)
        .fail( callbackFail )
        .done( callbackOk )
});