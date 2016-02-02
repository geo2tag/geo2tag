QUnit.test('plugin config test', function( assert ) {
var plugin_json = {'cat_1' : {'par_1': 'val_1', 'par_2': 'val_2', 'par_3': 'val_3'}, 'c' : {'par_12': 'val_12', 'par_3': 'val_3'}, '1': {'a':'b'}}

ini = convertJsonToIni(plugin_json)
var result_json = convertIniToJson(ini)
console.log(plugin_json)
console.log(result_json)
console.log(ini)
assert.equal(plugin_json, result_json)
});
