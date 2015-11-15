QUnit.test('search autocompliteinput test', function( assert ) {
    var done = assert.async(); 
    var x = new AutocompliteInput('test','22','333');
    assert.equal(x.getExternalValue(),'22');
    assert.equal(x.getInternalValue(),'333');
    x.inputobject.keyup(function(){
        x.makeAutocompliteToRequest();
    });
    done();
});