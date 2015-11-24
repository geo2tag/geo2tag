function AutocompliteInput(macroId, url, externalValueKey, internalValueKey, selectListener) {
    this.macroId = macroId;
    this.jQueryObject = $('#autocomplite_'+macroId);
    this.countView = 3;
    this.url = url; //'http://geomongo/instance/user?login=';
    this.externalValueKey = externalValueKey;
    this.internalValueKey = internalValueKey;
    this.selectListener = selectListener;
    this.setupAutocomplite();
}

AutocompliteInput.prototype.setExternalValue = function(externalValue){
    this.jQueryObject.val(externalValue);
    this.externalValue = externalValue;
}

AutocompliteInput.prototype.getExternalValue = function(){
    return this.jQueryObject.val();
}

AutocompliteInput.prototype.setInternalValue = function(internalValue){
    this.internalValue = internalValue;
}

AutocompliteInput.prototype.getInternalValue = function(){
    return this.internalValue;
}

// Creates url for request of entities
AutocompliteInput.prototype.buildUrl = function (){
    var name = this.getExternalValue(); 
    return this.url + name + '&number=' + this.countView + '&offset=0';
}

AutocompliteInput.prototype.setupAutocomplite = function(){
    var fn = this;
    $( this.jQueryObject).autocomplete({
        source: function(request, response) {
            $.get( fn.buildUrl(), function( data ) {
                var list = [];
                for(var i = 0;i<data.length;i++){
                    list.push({
                        label:data[i][fn.externalValueKey],
                        value:data[i][fn.internalValueKey]
                    });
                }
                response(list);  
                
            });
        },
        select: function(e, ui) {
            //this.externalValue = ui.item.label;
            console.log( ui.item);
            fn.internalValue = ui.item.label;
            console.log(fn.internalValue);
            e.preventDefault();
            fn.selectListener(ui);
            //$(this).val(ui.item.label);
        }
    }); 
}
