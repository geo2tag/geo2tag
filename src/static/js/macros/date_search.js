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

dateSearch.prototype.setValueDateEnd = function (value){
    this.jqueryObjectDateEnd.val(value);
}

dateSearch.prototype.getValueDateEnd = function (value){
    return this.jqueryObjectDateEnd.val();
}

dateSearch.prototype.setValueBCBegin = function (value){
    if(value == false)
        this.jqueryObjectBCBegin.removeAttr("checked")
    else
        this.jqueryObjectBCBegin.attr("checked", "checked")
}

dateSearch.prototype.getValueBCBegin = function (){
    if(this.jqueryObjectBCBegin.attr("checked") == "checked")
        return true;
    return false;
}
  
dateSearch.prototype.setValueBCEnd = function (value){
    if(value == false)
        this.jqueryObjectBCEnd.removeAttr("checked")
    else
        this.jqueryObjectBCEnd.attr("checked", "checked")
}

dateSearch.prototype.getValueBCEnd = function (){
    console.log(this.jqueryObjectBCEnd.attr("checked"))
    if(this.jqueryObjectBCEnd.attr("checked") == "checked")
        return true;
    return false;
}

dateSearch.prototype.clearDateBegin = function (){
    this.setValueDateBegin('');
}

dateSearch.prototype.clearDateEnd = function (){
    this.setValueDateEnd('');
}

dateSearch.prototype.clearBCBegin = function (){
    this.setValueBCBegin(false);
}

dateSearch.prototype.clearBCEnd = function (){
    this.setValueBCEnd(false);
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
