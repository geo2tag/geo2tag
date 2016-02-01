function convertJsonToIni(json){
    var ini = [];
    for(var obj in json){
        var category = '[' + obj + ']' + '\n'; 
        var parametrs = ''
        for (var par in json[obj]){
            parametrs += String(par) + '=' + String(json[obj][par]) + '\n';
        }
        ini.push(category);
        ini.push(parametrs)
    }
    return ini;
}

function convertIniToJson(ini){
    var json = {};
    var category = {};
    for(var i = ini.length-1; i >= 0; i--){
        if(ini[i].charAt(0) == '['){
            json[ini[i].substring(1,ini[i].length-1)] = category;      
            category = {};
        }
        else {
            var index = ini[i].indexOf('=');
            var par = ini[i].substring(0, index);
            var val = ini[i].substring(index+1, ini[i].length);
            category[par] = val;    
        }
    }
    return(json)
}

