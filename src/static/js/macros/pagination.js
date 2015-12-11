function Pagination(macroId, viewFunction){
    this.macroId = macroId;
    this.jqueryObject = $('#'+macroId.toString());
    this.setViewFunction(viewFunction);
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
