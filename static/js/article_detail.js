
$(document).ready(function(){

    $("#submit_comment_button").click(function () {
        var re = new RegExp('/blog/article/([0-9]*?)/');
        arr = re.exec(window.location.pathname);
        res = $("#textarea1").val();
        console.log();
        $.post("/blog/comment/",{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
			id:arr[1],
			comment:"http://www.runoob.com"
		},
		function(data,status){
			console.log("数据: \n" + data + "\n状态: " + status);
		});
    });
    var topbtn = document.getElementById("btn");
    var timer = null;//<br>    //获取屏幕的高度
    var pagelookheight = document.documentElement.clientHeight;

    window.onscroll = function(){
        //滚动超出高度，显示按钮，否则隐藏
        var backtop = document.body.scrollTop;//<br>           //  滚动超过一频    应该显示
        if(backtop >= pagelookheight){
            topbtn.style.display = "block";
        }//<br>      //   不显示<br>
        else{
            topbtn.style.display = "none";
        }
    }

    topbtn.onclick = function () {//<br>
    timer = setInterval(function () {
            var backtop = document.body.scrollTop; // <br>              //速度操作  减速
            var speedtop = backtop/5;
            document.body.scrollTop = backtop -speedtop;  //高度不断减少
            if(backtop ==0){  //滑动到顶端
                clearInterval(timer);  //清除计时器
            }
        }, 30);
    }
//     $(window).scroll(function () {
//     st = Math.max(document.body.scrollTop || document.documentElement.scrollTop);
//     if(st > fixedbox.offset().top){
//         fixedbox.addClass("fixedbox-on");
//     }
//     if(st < fixedlocation){
//         fixedbox.removeClass("fixedbox-on");
//     }
// });
});

