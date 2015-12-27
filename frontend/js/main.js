define(["jquery", "api/auth"],
    function($, Auth){
        Auth.getAuthToken("pat", "bandit");
});
