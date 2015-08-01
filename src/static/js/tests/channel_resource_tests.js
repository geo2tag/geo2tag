var test_data_channel_resource = {
    'GET':{
        url : getUrlWithPrefix('/service/testservice/channel/558807a47ec8ff5da755ee49')
    },
    'PUT':{
        data: {'name': 'test_channel_GT-1389_2'},
        url : getUrlWithPrefix('/service/testservice/channel/558807a47ec8ff5da755ee49')
    },
    'DELETE':{
        url : getUrlWithPrefix('/service/testservice/channel/'),
        id: ''
    }
};

QUnit.test( 'PUT' + test_data_channel_resource.PUT.url + JSON.stringify(test_data_channel_resource.PUT.data),
    function( assert ) { 
    var done = assert.async();
    var putCallbackFail = function() {
        assert.ok(false, 'ChannelResource put failed' );
        done();
    }; 
    var putCallbackSuccess = function() {
        assert.ok(true, 'ChannelResource put success' );
        done();
    };
    $.put(test_data_channel_resource.PUT.url, test_data_channel_resource.PUT.data )
        .fail(putCallbackFail).done(putCallbackSuccess);
    
    });

QUnit.test('GET' + test_data_channel_resource.GET.url, function( assert ) {
    var done = assert.async();
    var getCallbackFail = function() {
        assert.ok(false, 'ChannelResource get failed' );
        done();
    };
    var getCallbackSuccess = function() {
        assert.ok(true, 'ChannelResource get success' );
        done();
    };
    $.get(test_data_channel_resource.GET.url, test_data_channel_resource.GET.data )
        .fail(getCallbackFail).done(getCallbackSuccess);
 
});

var channelToDelete = {
    'POST':{
        data:{'name': 'chanelToDelete', 'json': "{'1': 2, '2': '4'}"},
        url : getUrlWithPrefix('/service/testservice/channel')
    }
};


QUnit.test('DELETE '+test_data_channel_resource.DELETE.url + test_data_channel_resource.DELETE.id, function( assert ) {
   var done = assert.async();
   $.post(channelToDelete.POST.url,channelToDelete.POST.data)
   .done(function(newObjectId){
        console.log(newObjectId);
        if(newObjectId != null)
            test_data_channel_resource.DELETE.url += newObjectId["$oid"];
        console.log(test_data_channel_resource);
       
    var deleteCallbackFail = function() {
           assert.ok(false, 'ChannelResource delete failed' );
           done();
       };
       var deleteCallbackSuccess = function() {
           assert.ok(true, 'ChannelResource delete success' );
           done();
       };
       console.log(test_data_channel_resource.DELETE.id);
       $.delete(test_data_channel_resource.DELETE.url)
       .fail(deleteCallbackFail).done(deleteCallbackSuccess);
    
   }).fail(function(){
          console.log("fail happened");
          assert.ok(false, 'Post channel for delete failed' );
          done();    
   })

});

