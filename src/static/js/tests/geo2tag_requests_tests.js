QUnit.test( 'Get channels test',
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

    	var test = new Geo2TagRequests('test', 'test');
    	test.getChannels('testservice', callbackSuccess, callbackFail);
    }); 

QUnit.test( 'Get points test',
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
    	var test = new Geo2TagRequests('test', 'test');
        var channel_ids_list = ["556721a52a2e7febd2744201","556721a52a2e7febd2744202"];
    	test.getPoints('testservice', callbackSuccess, callbackFail, channel_ids_list, 5);
    }); 