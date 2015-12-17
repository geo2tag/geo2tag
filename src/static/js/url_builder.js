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
    return this.url;
}

UrlBuilder.onChange(listener) 


