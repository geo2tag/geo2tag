$(document).ready(function(){
    var pagination = new Pagination('service_list');
    pagination.initPagination(5, 20);

    urlBuilder = new UrlBuilder('/instance/service?',  
        {'number':5, 'offset':0});
    urlBuilder.onChange(function(){
        service_list_page.url = this.getUrl();
        service_list_page.refresh();
    });
    urlBuilder.setParameterOnChangeListener('offset', 
        pagination.setOnChangeListener.bind(pagination), 
        pagination.getPageNumber.bind(pagination));
});

