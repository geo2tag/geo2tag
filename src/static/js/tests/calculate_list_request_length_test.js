QUnit.test('removeNumberOffsetParameters', function(assert) {
    var validUrl = '/url/?test=11';

    var checkUrls = ['/url/?number=111&test=11&offset=e44', 
                     '/url/?number=111&offset=e44&test=11',
                     '/url/?test=11&offset=e44&number=111'];

    for (var i = 0; i < checkUrls.length; i++){
         assert.equal(removeNumberOffsetParameters(checkUrls[i]), validUrl);
    }
});

QUnit.test('calculateListRequestLength', function(assert) {
    var done = assert.async()
    var callbackFail = function() {
        assert.ok(false, ' get failed')
        done()
    }
    var callbackSuccess = function(length) {
        assert.ok(true, ' went ok')
        assert.notEqual(length, undefined);
        done()
    }

    var VALID_URL = '/instance/service';

    calculateListRequestLength(VALID_URL, callbackSuccess, callbackFail); 

});
