var Service = Backbone.Model.extend({});

service = new Service({
    title: "Service"
});


var ServiceList = Backbone.Collection.extend({
    model: Service
    // url: '/service' -> service_list.fetch();
    // filter: function(){} 

});

var service_list = new ServiceList();

service_list.add({
    title: "Service List"
});

var ServiceView = Backbone.View.extend({
    tagName: "div",
    className: "container",
    render: function() { // отрисовка вида (сервиса)
        $(this.el).html(get_service_display(json)) // контроллер получит json
    }
    initialize: function(){


    }
});
