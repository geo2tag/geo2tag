QUnit.test('Test make url by channel_ids', function(assert) {
	var done = assert.async();
	var TEST_CHANNEL = 'test123';
	var TEST_CHANNEL_IDS = ["1","2","3"];
	var test_result = "/instance/service/test123/point?number=1000&channel_ids=1&channel_ids=2&channel_ids=3&lat1={lat1}&lat2={lat2}&lon1={lon1}&lon2={lon2}";
	var url = MakeUrlByChannelIds(TEST_CHANNEL,TEST_CHANNEL_IDS,1000);
	assert.equal(url,test_result);
	done();
});