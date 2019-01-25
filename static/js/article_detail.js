$.ajaxSetup({
  beforeSend: function(xhr, settings){
      var csrftoken = $.cookie('csrftoken');
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});
$(document).ready(function(){

    $("#submit_comment_button").click(function () {
        var re = new RegExp('/blog/article/([0-9]*?)/');
        arr = re.exec(window.location.pathname);
        console.log(arr[1]);
        // xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
        // var csrftoken = Cookies.get('csrftoken');
        // xhr.setRequestHeader("X-CSRFToken", csrftoken);
        $.post("/blog/comment",{
            csrfmiddlewaretoken: Cookies.get('csrftoken'),
			id:arr[1],
			comment:"http://www.runoob.com"
		},
		function(data,status){
			console.log("数据: \n" + data + "\n状态: " + status);
		});
    })
});

