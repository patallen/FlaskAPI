define(["jquery"],
    function($){
        var self = {};
        self.getAuthToken = function(username, password){
            $.ajax({
                url: "http://localhost:5000/authenticate/",
                method: "POST",
                data: {
                    "username": username,
                    "password": password
                }
            }).done(function(res){
                var token = res;
                if (token){
                    localStorage.setItem("flaskapitoken", "Bearer " + token);
                }
            });
        }
        return self;
});
