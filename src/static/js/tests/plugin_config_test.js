QUnit.test('plugin config test', function( assert ) {
    var plugin_json = {'cat_1' : {'par_1': 'val_1', 'par_2': 'val_2', 'par_3': 'val_3'}, 'cat_12' : {'par_12': 'val_12', 'par_22': 'val_22'}};
    var ini_valid = ["[cat_1]\n", "par_1=val_1\npar_2=val_2\npar_3=val_3\n", "[cat_12]\n", "par_12=val_12\npar_22=val_22\n"];
    var ini = convertJsonToIni(plugin_json);
    assert.equal(ini, ini_valid);
});
