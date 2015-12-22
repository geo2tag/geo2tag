var urlBuilder = undefined;
var pagination = undefined;

var SERVICES_PER_PAGE = 5;

$(document).ready(function(){
    pagination = new Pagination('service_list');

    var ownerId = new AutocompliteInput('owner_id', '/instance/user?login=' , 'login', '_id');

    var serviceName = $('#service_name');

    urlBuilder = new UrlBuilder('/instance/service?',  
        {'number':SERVICES_PER_PAGE, 'offset':0});
    urlBuilder.setParameterOnChangeListener('ownerId', 
        ownerId.setSelectListener.bind(ownerId), 
        ownerId.getInternalValue.bind(ownerId));

    urlBuilder.setParameterOnChangeListener('substring', 
        serviceName.keyup.bind(serviceName), 
        serviceName.val.bind(serviceName));

    urlBuilder.setParameterOnChangeListener('offset',
        pagination.setOnChangeListener.bind(pagination),
        pagination.getOffsetValue.bind(pagination));

    urlBuilder.setOnChangeListener(refreshServiceList);

    refreshServiceList();
     
});

// SHOULD BE reused as a part of Pagination macros
function refreshServiceList(){
    var url = urlBuilder.getUrl();
    console.log(url);
    calculateListRequestLength(url, function (length){
        var offset = undefined;
        if (pagination.isPageNumberChanged(length, SERVICES_PER_PAGE)){
            offset = pagination.initPagination(length, SERVICES_PER_PAGE);
        }
        service_page.model.url = urlBuilder.getUrl(offset);
        service_page.refresh();
    }, function(){});
}
