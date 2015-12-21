var urlBuilder = undefined;

$(document).ready(function(){
    var pagination = new Pagination('service_list');
    pagination.initPagination(20, 5);
    var ownerId = new AutocompliteInput('owner_id', '/instance/user?number=5&login=' , 'login', '_id');
    var serviceName = $('#service_name');

    urlBuilder = new UrlBuilder('/instance/service?',  
        {'number':5, 'offset':0});
    urlBuilder.setParameterOnChangeListener('owner_id', 
        ownerId.setSelectListener.bind(ownerId), 
        ownerId.getExternalValue.bind(ownerId));

    urlBuilder.setParameterOnChangeListener('substring', 
        serviceName.keyup.bind(serviceName), 
        serviceName.val.bind(serviceName));

    urlBuilder.setParameterOnChangeListener('offset',
        pagination.setOnChangeListener.bind(pagination),
        pagination.getPageNumber.bind(pagination));

    urlBuilder.setOnChangeListener(function(){
        console.log(this.getUrl());
        service_page.model.url = this.getUrl();
        service_page.refresh();
    });
});

