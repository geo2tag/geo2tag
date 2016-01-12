var test_id = 'pagintaion_block'
var pagination = new Pagination(test_id);

function testFunction(json){
    return "<div class='row'>" + json.name + "</div>"
}
var testElementsArray = [{name:1}, {name:2}, {name:3}];

QUnit.test('pagination macros init', function( assert ) {
    var elements_count = 10;
    pagination.initPagination(100, elements_count);
    assert.equal($('#' + test_id).children().children().length, elements_count)

});

QUnit.test('pagination macros viewFunction', function( assert ) {

    pagination.setViewFunction(testFunction);
    assert.equal(pagination.getViewFunction(), testFunction);     
    
});

QUnit.test('pagination macros drawPage', function( assert ) {
    pagination.setViewFunction(testFunction);
    
    pagination.drawPage(testElementsArray);
    var elements = $('#container_pagintaion_block').children();
    assert.equal( elements.length, testElementsArray.length);

    pagination.clearPage();
    var elements = $('#container_pagintaion_block').children();
    assert.equal( elements.length, 0);
    
});

QUnit.test('pagination macros test', function( assert ) {
    assert.ok($('#pagintaion_block').children().children().length > 0);
});

QUnit.test('pagination macros change page', function( assert ) {
    var done = assert.async();
    var service_list_id = 'service_list'
    var pagination_service_list = new Pagination(service_list_id);
    pagination_service_list.initPagination(20, 5);
    urlBuilder = new UrlBuilder('/instance/service?',  
        {'number':5, 'offset':0});
    urlBuilder.setParameterOnChangeListener('offset',
        pagination_service_list.setOnChangeListener.bind(pagination_service_list),
        pagination_service_list.getPageNumber.bind(pagination_service_list));

    urlBuilder.setOnChangeListener(function(){
        service_page.model.url = this.getUrl();
        service_page.refresh();
    });
    var test_service_list_id = 'macro_pagination_service_list'
    var test_id_first_page = $('#' + test_service_list_id).children().children().attr('id');
    console.log(test_id_first_page)
    console.log($('#' + test_service_list_id).children())
    $('a.next').trigger('click');
    setTimeout(function(){
        var test_id_second_page = $('#' + test_service_list_id).children().children().attr('id'); 
        assert.ok(test_id_first_page != test_id_second_page);
        done();
    }, 1000);
    
});
