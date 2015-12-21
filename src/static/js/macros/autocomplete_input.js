/*
  macroId - macros unique identifier
  url - url for retriving objects list. Note that @SUBSTRING@&number=3&offset=0  will be added to it
  externalValueKey - key for displayed value in the input field (e.g. user_login)
  internalValueKey - key for actual needed data (e.g. user_id)
  selectListener - function (e, ui) for additional processing of onselect event for autocomplite 

*/
function AutocompliteInput(macroId, url, externalValueKey, internalValueKey, selectListener) {
    this.macroId = macroId;
    this.jQueryObject = $('#autocomplite_'+macroId);
    this.countView = 3;
    this.url = url; //'http://geomongo/instance/user?login=';
    this.externalValueKey = externalValueKey;
    this.internalValueKey = internalValueKey;
    if (selectListener != undefined)
       this.setSelectListener(selectListener);
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
    console.log(fn);
    console.log(this.jQueryObject);
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
            console.log( ui.item);
            fn.setExternalValue(ui.item.label);
            fn.internalValue = ui.item.value;
            console.log(fn.internalValue);
            e.preventDefault();
            if (fn.selectListener !== undefined)
                fn.selectListener(e, ui);
        }
    }); 
}

AutocompliteInput.prototype.setSelectListener = function(selectListener){
    this.selectListener = selectListener;
    this.setupAutocomplite();
}
