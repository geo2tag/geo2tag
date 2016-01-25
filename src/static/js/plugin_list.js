var Plugin = Backbone.Model.extend({});

var plugin = new Plugin({
    title: "Plugin"
});

var PluginList = Backbone.Collection.extend({
    model: Plugin,
    url: function(){
        return '/instance/plugin';
    },
    parse: function (response) {
        var keys = Object.keys(response);
        var result = [];
        for (var i in keys){
             result.push({'name':keys[i]})
        }
        return result;
    }
});

var PluginView = Backbone.View.extend({
    tagName: "div",
    id: "container_plugin_list",
    render: function(json) {
        $('#' + this.id).append(get_plugin_display(json));
        return this;
    },
    clear: function(){
        $('#' + this.id).empty();
    }
});

plugin_view = new PluginView({'model' : plugin});

var PluginPageModel = Backbone.Model.extend({
    initialize: function() {
        this.plugins = new PluginList();       
    }
});

plugin_list_page = new PluginPageModel;

var PluginPageView = Backbone.View.extend({
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
        plugin_view.clear();
        for(var i = 0; i < this.model.length; i++)
            plugin_view.render(this.model.at(i).attributes);
    }
});

var plugin_page = new PluginPageView({model: plugin_list_page.plugins});

function get_plugin_display(json){
    var plugin_name = json.name;
    var result = '<div class="row"><div class="col-xs-8 name-config-plugin"><h3>' + plugin_name + '</h3></div>';
    result += '<div class="col-xs-4"><button type="button" class="btn btn-primary btn-lg btn-delete-plugin">X</button>';
    result += '<a href=' + getUrlWithPrefix('/admin/plugin/config/' + plugin_name) + '><button type="button" class="btn btn-primary btn-lg btn-config-plugin">C</button>' + '</a></div></div>';
    return result;
}