function Pagination(macroId, viewFunction){
    this.macroId = macroId;
    this.jqueryObject = $('#'+macroId.toString());
    this.jqueryObject.pagination({
            items: 100,
            itemsOnPage: 10,
            cssStyle: 'light-theme'
        });
    this.setViewFunction(viewFunction);
    this.jqueryObject.bind('click', function() {});
}

/*
   viewFunction - function with single argument json, which is a 
       (json) representation of single pagination object. viewFunction
       returns html view of single pagination object.
*/

Pagination.prototype.setViewFunction = function (viewFunction){
    this.viewFunction = viewFunction;
}

Pagination.prototype.getViewFunction = function (){
    return this.viewFunction;
}
