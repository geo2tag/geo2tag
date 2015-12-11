function Pagination(macroId){
    this.macroId = macroId;
    this.jqueryObject = $('#'+macroId.toString());
    this.jqueryObject.pagination({
            items: 100,
            itemsOnPage: 10,
            cssStyle: 'light-theme'
        });
}
