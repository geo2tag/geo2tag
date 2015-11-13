QUnit.test('pagination macros test', function( assert ) {
    var done = assert.async();
    var active_ul = 'p2';
    var set_active = 'p5';
    var unf = undefined;
    var pagination = new Pagination('pagintaion_block');
    assert.equal(active_ul,pagination.getActiveUlId());
    pagination.removeActivePage();
    assert.equal(unf,pagination.getActiveUlId());
    pagination.setActiveUl(set_active);
    assert.equal(set_active,pagination.getActiveUlId());
    done();
});