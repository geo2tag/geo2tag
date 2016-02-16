function getConfigDataFromPage(){
    data = $('#container_config_plugin').html();
    data = data.replace('<br>', '\n');
    data = data.replace(/<\/?[^>]+>/g,'');
    data = convertIniToJson(data);
    console.log(data)
    return data;
}

function saveConfigPluginChange(plugin_name) {
     page_data = getConfigDataFromPage();
     $.ajax({
        type: "PUT",
        url: "/instance/plugin_config/" + plugin_name,
        timeout: 150000,
        crossDomain: true,
        data: page_data,
        success: function(json, status) {
            console.log("save plugin config success" );
            spinner.stop(target);
            printBootstrapAlert(status,'Saving is finished successfully');
        },
        error: function (request, textStatus, errorThrown){
            console.log("save plugin config result: " + textStatus);
            msg = 'Saving is finished unsuccessfully ' + textStatus + ': ' + request.status;
            printBootstrapAlert('danger', msg);
        }
    }); 
}

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
    ini = ini.replace('=', '":"')
    ini = ini.replace('[', '"')
    ini = ini.replace(']\n', '":{"')
    ini = ini.replace('\n', '"}')
    ini = '{' + ini + '}'
    console.log(ini)
    result = JSON.parse(ini)
    console.log(result)
    return result;
}

$(document).ready(function(){
    var url = window.location.toString();
    var index = url.lastIndexOf('/');
    var plugin_name = url.substring(index+1)
    var config_plugin = new ConfigPlugin(plugin_name)
    var config_pluginview = new ConfigPluginView({'model' : config_plugin})
});
