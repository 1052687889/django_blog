$(document).ready(function(){
    $("#login").click(function(){
      console.log('login');
    });

    $("#register").click(function(){
      console.log('register');
    });
     $("#logout").click(function(){
         console.log('logout');
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
     $('#nav_blog').mouseenter(function () {
         $(this).addClass('show');
         $(this).children('div').addClass('show');
     });
     $('#nav_blog').mouseleave(function () {
         $(this).removeClass('show');
         $(this).children('div').removeClass('show');
     });
//    user_opt
     $('#user_opt').mouseenter(function () {
         console.log('111111111111111');
         item = $(this).children('ul').children('li');
         item.addClass('show');
         item.children('a').attr('aria-expanded','true');
         item.children('div').addClass('show')
         // $(this).children('div:last').addClass('show');
     });
     $('#user_opt').mouseleave(function () {
         console.log('22222222222222');
         item = $(this).children('ul').children('li');
         item.removeClass('show');
         item.children('a').attr('aria-expanded','false');
         item.children('div').removeClass('show')
         // $(this).removeClass('show');
         // $(this).children('div:last').removeClass('show');
     });

});

