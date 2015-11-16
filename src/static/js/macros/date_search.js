function Date_search(macroId) {
    this.macroId = macroId;
    this.jqueryObject = $('#input_'+macroId);
}
  
Date_search.prototype.setValue = function (value){
    this.jqueryObject.val(value);   
}
  
Date_search.prototype.getValue = function (value){
    return this.jqueryObject.val();
}
  
Search.prototype.clear = function (){
    this.setValue('');
}

Search.prototype.change = function (callBack){
    this.jqueryObject.change(callBack);
}
