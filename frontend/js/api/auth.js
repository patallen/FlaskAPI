define(["jquery"],
    function($){
        var self = {};
        self.getAuthToken = function(username, password){
            $.ajax({
                url: "http://api.flaskapi.dev/authenticate/",
                method: "POST",
                data: {
                    "username": username,
                    "password": password
                }
            }).done(function(res){
                var token = res;
                if (token){
                    localStorage.setItem("flaskapitoken", "Bearer " + token);
                    console.log(token)
                }
            }).fail(function(res){
                var error = res.responseText;
                console.log(error);
                return error;
            });
        }
        return self;
});
