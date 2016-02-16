function convertJsonToIni(json){
    var ini = '';
    for(var obj in json){
        var category = '[' + obj + ']' + '\n'; 
        var parametrs = '';
        for (var par in json[obj]){
            parametrs += String(par) + '=' + String(json[obj][par]) + '\n';
        }
        ini += category;
        ini += parametrs;
    }
    return ini;
}

function convertIniToJson(ini){
    var json = {};
    var category = {};
    var index = ini.length-1;
    var pos = ini.length-2;
    var flag = true;
    while (flag) {
     if((pos = ini.lastIndexOf('\n', pos-1)) != -1){
        str = ini.substring(pos, index);
        if(str.charAt(1) == '['){
            json[str.substring(2,str.length-1)] = category;
            category = {};
        }
        else {
            var i = str.indexOf('=');
            var par = str.substring(1, i);
            var val = str.substring(i+1, str.length);
            category[par] = val;
        }
        index = pos;
      }
      else{
          str = ini.substring(pos, index);
          json[str.substring(1,str.length-1)] = category;
          flag = false;
      }
    }
    return json
}
var url = window.location.toString();
var index = url.lastIndexOf('/');
var plugin_name = url.substring(index+1)
var config_plugin = new ConfigPlugin(plugin_name)
console.log(config_plugin)
var config_pluginview = new ConfigPluginView({'model' : config_plugin})
// fetch
//обновление view
