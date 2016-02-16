QUnit.test('plugin config test', function( assert ) {
    var plugin_json = {'cat_1' : {'par_1': 'val_1', 'par_2': 'val_2', 'par_3': 'val_3'}, 'c' : {'par_12': 'val_12', 'par_3': 'val_3'}, '1': {'a':'b'}}
    var ini = '[1]\na=b\n[cat_1]\npar_1=val_1\npar_2=val_2\npar_3=val_3\n[c]\npar_12=val_12\npar_3=val_3\n'
    var result_ini = convertJsonToIni(plugin_json);
    var result_json = convertIniToJson(ini);
    assert.deepEqual(plugin_json, result_json);
    assert.equal(ini, result_ini);
});
