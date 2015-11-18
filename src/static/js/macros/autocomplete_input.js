
function AutocompliteInput(macroId,externalValue,internalValue) {
    this.macroId = macroId;
    this.inputobject = $('#autocomplite_'+macroId);
    this.countView = 3;
    this.url_request = 'http://geomongo/instance/user';
    this.setInternalValue(internalValue);
    this.setExternalValue(externalValue);    
}
AutocompliteInput.prototype.setExternalValue = function(externalValue){
	this.inputobject.val(externalValue);
    this.externalValue = externalValue;
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
AutocompliteInput.prototype.makeAutocompliteToRequest = function(){
    var fn = this;
    var name = this.getExternalValue(); 
    var req_url = this.url_request + '?login=' + name + '&number=' + this.countView + '&offset=0'
    $( this.inputobject).autocomplete({
        source: function(request, response) {
            $.get( req_url, function( data ) {
                var list = [];
                for(var i = 0;i<data.length;i++){
                    list.push({
                        label:data[i]['login'],
                        value:data[i]['_id']
                    });
                }
                response(list);  
                
            });
        },
        select:function(e, ui) {
            //this.externalValue = ui.item.label;
            fn.internalValue = 1;
            e.preventDefault();
            $(this).val(ui.item.label);
        }
    }); 
}
