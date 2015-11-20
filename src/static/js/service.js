$(document).ready(function (){
    addSaveServiceHandler();
});

function getDataFromPage(){
    data = {'logSize' : $('#logsize_id').val()}
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


