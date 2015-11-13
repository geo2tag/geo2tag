function Pagination(macroId){
	this.macroId = macroId;
    this.jqueryObject = $('#'+macroId.toString());
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