QUnit.test('Parsing url', function(assert) {
    url = 'http://geomongo/instance/service/testservice/map?longitude=10&lantitude=3'
    par = getArgsQueryForMap(url)
    assert.equal(par['longitude'], 10);
    assert.equal(par['lantitude'], 3);
});
