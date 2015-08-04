QUnit.test( 'Get channels test',
    function( assert ) {
    	var done = assert.async();
    	var testCallback = function (date) {
    		assert.ok(true);
    	};

    	var test = new Geo2TagRequests('test', 'test');
    	test.getChannels('testservice', testCallback);
    }); 