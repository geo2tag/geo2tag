var urlBuilder = undefined;

$(document).ready(function(){
    var pagination = new Pagination('service_list');
    pagination.initPagination(5, 20);

    var ownerId = new AutocompliteInput('owner_id', '/instance/user?login=' , 'login', '_id');
    var serviceName = $('#service_name');

    urlBuilder = new UrlBuilder('/instance/service?',  
        {'number':5, 'offset':0});
    urlBuilder.setParameterOnChangeListener('ownerId', 
        ownerId.setSelectListener.bind(ownerId), 
        ownerId.getInternalValue.bind(ownerId));

    urlBuilder.setParameterOnChangeListener('substring', 
        serviceName.keyup.bind(serviceName), 
        serviceName.val.bind(serviceName));


    urlBuilder.setOnChangeListener(function(){
        console.log(this.getUrl());
        service_page.model.url = this.getUrl();
        service_page.refresh();
    });
});

