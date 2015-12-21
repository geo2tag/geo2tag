function Pagination(macroId, viewFunction){
    this.macroId = macroId;
    this.jqueryObject = $('#'+macroId.toString());
    this.container = $('#container_' + macroId.toString());
    this.setViewFunction(viewFunction);
    this.jqueryObject.bind('click', function(){});
    this.setPageNumber(1);
}

Pagination.prototype.initPagination = function (totalNum, elPerPage){
    var this_ = this;
    this.jqueryObject.pagination({
            items: totalNum,
            itemsOnPage: elPerPage,
            cssStyle: 'light-theme',
            onPageClick: function(pageNumber){
                this_.setPageNumber(pageNumber);
                if (this_.onChangeListener!= undefined) {
                    this_.onChangeListener();
                }
            }
        });
    var elementsArray = [];
    this.drawPage(elementsArray);
}

Pagination.prototype.setOnChangeListener = function(listener){
    this.onChangeListener = listener;
}

Pagination.prototype.getPageNumber = function (){
    return this.pageNumber;
}

Pagination.prototype.setPageNumber = function (pageNumber){ 
    this.pageNumber = pageNumber;
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
