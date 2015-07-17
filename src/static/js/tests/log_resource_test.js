var log_resource_test_data = { 'GET':{
        url : '/instance/log'
    } ,
};
  
var log_resource_serviceName_test_data = { 'GET':{
        url : '/instance/service/test_service_name/log'
    } ,
};

QUnit.test( log_resource_serviceName_test_data.GET.url, function( assert ) {
    var done = assert.async(); 
    var callbackFail = function() {
        assert.ok(false,' get failed' );
        done();
    };
    var callbackOk = function() {
        assert.ok(true, ' went ok' );
        done();
    };

    $.get(log_resource_serviceName_test_data.GET.url)
        .fail( callbackFail )
        .done( callbackOk )

});

QUnit.test( log_resource_test_data.GET.url, function( assert ) {
    var done = assert.async(); 
    var callbackFail = function() {
        assert.ok(false, ' get failed' );
        done();
    };
    var callbackOk = function() {
        assert.ok(true, ' went ok' );
        done();
    };

    $.get(log_resource_test_data.GET.url)
        .fail( callbackFail )
        .done( callbackOk )
});


