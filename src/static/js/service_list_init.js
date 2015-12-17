$(document).ready(function(){
    var pagination = new Pagination('service_list');
    pagination.initPagination(5, 20);

/*    urlBuilder = new UrlBuilder('/instance/service?',  
        {'number':5, 'offset':0});
    urlBuilder.setParameterOnChangeListener('offset', 
        pagination.setOnChangeListener, 
        pagination.getPageNumber);


    urlBuilder.onChange(function(){
        service_list_page.url = this.getUrl();
        service_list_page.refresh(); //?
    });*/
});

