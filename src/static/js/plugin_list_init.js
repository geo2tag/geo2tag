var pagination = undefined;
var length = 5
var PLUGINS_PER_PAGE = 5;

$(document).ready(function(){
    pagination = new Pagination('plugin_list');
    pagination.initPagination(length, PLUGINS_PER_PAGE);
});

