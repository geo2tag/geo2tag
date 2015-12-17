var counter = 0;
QUnit.test('url_builder', function(assert) {
    var done = assert.async()
    var baseUrl = '/instance/test?';
    var validUrl = baseUrl + 'number=10&offset=4';

    // Setting up urlBuilder

    var urlBuilder = new UrlBuilder(baseUrl, {});
    var callback = function(){
        counter++; 
        if (counter == 2){
            var testUrl = urlBuilder.getUrl();
            assert.equal(testUrl, validUrl);
            done();
        }
    }
    urlBuilder.setOnChangeListener(callback);

    var numberWidget = $('#number');
    var offsetWidget = $('#offset');

    urlBuilder.setParameterOnChangeListener('number', 
        numberWidget.change.bind(numberWidget), numberWidget.val.bind(numberWidget))

    urlBuilder.setParameterOnChangeListener('offset', 
        offsetWidget.change.bind(offsetWidget), offsetWidget.val.bind(offsetWidget)) 

    //  Emulating changes at number and offset
    numberWidget.val(10).trigger('change');
    offsetWidget.val(4).trigger('change');

       

});
