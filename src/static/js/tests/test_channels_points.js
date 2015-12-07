QUnit.test('test channels points ', function( assert ) {
    var done = assert.async();
    function callBack(countPoints, countChannels){
      assert.ok(countPoints != 0);
      assert.ok(countChannels != 0);
      done();
    }
    var countPoints = 0, countChannels = 0;
    queryChannelsAndPoints(callBack, countChannels, countPoints, 'testservice');
});
