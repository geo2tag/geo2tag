var log_resource_test_data = { 'GET':{
        url : getUrlWithPrefix('/log')
    } 
};
  
var log_resource_serviceName_test_data = { 'GET':{
        url : getUrlWithPrefix('/service/test_service_name/log')
    } 
};

var data = {
    'number' : 1,
    'offset' : 1,
    'date_from' : '1983-01-22T08:00:00',
    'date_to' : '2014-01-22T08:00:00'
}

QUnit.test('GET ' + log_resource_serviceName_test_data.GET.url + JSON.stringify(data), function( assert ) {
    var done = assert.async(); 
    var callbackFail = function() {
        assert.ok(false,' get failed' );
        done();
    };
    var callbackOk = function() {
        assert.ok(true, ' went ok' );
        done();
    };

    $.get(log_resource_serviceName_test_data.GET.url, data)
        .fail( callbackFail )
        .done( callbackOk )

});

QUnit.test( 'GET ' + log_resource_test_data.GET.url + JSON.stringify(data), function( assert ) {
    var done = assert.async(); 
    var callbackFail = function() {
        assert.ok(false, ' get failed' );
        done();
    };
    var callbackOk = function() {
        assert.ok(true, ' went ok' );
        done();
    };

    $.get(log_resource_test_data.GET.url, data)
        .fail( callbackFail )
        .done( callbackOk )
});


