var pagination = new Pagination('pagintaion_block');
function testFunction(json){
    return "<div class='row'>" + json.name + "</div>"
}
var testElementsArray = [{name:1}, {name:2}, {name:3}];

QUnit.test('pagination macros init', function( assert ) {
    var active_ul = 'p2';
    var set_active = 'p5';
    var unf = undefined;
    assert.equal(active_ul,pagination.getActiveUlId());
    pagination.removeActivePage();
    assert.equal(unf,pagination.getActiveUlId());
    pagination.setActiveUl(set_active);
    assert.equal(set_active,pagination.getActiveUlId());


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
