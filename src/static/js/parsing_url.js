function getUrlPage(){
    return window.location.toString();
}

function getArgsQuery(url){ // return json
    var i = url.indexOf('?');
    if(i == -1)
        return {};
    else{
        url = url.substring(i)
        return URI.parseQuery(url)
    }
}
