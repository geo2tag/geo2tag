function AutocompliteInput(macroId,externalValue,internalValue) {
    this.macroId = macroId;
    this.inputobject = $('#autocomplite_'+macroId);
    this.countView = 3;
    this.url_request = 'http://geomongo/instance/user';
    this.externalValue = externalValue;
    this.internalValue = internalValue;
    this.setExternalValue(externalValue);
}
AutocompliteInput.prototype.setExternalValue = function(externalValue){
	this.inputobject.val(externalValue);
}
AutocompliteInput.prototype.getExternalValue = function(){
	return this.inputobject.val();
}
AutocompliteInput.prototype.setInternalValue = function(internalValue){
	this.internalValue = internalValue;
}
AutocompliteInput.prototype.getInternalValue = function(){
	return this.internalValue;
}
