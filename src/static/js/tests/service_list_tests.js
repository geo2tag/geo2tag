QUnit.test('service list', function( assert ) {
    var service_link = "/instance/admin/service/ObjectId('55671ae113293c504d515a33')"
    var service_btn_del_id = "ObjectId('55671ae113293c504d515a33')"
    var service_json = {'name' : 'test_service', '_id' : {'$oid':"ObjectId('55671ae113293c504d515a33')"}};
    var service_display = get_service_display(service_json);
    $('#service_list_test').html(service_display);
    assert.equal($('#service_list_test').children().children().children().length, 2);
    var service_link_result = $('#service_list_test').children().children().children().children('a').attr('href');
    assert.equal(service_link, service_link_result);
    var service_btn_del_id_result = $('#service_list_test').children().children().children('button').attr('service_id');
    assert.equal(service_btn_del_id, service_btn_del_id_result);
});
