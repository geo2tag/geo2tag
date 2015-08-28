function getPointPopupHtml(point){
	var JSON = 'json';
	var IMAGE_URL = 'image_url'
	var NAME = 'name';
	var DESCRIPTION = 'description';
	var SOURCE_URL = 'source_url';
	var text;
	var image_url = point[JSON][IMAGE_URL];
	var name = point[JSON][NAME];
	var description = point[JSON][DESCRIPTION];
	var source_url = point[JSON][SOURCE_URL];
	var text_img = '<img src="' + image_url + '" width="50" height="50">';
	var text_name = '<b>  Name:</b>' + name  + '<br>';
	var text_description = '<b>  Description:</b>' + description + '<br>';
	var text_source = '<b>  Source_url:</b><a href="' + source_url + '">' + source_url + '</a><br>';
	text = '<table><tr><td>' + text_img + '</td>' + '<td>' + text_name + text_description + text_source + '</td></tr></table>';
	return text;
}