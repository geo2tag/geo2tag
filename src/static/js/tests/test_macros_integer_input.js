QUnit.test('integer_input test', function( assert ) {
    var done = assert.async();
    var testIntegerInput = new IntegerInput('integer_input');
    var testValue = '1';

    function onChangeListener(){
        assert.equal(testValue, testIntegerInput.getValue());
        done();
    }
    
    testIntegerInput.setOnChangeListener(onChangeListener);
 
    testIntegerInput.setValue(testValue);
    testIntegerInput.jqueryObject.trigger('change');
});
