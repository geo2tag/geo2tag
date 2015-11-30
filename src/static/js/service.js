var ownerInput = null;
var logSizeInput = null;

$(document).ready(function (){
    addSaveServiceHandler();
    initUi();
});

function checkNewService(){
    service_name = getServiceName();
    $.ajax({
        type: "GET",
        url: getUrlWithPrefix("/service"),
        timeout: 150000,
        async: false,
        crossDomain: true,
        success: function(json, status) {
            var service_list = json;
            var key = 'name';
            flag = true;
            for(var i = 0; i < service_list.length; i++){
                if(service_list[i][key] == service_name){
                    flag = false;
                    break;
                }
            }           
        },
        error: function (request, textStatus, errorThrown){
                   console.log("get service list result: " + textStatus);
        }
    });
    return flag;
}
function initUi(){
    var flag = checkNewService();
    if(flag){
        $('#service_h2_id').prepend('<h2>New</h2>');        
    }
    ownerInput = new AutocompliteInput('owner_id', '/instance/user?login=' , 'login', '_id');
    logSizeInput = new IntegerInput('log_size');
}

function getDataFromPage(){
    data = {'logSize' : logSizeInput.getValue()}
    return data;
}


function saveServiceChange(service_id) {
     page_data = getDataFromPage();
     console.log(service_id)
     $.ajax({
        type: "PUT",
        url: "/instance/service/" + service_id,
        timeout: 150000,
        crossDomain: true,
        data: page_data,
        success: function(json, status) {
            console.log("save service success" );
            alert('this alert must be deleted');
            spinner.stop(target);
            printBootstrapAlert(status,'Saving is finished successfully');
        },
        error: function (request, textStatus, errorThrown){
            console.log("save service result: " + textStatus);
            msg = 'Saving is finished unsuccessfully ' + textStatus + ': ' + request.status;
            printBootstrapAlert('danger', msg);
        }
    }); 
}

function addSaveServiceHandler(){
    $('#save_service_btn').click(function(){
        target = document.getElementById('spin')
        spinner = new Spinner().spin(target);
    });
}

function printBootstrapAlert(class_alert, msg){
    result = '<div class="alert alert-' + class_alert + '">';
    result += '<strong>' + status + ' ' + msg + '</strong>';
    result += '</div>';
    console.log(result);
    $('#main_div_service_page_id').prepend(result);
}


