$(document).ready(function(){

    $("#login").click(function(){
      console.log('login');
    });

    $("#register").click(function(){
      console.log('register');
    });
     $("#logout").click(function(){
         console.log('logout');
         console.log(window.location.host+"/users/logout");
         // response = $.ajax({url:window.location.host+"/users/logout",async:false});
         // console.log(response)
        var xmlhttp;
        if (window.XMLHttpRequest) {
            xmlhttp=new XMLHttpRequest();
        }
        else {
            xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                window.location.reload();
            }
        }
        xmlhttp.open("GET", window.location.host+"/users/logout/?url=?", true);
        xmlhttp.send();
    });
    // $(".dropdown").mouseover(function () {
    //         $(this).addClass("show");
    //         $('.dropdown-toggle')
    // });
    // // $(".dropdown-menu").mouseover(function () {
    // //         $(this).addClass("show");
    // // });
    // $(".dropdown").mouseleave(function () {
    //     $(this).removeClass("show");
    // });
    // $(".dropdown-menu").mouseleave(function () {
    //     $(this).removeClass("show");
    // });
});

// function request() {
//   	var xmlhttp;
// 	if (window.XMLHttpRequest) {
// 		xmlhttp=new XMLHttpRequest();
// 	}
// 	else {
// 		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
// 	}
// 	xmlhttp.onreadystatechange=function() {
// 		if (xmlhttp.readyState==4 && xmlhttp.status==200)
// 		{
//             location.reload();
// 		}
// 	}
// 	xmlhttp.open("GET", window.location.host+"users/logout"+url, true);
// 	xmlhttp.send();
// }
