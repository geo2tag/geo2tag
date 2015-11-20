$(document).ready(function (){
    addSaveServiceHandler();
});

function saveServiceChange(service_id) {
     $.ajax({
        type: "GET",
        url: "/instance/admin/service" + service_id,
        timeout: 150000,
        crossDomain: true,
        success: function(json, status) {
            console.log("save service success" );
            alert('this alert must be deleted')
            spinner.stop(target);
            console.log(json);
            printBootstrapAlert(status, status, 'json');
        },
        error: function (jqXHR, textStatus, errorThrown){
            console.log("save service result: " + textStatus);
            console.log(errorThrown);
            printBootstrapAlert('danger', textStatus, '');
        }
    }); 
}

function addSaveServiceHandler(){
    $('#save_service_btn').click(function(){
        target = document.getElementById('spin')
        spinner = new Spinner().spin(target);
    });
}

function printBootstrapAlert(class_alert, status, msg){
    result = '<div class="alert alert-' + class_alert + '">';
    result += '<strong>' + status + ' ' + msg + '</strong>';
    result += '</div>';
    console.log(result);
    $('#main_div_service_page_id').prepend(result);
}


