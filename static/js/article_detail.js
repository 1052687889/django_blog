$(document).ready(function(){
    $("#textarea1").emojioneArea();
    $(".comment_content p, .reply_content p").each(function(){
    var value = $(this).text();
    var code = $('<div/>').text(value).html(); //html转义
    $(this).html(emojione.toImage(code));
});
    $("#submit_comment_button").click(function () {
        var re = new RegExp('/blog/article/([0-9]*?)/');
        arr = re.exec(window.location.pathname);
        res = $("#textarea1").val();
        console.log();
        $.post("/blog/comment/",{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
			id:arr[1],
			comment:emojione.toImage($("#textarea1").val())
		},
		function(data,status){
            var t = $("p:contains('暂无评论,敬请期待.')");
            if(t){
                t.remove();
            }
            console.log(data);
             $("div#comment_display").append(data);

		});
        $("#textarea1").next().children("div.emojionearea-editor").html('');
    });
    $(document).on('click',"a[id^='comment_']",function (e) {
            var zan_num = RegExp('点赞\\(([0-9]*?)\\)$').exec(e.target.text)[1];
            var comment_id = RegExp('comment_([0-9]*?)$').exec(e.target.id)[1];
            var article_id = RegExp('/blog/article/([0-9]*?)/').exec(window.location.pathname)[1];
            $.get('comment/zan'+'?comment_id='+comment_id+'&zan_num='+zan_num+'&article_id='+article_id,function (data,status) {
                e.target.text = '点赞('+data.zan_num+')'
            })
        })
});
