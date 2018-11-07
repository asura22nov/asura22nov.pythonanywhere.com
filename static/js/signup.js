$(document).ready(function(){
    $("#btnSignUp").click(function() {
	alert("Hello");
	console.log("This is working so far");
        $.ajax({
            url: "/signup",
            data: $("form").serialize(),
            type: "POST",
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
