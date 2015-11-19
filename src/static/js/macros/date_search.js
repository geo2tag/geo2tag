function dateSearch(macroId) {
    this.macroId = macroId;
    this.jqueryObjectDateBegin = $('#date-begin_' + macroId);
    this.jqueryObjectDateEnd = $('#date-end_' + macroId);
}
  
dateSearch.prototype.setValueDateBegin = function (value){
    this.jqueryObjectDateBegin.val(value);   
}

dateSearch.prototype.getValueDateBegin = function (value){
    return this.jqueryObjectDateBegin.val();
}
  
dateSearch.prototype.setValueDateEnd = function (value){
    this.jqueryObjectDateEnd.val(value);
}

dateSearch.prototype.getValueDateEnd = function (value){
    return this.jqueryObjectDateEnd.val();
}

dateSearch.prototype.clearDateBegin = function (){
    this.setValueDateBegin('');
}

dateSearch.prototype.clearDateEnd = function (){
    this.setValueDateEnd('');
}

dateSearch.prototype.changeDateBegin = function (callBack){
    this.jqueryObjectDateBegin.change(callBack);
}

dateSearch.prototype.changeDateEnd = function (callBack){
    this.jqueryObjectDateEnd.change(callBack);
}

