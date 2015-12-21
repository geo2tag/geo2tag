var urlBuilder = undefined;

$(document).ready(function(){
    var pagination = new Pagination('service_list');
    pagination.initPagination(5, 20);

    var ownerId = new AutocompliteInput('owner_id', '/instance/user?number=5&login=' , 'login', '_id');
    var serviceName = $('#service_name');

    urlBuilder = new UrlBuilder('/instance/service?',  
        {'number':5, 'offset':0});
    urlBuilder.setParameterOnChangeListener('owner_id', 
        ownerId.setSelectListener.bind(ownerId), 
        ownerId.getExternalValue.bind(ownerId));

    urlBuilder.setParameterOnChangeListener('service_name', 
        serviceName.keyup.bind(serviceName), 
        serviceName.val.bind(serviceName));


    urlBuilder.setOnChangeListener(function(){
        console.log(this.getUrl());
        service_page.model.url = this.getUrl();
        service_page.refresh();
    });
});

