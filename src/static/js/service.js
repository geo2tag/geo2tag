var ownerInput = null;
var logSizeInput = null;
var flagAddContent;


$(document).ready(function(){
    addSaveServiceHandler();
    initUi();
    setLogSizeOwnerId();
});

function getServiceName(){
    var url_service = location.href;
    var service_str_const = 'service/';
    var length_service_str_const = service_str_const.length;
    var service_str_index = url_service.indexOf(service_str_const);
    var result = url_service.substring(service_str_index + length_service_str_const);
    return result;
}

function checkNewService(service_name){
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

function getValuesForServicePage(service_name){
    $.ajax({
        type: "GET",
        url: getUrlWithPrefix("/service/" + service_name),
        timeout: 150000,
        async: false,
        crossDomain: true,
        success: function(json, status) {
            var service_inf = json;
            var key = 'config';
            log_size = service_inf[key]['logSize'];
            console.log(log_size)
            owner_id = service_inf['owner_id'];
        },
        error: function (request, textStatus, errorThrown){
                   console.log("get service information result: " + textStatus);
        }
    });
    return {'log_size': log_size, 'owner_id': owner_id};    
}

function initUi(){
    ownerInput = new AutocompliteInput('owner_id', '/instance/user?login=' , 'login', '_id');
    logSizeInput = new IntegerInput('log_size');
}

function initValuesForServicePage(){
    var service_name = getServiceName();
    var flag = checkNewService(service_name);
    if(!flag)
        values = getValuesForServicePage(service_name);
    window.flagAddContent = flag;
}


function setLogSizeOwnerId(){
    var service_name = getServiceName();
    $('#service_h2_id').html("");
    if(window.flagAddContent){
        $('#service_h2_id').html('<h2 class="inline">New service ' + service_name + '</h2>');
    }
    else{
        $('#service_h2_id').html('<h2 class="inline">Service ' + service_name + '</h2>');
        $('#integer_input_log_size').val(window.values['log_size']);
        $('#autocomplite_owner_id').val(window.values['owner_id']);
    }
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


