function Pagination(macroId, viewFunction){
    this.macroId = macroId;
    this.jqueryObject = $('#'+macroId.toString());
    this.container = $('#container_' + macroId.toString());
    this.setViewFunction(viewFunction);
    this.jqueryObject.bind('click', function(){});
    this.isPaginationDefined = false;
    this.setPageNumber(1);
}

Pagination.prototype.initPagination = function (totalNum, elPerPage){
    console.log('initPagination');
    this.setElementsPerPage(elPerPage);
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
    this.isPaginationDefined = true;
    // In case that we are standing on the page, which will not exist after pagesCount changed
    this.setPageNumber(1);
    return this.getOffsetValue();
}

Pagination.prototype.getPagesCount = function(){
    if (this.isPaginationDefined)
        return this.jqueryObject.pagination('getPagesCount');

    return 0;
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

Pagination.prototype.isPageNumberChanged = function (length){
    var interval = this.getElementsPerPage();
    if (interval == undefined)
        return true;
    var newPagesCount = Math.ceil(length / interval);
    console.log('isPageNumberChanged : '+newPagesCount+' '+this.getPagesCount());
    return newPagesCount != this.getPagesCount();
}

Pagination.prototype.setElementsPerPage = function (elPerPage){
    this.elementsPerPage = elPerPage;
}

Pagination.prototype.getElementsPerPage = function (){
    return this.elementsPerPage;
}

Pagination.prototype.getOffsetValue = function(){
    return this.getElementsPerPage()*(this.getPageNumber() - 1);
}
