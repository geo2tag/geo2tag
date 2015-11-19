function saveServiceChange(service_id) {
     $.ajax({
        type: "GET",
        url: "/instance/admin/service" + "service_id",
        timeout: 150000,
        crossDomain: true,
        success: function(json, status) {
            console.log("save service success" );
            alert('');
            spinner.stop(target);
        },
        error: function (jqXHR, textStatus, errorThrown){
            console.log("save service result: " + textStatus);
            console.log(errorThrown);
            alert('')
            spinner.stop(target);
        }
    }); 
}
function addSaveServiceHandler(){
    $('#save_service_btn').click(function(){
        target = document.getElementById('spin')
        spinner = new Spinner().spin(target);
    });

}

