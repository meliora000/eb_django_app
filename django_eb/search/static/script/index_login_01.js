// default setting
function getstatus(){
$.get('../user/status',$(this).serialize(),function(data){
	if(data.login.status == "login"){
		login();
		setUsername("WELCOME! " + data.login.name+"님");
	}
	else{
		showLogin();
		hideLogout();
		hiderUsername();
	}
});
}

getstatus();


var loginstatus = "needLogin"

// when user click login
$('.login').toggle(function(){
   showLoginForm();
},function(){
	hideLoginForm();
});
// whe user click login - animate
function hideLoginForm(){
	$('#loginpage').animate({height:'0px',width:'0px'},300);
}
function showLoginForm(){
	$('#loginpage').animate({height:'200px',width:'230px'},300);
}

function login(){
		hideLogin();
		showLogout();
		hideLoginForm();
		showUsername();
		loginstatus = "LOGIN"
}
// when user click login - submit
$('#loginform').submit(function(e){
	$.post('../user/login/', $(this).serialize(), function(data){
	       $(".message").text(data.message.id + " <> " + data.message.password);
	       if(data.message.status == "login"){
				login();
				setUsername("WELCOME! " + data.message.userName+"님");
	       }
	       if(data.message.status == "id"){
				alert("NO ID SIGNUP PLEASE")
	       }
	       if(data.message.status == "password"){
				alert("PASSWORD IS NOT RIGHT")
	       }
       // of course you can do something more fancy with your respone
    });
    e.preventDefault();
	})

// when user click login - signup
$('#signup').click(function(){
    window.location = '/user/signup'
});
// when user click logout
$('.logout').click(function(){
	hiderUsername();
	hideLogout();
	showLogin();
	loginstatus = "needLogin"
	$.get('../user/logout',$(this).serialize(),function(data){
	});
	});

// when user click favorite
$('.favorite').click(function(){
	if(loginstatus == "needLogin"){
		alert("LOGIN FIRST")
	}
	else{
		window.location = '../favorite'
	}
})


function hideLogin(){
	$('.login').hide();
}
function showLogin(){
	$('.login').show();
}


function hideLogout(){
	$('.logout').hide();
}
function showLogout(){
	$('.logout').show();
}

function hiderUsername(){
	$('.username').hide();
}
function showUsername(){
	$('.username').show();
}
function setUsername(x){
	$('.username').text(x);
}
