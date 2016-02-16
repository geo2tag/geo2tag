function getConfigDataFromPage(){
    data = $('#container_config_plugin').html();
    data = data.replace('<br>', '\n');
    data = data.replace(/<\/?[^>]+>/g,'');
    console.log(data);
    return data;
}

function saveConfigPluginChange(plugin_name) {
     page_data = getConfigDataFromPage();
     $.ajax({
        type: "PUT",
        url: "/instance/service/" + plugin_name,
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
