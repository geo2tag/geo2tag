function get_plugin_display(json){
    var plugin_name = json.name;
    var plugin_id = json.id;
    var result = '<div class="row" id="' + plugin_id + '"><div class="col-xs-8"><h3>' + plugin_name + '</h3></div>';
    result += '<div class="col-xs-4"><button type="button" class="btn btn-primary btn-lg" plugin_id="' + plugin_id + '">X</button>';
    result += '<button type="button" class="btn btn-primary btn-lg btn-config-plugin" plugin_id="' + plugin_id + '">C</button>' + '</div></div>';
    return result;
}
