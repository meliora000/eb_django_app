$('#loginform').submit(function(e){
	$.post('user/login/', $(this).serialize(), function(data){
	       $(".message").text(data.message.id + " <> " + data.message.password);
       // of course you can do something more fancy with your respone
    });
    e.preventDefault();
	})
	$('.login').toggle(function(){
	    $('#loginpage').animate({height:'200px',width:'280px'},300);
	},function(){
	     $('#loginpage').animate({height:'0px',width:'0px'},300);
	});

$('#signup').click(function(){
    window.location = '/user/signup'
});