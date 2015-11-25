QUnit.test('search autocompliteinput test', function( assert ) {
    var done = assert.async();
    var testLogin = 'test_user';
    var testId = 'ZzKPM5GJQ1';
    var validUrl = '/instance/user?login='+testLogin+'&number=3&offset=0';
    console.log('validUrl: '+validUrl);

       // Called when menu is selected
    var selectListener = function( e, ui ) {
           console.log('select');
           assert.equal(validUrl, testObject.buildUrl());
           assert.equal(testLogin, testObject.getExternalValue());
           assert.equal(testId, testObject.getInternalValue());
           done();
    };
    var testObject = new AutocompliteInput('test', '/instance/user?login=' , 'login', '_id', selectListener);

    testObject.jQueryObject.autocomplete({
       // Called when menu is shown
       open: function( event, ui ) {
           console.log('open');
           $("a:contains('"+ testLogin +"')").trigger('mouseover').trigger('click');
       }
 
    });

    // Testing autocomplite
    testObject.setExternalValue(testLogin);
    testObject.jQueryObject.autocomplete("search");
});
