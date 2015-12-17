/* Changes /url/?number=111&test=11&offset=e44
   to /url/?test=11 */
function removeNumberOffsetParameters(url){
    var paramsToRemove = ['number', 'offset'];
    var urlSplit = url.split('?');
    if (urlSplit.length == 1)
        return url;

    var params = urlSplit[1].split('&');
    var filteredParams = [];
    for (var i = 0; i < params.length; i++){
        var param = params[i];
        var paramPair =  param.split('=');
        
        if ( paramsToRemove.indexOf(paramPair[0]) < 0 ){
            filteredParams.push(param);
        }
    }

    var result = urlSplit[0] + '?' + filteredParams.join('&') ;
    return result;
}

/* Performs ajax call for url, run successCallback in case of success 
   (dataSequence length is passed as argument), failCallback in all 
   other */
function calculateListRequestLength(url, successCallback, failCallback){
    var filteredUrl = removeNumberOffsetParameters(url);
    function calculateLength(data){
        var length = data.length;
        successCallback(length);
    }
 
    $.get(filteredUrl, calculateLength).fail(failCallback); 
}
