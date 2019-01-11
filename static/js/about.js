function zan_onclick() {

  	var xmlhttp;
	if (window.XMLHttpRequest) {
		//  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
		xmlhttp=new XMLHttpRequest();
	}
	else {
		// IE6, IE5 浏览器执行代码
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
		    var zan_num = $.parseJSON(xmlhttp.responseText).zan_num;
            zan_num_item = $("#zan_num");
            zan_num_item.text(zan_num);
		}
	}
	xmlhttp.open("GET", "zan/", true);
	xmlhttp.send();
}
