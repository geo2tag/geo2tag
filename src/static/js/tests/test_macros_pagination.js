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
