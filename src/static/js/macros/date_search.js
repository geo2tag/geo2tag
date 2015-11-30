function dateSearch(macroId) {
    this.macroId = macroId;
    this.jqueryObjectDateBegin = $('#date-begin_' + macroId);
    this.jqueryObjectDateEnd = $('#date-end_' + macroId);
    this.jqueryObjectBCBegin = $('#bc_begin_' + macroId);
    this.jqueryObjectBCEnd = $('#bc_end_' + macroId);
}
  
dateSearch.prototype.setValueDateBegin = function (value){
    this.jqueryObjectDateBegin.val(value);   
}

dateSearch.prototype.getValueDateBegin = function (value){
    return this.jqueryObjectDateBegin.val();
}

dateSearch.prototype.setValueBCBegin = function (value){
    this.jqueryObjectBCBegin.attr("checked", value)
}

dateSearch.prototype.getValueBCBegin = function (value){
    return this.jqueryObjectDateBegin.attr("checked");
}
  
dateSearch.prototype.setValueDateEnd = function (value){
    this.jqueryObjectDateEnd.val(value);
}

dateSearch.prototype.getValueDateEnd = function (value){
    return this.jqueryObjectDateEnd.val();
}

dateSearch.prototype.setValueDateEnd = function (value){
    this.jqueryObjectDateEnd.attr("checked", value);
}

dateSearch.prototype.getValueDateEnd = function (value){
    return this.jqueryObjectDateEnd.attr("checked");
}

dateSearch.prototype.clearDateBegin = function (){
    this.setValueDateBegin('');
}

dateSearch.prototype.clearDateEnd = function (){
    this.setValueDateEnd('');
}

dateSearch.prototype.clearBCBegin = function (){
    this.setValueBCBegin('');
}

dateSearch.prototype.clearBCEnd = function (){
    this.setValueBCEnd('');
}

dateSearch.prototype.changeDateBegin = function (callBack){
    this.jqueryObjectDateBegin.change(callBack);
}

dateSearch.prototype.changeDateEnd = function (callBack){
    this.jqueryObjectDateEnd.change(callBack);
}

dateSearch.prototype.changeBCBegin = function (callBack){
    this.jqueryObjectBCBegin.change(callBack);
}

dateSearch.prototype.changeBCEnd = function (callBack){
    this.jqueryObjectBCEnd.change(callBack);
}
