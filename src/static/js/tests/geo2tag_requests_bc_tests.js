QUnit.test( 'Get points test bc format',
    function( assert ) {
    	var done = assert.async();
    	var callbackSuccess = function (data) {
            assert.ok(true);
    	    done();
    	};
    	var callbackFail = function () {
    	    assert.ok(false);
    	    done();
    	};
    	var testgetPointsBC = new Geo2TagRequests('test', 'test');
        var channel_ids_list = ["556721a52a2e7febd2744201","556721a52a2e7febd2744202"];
    	testgetPointsBC.getPoints('testservice', callbackSuccess, callbackFail, channel_ids_list, 100,'{"coordinates": [-115.8, 37.2], "type": "Point"}',0,0,0,'2015-09-10T23:32:17.000000','2015-09-11T23:32:17.000000',0,0,'true','true');
}); 
