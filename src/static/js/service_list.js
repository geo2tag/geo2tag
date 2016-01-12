var Service = Backbone.Model.extend({});

var service = new Service({
    title: "Service"
});

var ServiceList = Backbone.Collection.extend({
    model: Service,
    url: function(){
        var number = 5;
        return '/instance/service?number=' + number;
    }
});

var ServiceView = Backbone.View.extend({
    tagName: "div",
    id: "container_service_list",
    render: function(json) {
        $('#' + this.id).append(get_service_display(json));
        return this;
    },
    clear: function(){
        $('#' + this.id).empty();
    }
});

service_view = new ServiceView({'model' : service});

var ServicePageModel = Backbone.Model.extend({
    initialize: function() {
        this.services = new ServiceList();       
    }
});

service_list_page = new ServicePageModel;

var ServicePageView = Backbone.View.extend({
    initialize:function(){
        this.refresh();
    },

    refresh: function() {
        this_ = this;
        this.model.fetch({
            success: function(){
                this_.render();
            }
        });
    },
    render: function() {
        service_view.clear();
        for(var i = 0; i < this.model.length; i++)
            service_view.render(this.model.at(i).attributes);
    }
});

var service_page = new ServicePageView({model: service_list_page.services});

function get_service_display(json){
    var service_name = json.name;
    var service_id = json._id.$oid;
    var service_link = getUrlWithPrefix('/admin/service/');
    var result = '<div class="row" id="' + service_id + '"><div class="col-xs-8"><h3><a href = ' + service_link + service_id + ' class="service_url">' + service_name + '</a></h3></div>';
    result += '<div class="col-xs-4"><button type="button" class="btn btn-primary btn-lg" service_id="' + service_id + '" id="delete_' + service_name + '" onclick=deleteService("' + service_name + '")>DELETE</button></div></div>';
    return result;
}


function printBootstrapAlert(class_alert, msg){
    result = '<div class="alert alert-' + class_alert + '">';
    result += '<strong>' + status + ' ' + msg + '</strong>';
    result += '</div>';
    console.log(result);
    $('#results_service_search').prepend(result);
}

function deleteService(serviceName){
    $.ajax({
       type: "DELETE",
       url: getUrlWithPrefix('/service/') + serviceName,
       success: function(json, status){
          printBootstrapAlert(status,serviceName+' was deleted successfully'); 
          console.log('service is successfully deleted');
          var tryToKeepPageNumber = true;
          // TODO ability to save active page number after update of URL
          // https://geo2tag.atlassian.net/browse/GT-2112
          refreshServiceList(tryToKeepPageNumber);
       },
       error: function(request, textStatus, errorThrown){
           msg = 'Deleting is finished unsuccessfully ' + textStatus + ': ' + request.status;
           printBootstrapAlert('danger', msg);
           console.log('ERRROR service is unsuccessfully deleted');
       }
     });

}

