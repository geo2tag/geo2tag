function get_service_display(json){
    var service_name = json.name;
    var service_id = json._id;
    var service_link = '/instance/admin/service/';
    var result = '<div class="col-xs-8"><h3><a href = ' + service_link + service_id + '>' + service_name + '</a></h3></div>';
    result += '<div class="col-xs-4"><button type="button" class="btn btn-primary btn-lg" id="delete_service_' + service_id + '">DELETE</button></div>';
    return result;
}
