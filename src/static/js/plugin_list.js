var Plugin = Backbone.Model.extend({});

var ConfigPlugin = Backbone.Model.extend({
    url: function(){
        plugin_name = this.plugin_name
        return '/instance/plugin_config/' + plugin_name;
    },
    constructor: function(plugin_name) {
        this.plugin_name = plugin_name;
        Backbone.Model.apply(this, arguments);
    }
});

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
            var enabled = response[keys[i]]['enabled'];
            result.push({'name':keys[i], 'enabled': enabled})
        }
        return result;
    }
});

var ConfigPluginView = Backbone.View.extend({
    tagName: "textarea",
    id: "container_config_plugin",
    initialize:function(){
        this.refresh();
    },
    refresh: function() {
        this_ = this;
        this.model.fetch({
            success: function(json){
                this_.render(json.attributes);
            }
        });
    },
    render: function(json) {
        this.clear();
        $('#' + this.id).html(get_config_plugin_display(json));
        return this;
    },
    clear: function(){
        $('#' + this.id).empty();
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

var plugin_list_page = new PluginPageModel;


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

function get_plugin_enable_button_text(json){
    if (json.enabled == true)
        return 'Disable';

    return 'Enable';
}

function get_config_plugin_display(json){
    var ini = convertJsonToIni(json)
    return ini;
}

function get_plugin_display(json){
    console.log(json);
    var plugin_name = json.name;
    
    var result = '<div class="row"><div class="col-xs-8 name-config-plugin"><h3>' + plugin_name + '</h3></div>';
    result += '<div class="col-xs-4"><button plugin_name="' + plugin_name + '" type="button" class="btn btn-primary btn-lg btn-delete-plugin" onclick=unable_plugin("' + plugin_name + '",'+json.enabled +')>' + get_plugin_enable_button_text(json) + '</button>';
    result += '<a target="_blank" href=' + getUrlWithPrefix('/admin/plugin/config/' + plugin_name) + '><button type="button" class="btn btn-primary btn-lg btn-config-plugin">C</button>' + '</a></div></div><hr>';
    return result;
}

function unable_plugin(pluginName, enabled){
    var state = !enabled; 
    stateText = '';
    if (state)
        stateText = 'enabled';
    else
        stateText = 'disabled';
    $.ajax({
       type: "GET",
       url: getUrlWithPrefix('/manage_plugins?') + pluginName + '=' + state,
       success: function(json, status){
          plugin_page.refresh();
          var message = pluginName + ' was ' + stateText + ' successfuly';
          printSuccessAlert(message);
          console.log(message);
       },
       error: function(request, textStatus, errorThrown){
          plugin_page.refresh();
          message = 'An error occured while set ' + pluginName + ' ' + 
              stateText + ':' + textStatus;
          printDangerAlert(message);
          console.log(message);
       }
     });

}
