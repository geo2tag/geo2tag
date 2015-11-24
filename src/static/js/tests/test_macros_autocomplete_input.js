QUnit.test('search autocompliteinput test', function( assert ) {
    var done = assert.async();
    var validUrl = '/instance/user?login=test&number=3&offset=0';
    var testLogin = 'test_user';
    var testId = 'ZzKPM5GJQ1';

       // Called when menu is selected
    var selectListener = function( ui ) {
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
