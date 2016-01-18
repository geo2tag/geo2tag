QUnit.test('plugin list', function( assert ) {
    var plugin_json = {'name' : 'test_plugin'};
    var plugin_display = get_plugin_display(plugin_json);
    $('#plugin_list_test').html(plugin_display);
    assert.equal($('#plugin_list_test').children().children().children().length, 3);
});
