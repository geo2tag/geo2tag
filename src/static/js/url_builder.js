UrlBuilder(baseUrl, defaultParameters){
    this.baseUrl = baseUrl;
    this.parameterDicts = defaultParameters;
}

UrlBuilder.prototype.setParameterOnChangeListener = function(parameterName, setMethodForElementOnChange, getValueMethod){
    setMethodForElementOnChange = function (){
        this.parameterDicts[parameterName] = getValueMethod();  
    }
}

UrlBuilder.prototype.getUrl = function(){
    var keys = ['number', 'offset', 'substring']
    this.url = baseUrl;
    for(var key in keys){
        if(key in this.parameterDicts){
            this.url += key + this.parameterDicts[key];
        }
    }
    return this.url;
}


UrlBuilder.onChange(listener) 


