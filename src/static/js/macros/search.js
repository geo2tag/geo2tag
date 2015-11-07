function Search(macroId) {
    this.macroId = macroId;
    this.jqueryObject = $('input_'+macroId);
}
  
Search.prototype.setValue = function (value){
    this.jqueryObject.val(value);   
}
  
Search.prototype.getValue = function (value){
    return this.jqueryObject.val();
}
  
Search.prototype.clear = function (){
    this.setValue('');
}

Search.prototype.change = function (callBack){
    this.jqueryObject.change(callBack());
}