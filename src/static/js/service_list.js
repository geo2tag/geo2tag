var Service = Backbone.Model.extend({});

service = new Service({
    title: "Service"
    // получить json c инф о сервисе
});


var ServiceList = Backbone.Collection.extend({
    model: Service
    // filter: function(){} 

});

var service_list = new ServiceList();

service_list.add({
    title: "Service List"
});

var ServiceView = Backbone.View.extend({
    tagName: "div",
    className: "container",
    render: function() { // отрисовка вида (одного сервиса)
        $(this.el).html(get_service_display(this.model.json))
    }
//    initialize: function(){    }
});

function get_service_display(json){
    var service_name = json.name;
    var service_id = json._id;
    var service_link = getUrlWithPrefix('/admin/service/');
    var result = '<div class="row" id="' + service_id + '"><div class="col-xs-8"><h3><a href = ' + service_link + service_id + '>' + service_name + '</a></h3></div>';
    result += '<div class="col-xs-4"><button type="button" class="btn btn-primary btn-lg" service_id="' + service_id + '">DELETE</button></div></div>';
    return result;
}
