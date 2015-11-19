function saveServiceChange(service_id) {
     $.ajax({
        type: "GET",
        url: "/instance/admin/service" + "service_id",
        timeout: 150000,
        crossDomain: true,
        success: function(json, status) {
            console.log("save service success" );
            spinner.stop(target);
            printBootstrapAlert();
        },
        error: function (jqXHR, textStatus, errorThrown){
            console.log("save service result: " + textStatus);
            console.log(errorThrown);
            spinner.stop(target);
            printBootstrapAlert();
        }
    }); 
}
function addSaveServiceHandler(){
    $('#save_service_btn').click(function(){
        target = document.getElementById('spin')
        spinner = new Spinner().spin(target);
    });

}
function printBootstrapAlert(status){
    result = '<div class="alert alert-"' + status + '>'
    result += '<strong>' + status +'</strong>'
    result += '</div>'
}


