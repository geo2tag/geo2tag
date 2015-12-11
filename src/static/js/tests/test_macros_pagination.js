QUnit.test('pagination macros test', function( assert ) {
    var pagination = new Pagination('pagintaion_block');
    assert.ok($('#pagintaion_block').children().children().length > 0);

    function testFunction(json){
        return "<div>" + json.name + "</div>"
    }

    pagination.setViewFunction(testFunction);
    assert.equal(pagination.getViewFunction(), testFunction);
});
