/*
    How to use this module: add <div id="alert_div'></div> into your markup where
    you whant to be alerts displayed. Than call print<STATUS>Alert(message) 
*/

var SUCCESS = 'success';
var DANGER = 'danger';
var INFO = 'info';
var WARNING = 'warning';
var ALERT_DIV_ID = 'alert_div';

function generateAlert(alertType, message){
    var result = '<div class="alert alert-' + alertType + '">';
    result += '<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>';
    result += '<strong>' + message + '</strong>';
    result += '</div>';
    return result;
}

function printBootstrapAlert(alertType, message){
    var result = generateAlert(alertType, message);
    $('#'+ ALERT_DIV_ID).prepend(result);
}

function printSuccessAlert(message){
    printBootstrapAlert(SUCCESS, message);
}

function printDangerAlert(message){
    printBootstrapAlert(DANGER, message);
}

function printInfoAlert(message){
    printBootstrapAlert(INFO, message);
}

function printWarningAlert(message){
    printBootstrapAlert(WARNING, message);
}
