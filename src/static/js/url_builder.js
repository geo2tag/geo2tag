/*
   baseUrl - url for parameters concatenaiton. must be ended with ? or &
   initialParameters - dict of parameters initial values 
*/

function UrlBuilder(baseUrl, initialParameters){
    this.baseUrl = baseUrl;
    this.parameterDicts = initialParameters;
}

UrlBuilder.prototype.setParameterOnChangeListener = function(parameterName, 
                                                             setMethodForElementOnChange, 
                                                             getValueMethod){
    var this_ = this;
    console.log(this)
    setMethodForElementOnChange( function (){
        console.log(this_.parameterDicts);
        this_.parameterDicts[parameterName] = getValueMethod();  
        this_.onChangeListener();
    });
}

/*
  Parameter @offset@ is needed for handling situation when page count changed and current offset became invalid
*/
UrlBuilder.prototype.getUrl = function(offset){
    if (offset != undefined)
        this.parameterDicts.offset = offset;
    var params = [];
    for (var key in this.parameterDicts){
        params.push(key + '=' + this.parameterDicts[key]);
    }

    return this.baseUrl + params.join('&'); 
}

UrlBuilder.prototype.setOnChangeListener = function(listener){
    this.onChangeListener = listener;
}
