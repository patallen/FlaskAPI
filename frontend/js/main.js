define(["jquery", "api/auth"],
    function($, Auth){
        $("body").css("background", "black");
        var res = Auth.getAuthToken("pat", "bandit");
        console.log(res);
})
