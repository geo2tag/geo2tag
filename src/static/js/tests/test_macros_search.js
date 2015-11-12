QUnit.test('search macros test', function( assert ) {
    var done = assert.async(); 
    var searchId = 'search', value = 'new value', changeValue = 'change value';
    var search = new Search('search');
    assert.equal(searchId, search.macroId);
    search.setValue(value);
    assert.equal(search.getValue(), value);
    search.clear();
    assert.equal(search.getValue(), '');
    function myChange() {
        search.setValue(changeValue);
    }
    search.change(myChange);
    //assert.equal(search.getValue(), changeValue);
    done();
});