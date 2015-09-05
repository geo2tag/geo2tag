var data_test_1 = {
    '_id' : {'$oid' : 'test_id_point'},
    'json' : { "name" : "test_GT-1567", "description" : "test_GT-1567", "image_url" : "http://www.dunbartutoring.com/wp-content/themes/thesis/rotator/sample-1.jpg","source_url" : "http://geo2tag.com/"}
}
var data_test_2 = {
    'json' : { "description" : "test_GT-1567", "image_url" : "http://www.dunbartutoring.com/wp-content/themes/thesis/rotator/sample-1.jpg","source_url" : "http://geo2tag.com/"}
}
var data_test_3 = {
    'json' : { "name" : "test_GT-1567", "image_url" : "http://www.dunbartutoring.com/wp-content/themes/thesis/rotator/sample-1.jpg","source_url" : "http://geo2tag.com/"}
}
var data_test_4 = {
    'json' : { "name" : "test_GT-1567", "description" : "test_GT-1567", "image_url" : "http://www.dunbartutoring.com/wp-content/themes/thesis/rotator/sample-1.jpg"}
}
var data_test_5 = {
    'json' : { "name" : "test_GT-1567", "description" : "test_GT-1567", "source_url" : "http://geo2tag.com/"}
}
var data_test_6 = {
    'json' : { "name" : "test_GT-1567", "source_url" : "http://geo2tag.com/"}
}
var result_1 = '<table><tr><td><img src="http://www.dunbartutoring.com/wp-content/themes/thesis/rotator/sample-1.jpg" width="50" height="50"></td><td><b>  Name:</b> test_GT-1567<br><b>  Description:</b> test_GT-1567<br><b>  Source_url:</b> <a href="http://geo2tag.com/">http://geo2tag.com/</a><br></td></tr></table>';
var result_2 = '<table><tr><td><img src="http://www.dunbartutoring.com/wp-content/themes/thesis/rotator/sample-1.jpg" width="50" height="50"></td><td><b>  Name:</b>  - <br><b>  Description:</b> test_GT-1567<br><b>  Source_url:</b> <a href="http://geo2tag.com/">http://geo2tag.com/</a><br></td></tr></table>';
var result_3 = '<table><tr><td><img src="http://www.dunbartutoring.com/wp-content/themes/thesis/rotator/sample-1.jpg" width="50" height="50"></td><td><b>  Name:</b> test_GT-1567<br><b>  Description:</b>  - <br><b>  Source_url:</b> <a href="http://geo2tag.com/">http://geo2tag.com/</a><br></td></tr></table>';
var result_4 = '<table><tr><td><img src="http://www.dunbartutoring.com/wp-content/themes/thesis/rotator/sample-1.jpg" width="50" height="50"></td><td><b>  Name:</b> test_GT-1567<br><b>  Description:</b> test_GT-1567<br><b>  Source_url:</b>  - <br></td></tr></table>';
var result_5 = '<table><tr><td>No image</td><td><b>  Name:</b> test_GT-1567<br><b>  Description:</b> test_GT-1567<br><b>  Source_url:</b> <a href="http://geo2tag.com/">http://geo2tag.com/</a><br></td></tr></table>';
var result_6 = '<table><tr><td>No image</td><td><b>  Name:</b> test_GT-1567<br><b>  Description:</b>  - <br><b>  Source_url:</b> <a href="http://geo2tag.com/">http://geo2tag.com/</a><br></td></tr></table>';
var result_no_json = '<b>test_id_point</b>';
QUnit.test( 'Test point popup html', function( assert ) {
    var test_popup = function(data,result){
        assert.ok(getPointPopupHtml(data) == result,'Okay');
    }
    test_popup(data_test_1,result_1);
    test_popup(data_test_2,result_2);
    test_popup(data_test_3,result_3);
    test_popup(data_test_4,result_4);
    test_popup(data_test_5,result_5);
    test_popup(data_test_6,result_6);
    delete data_test_1['json'];
    test_popup(data_test_1,result_no_json);
});
