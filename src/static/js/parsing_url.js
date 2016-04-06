function getUrlPage(){
    return window.location.toString();
}

function getArgsQuery(url){ # return json
    return URI.parseQuery(url)
}
