$(document).ready(function(){
    var pagination = new Pagination('service_list');
    pagination.initPagination(20, 5);

    urlBuilder = new UrlBuilder('/instance/service?',  
        {'number':5, 'offset':0});
    var callback = function(){
        service_list_page.model.url = this.getUrl();
        console.log(service_list_page.model.url)
        service_list_page.refresh();
    }
    urlBuilder.setOnChangeListener(callback);
    
    urlBuilder.setParameterOnChangeListener('offset', 
        pagination.setOnChangeListener.bind(pagination), 
        pagination.getPageNumber.bind(pagination));
    
});

