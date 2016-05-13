QUnit.test('Test make url by channel_ids', function(assert) {
	var done = assert.async();
	var SERVICE_NAME = 'serviceName';
	var CHANNEL_IDS = 'channel_ids';
	var NUMBER = 'number';
	var TEST_CHANNEL = 'test123';
	var TEST_CHANNEL_IDS = '1';
	var TEST_NUMBER_POINTS = 1000;
	var par = {};
	par[SERVICE_NAME] = TEST_CHANNEL;
	par[CHANNEL_IDS] = TEST_CHANNEL_IDS;
	par[NUMBER] = TEST_NUMBER_POINTS;
	var test_result = "/instance/service/test123/point?number=1000&channel_ids=1&lat1={lat1}&lat2={lat2}&lon1={lon1}&lon2={lon2}";
	var url = MakeUrlForChannelId(par, TEST_CHANNEL_IDS);
	assert.equal(url,test_result);
	done();
});
