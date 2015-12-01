function IntegerInput (macroId){
    this.jqueryObject = $('#integer_input_'+macroId);

}

IntegerInput.prototype.getValue = function(){
    return this.jqueryObject.val();
}

IntegerInput.prototype.setValue = function(value){
    this.jqueryObject.val(value);
}

IntegerInput.prototype.setOnChangeListener = function (listener) {
    this.jqueryObject.on('change', listener);
}

