function getPointPopupHtml(point){
	var text;
	var JSON = 'json';
	var IMAGE_URL = 'image_url'
	var NAME = 'name';
	var DESCRIPTION = 'description';
	var SOURCE_URL = 'source_url';
	if(point[JSON] != null){
		var image_url = point[JSON][IMAGE_URL] != null ? '<img src="' + point[JSON][IMAGE_URL] + '" width="50" height="50">': 'No image';
		var name = point[JSON][NAME] != null ? point[JSON][NAME] : ' - ';
		var description = point[JSON][DESCRIPTION] != null ? point[JSON][DESCRIPTION]: ' - ';
		var source_url = point[JSON][SOURCE_URL] != null ? '<a href="' + point[JSON][SOURCE_URL] + '">' + point[JSON][SOURCE_URL] + '</a>' : ' - ';
		var text_img = image_url;
		var text_name = '<b>  Name:</b>' + name  + '<br>';
		var text_description = '<b>  Description:</b>' + description + '<br>';
		var text_source = '<b>  Source_url:</b>' + source_url + '<br>';
		text = '<table><tr><td>' + text_img + '</td>' + '<td>' + text_name + text_description + text_source + '</td></tr></table>';
	}else{
		text = "<b>" + point['_id']['$oid'] + "</b>";
	}
	return text;
}