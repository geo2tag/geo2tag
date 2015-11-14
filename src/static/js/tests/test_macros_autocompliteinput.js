QUnit.test('search autocompliteinput test', function( assert ) {
    var done = assert.async(); 
    var x = new AutocompliteInput('test','22','333');
    assert.equal(x.getExternalValue(),'22');
    assert.equal(x.getInternalValue(),'333');
    x.inputobject.keyup(function(){
        var name = x.getExternalValue();
        var req_url = x.url_request + '?login=' + name + '&number=' + x.countView + '&offset=0'
        $.get( req_url, function( data ) {
            $( x.inputobject ).autocomplete({source: data});
        });
    });
    done();
});