function Pagination(macroId, viewFunction){
    this.macroId = macroId;
    this.jqueryObject = $('#'+macroId.toString());
    this.container = $('#container_' + macroId.toString());
    this.initPagination(100, 10);
    this.setViewFunction(viewFunction);
}

Pagination.prototype.initPagination = function (totalNum, elPerPage){
    this.jqueryObject.pagination({
            items: totalNum,
            itemsOnPage: elPerPage,
            cssStyle: 'light-theme'
        });
    var elementsArray = [];
    this.drawPage(elementsArray);
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


Pagination.prototype.setActiveUl = function(ulId){
    this.removeActivePage();
    this.jqueryObject.children('#' + ulId).addClass('active');
}
Pagination.prototype.getActiveUlId = function(){
    var list_ul = this.jqueryObject.children();
    for(var  i = 0;i<list_ul.length;i++){
	if($(list_ul[i]).attr('class') == 'active'){
            return list_ul[i].id;
	    continue;
	}
    }
}
Pagination.prototype.getActiveUlNumber = function(){
    var list_ul = this.jqueryObject.children();
    for(var  i = 0;i<list_ul.length;i++){
	if($(list_ul[i]).attr('class') == 'active'){
	    return i;
	    continue;
	}
    }
}
Pagination.prototype.removeActivePage = function(){
    this.jqueryObject.children().removeClass();
}
