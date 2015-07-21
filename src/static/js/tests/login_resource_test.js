var test_data_login = { 'GET':{
        url : '/instance/login'
    } ,
};
  

QUnit.test( test_data_login.GET.url, function( assert ) {
    var done = assert.async(); 
    var callbackFail = function() {
        assert.ok(false, 'get failed' );
        done();
    };
    var callbackOk = function() {
        assert.ok(true, 'went ok' );
        done();
    };

    $.get(test_data_login.GET.url)
        .fail( callbackFail )
        .done( callbackOk )
});
