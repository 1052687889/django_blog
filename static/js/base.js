$(document).ready(function(){
     $("#logout").click(function(){
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
         item = $(this).children('ul').children('li');
         item.addClass('show');
         item.children('a').attr('aria-expanded','true');
         item.children('div').addClass('show');
     });
     $('#user_opt').mouseleave(function () {
         item = $(this).children('ul').children('li');
         item.removeClass('show');
         item.children('a').attr('aria-expanded','false');
         item.children('div').removeClass('show');
     });
//当滚动条的位置处于距顶部100像素以下时，跳转链接出现，否则消失
        $(function () {
            $(window).scroll(function(){
                if ($(window).scrollTop()>100){
                    $("#back-to-top").fadeIn(1000);
                }
                else
                {
                    $("#back-to-top").fadeOut(1000);
                }
            });

            //当点击跳转链接后，回到页面顶部位置
            $("#back-to-top").click(function(){
                if ($('html').scrollTop()) {
                    $('html').animate({ scrollTop: 0 }, 100);//动画效果
                    return false;
                }
                $('body').animate({ scrollTop: 0 }, 100);
                return false;
            });
        });

});
/*自定义字符串格式化*/
String.prototype.Format = function (args) {
    /*this代表要调用Format方法的字符串*/
    /*replace的第一个参数为正则表达式，g表示处理匹配到的所有字符串，在js中使用//包起来*/
    /*replace的第二个参数为匹配字符串的处理，k1匹配结果包含{}，k2只保留{}内的内容*/
    var temp = this.replace(/\{(\w+)\}/g, function (k1, k2) {
    // console.log(k1, k2);
    /*replace将匹配到的k2用参数args替换后赋给新变量temp*/
    return args[k2];
    });
    /*自定义方法Format将格式化后的字符串返回*/
    return temp;
}

