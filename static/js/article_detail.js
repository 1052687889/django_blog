
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
			comment:$("#textarea1").val()
		},
		function(data,status){
            var t = $("p:contains(暂无评论,敬请期待.)");
            if(t){
                t.remove();
            }
             $("div#comment_display").append(data);
		});
    });
});
