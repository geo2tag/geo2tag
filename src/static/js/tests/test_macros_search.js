function Search(macroId) {
    this.macroId = macroId;
    this.jqueryObject = $('#input_'+macroId);
}
  
Search.prototype.setValue = function (value){
    this.jqueryObject.val(value);   
}
  
Search.prototype.getValue = function (value){
    return this.jqueryObject.val();
}
  
Search.prototype.clear = function (){
    this.setValue('');
}

Search.prototype.change = function (callBack){
    this.jqueryObject.change(callBack());
}

QUnit.test('search macros test', function( assert ) {
    var done = assert.async(); 
    var searchId = 'search', value = 'new value';
    var search = new Search('search');
    assert.equal(searchId, search.macroId);
    search.setValue(value);
    assert.equal(search.getValue(), value);
    search.clear();
    assert.equal(search.getValue(), '');
    function myChange() {
        console.log('111111111111');
    }
    $('#input_search').change(myChange);
    search.change(myChange);
    done();
});