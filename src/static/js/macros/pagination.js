function Pagination(macroId, viewFunction){
    this.macroId = macroId;
    this.jqueryObject = $('#'+macroId.toString());
    this.jqueryObject.pagination({
            items: 100,
            itemsOnPage: 10,
            cssStyle: 'light-theme'
        });
    this.container = $('#container_' + macroId.toString());

    this.setViewFunction(viewFunction);
    this.jqueryObject.bind('click', function(){});
}

/*
  viewFunction - function with single argument, which is a 
       (json) representation of single pagination object. viewFunction
       returns html view of single pagination object.
*/

Pagination.prototype.setViewFunction = function (viewFunction){
    this.viewFunction = viewFunction;
}

Pagination.prototype.getViewFunction = function (){
    return this.viewFunction;
}

Pagination.prototype.drawPage = function (elementsArray){
    var elementView = undefined;
    for (var i=0; i < elementsArray.length; i++){
        elementView = this.viewFunction(elementsArray[i]);
        this.container.append(elementView);
    }
}

Pagination.prototype.clearPage = function (){
    this.container.empty();
}

Pagination.prototype.refreshPage = function (elementsArray){
    this.draPage(elementsArray);
    this.clearPage();
}
