window.onload=function (){
    var userName="xiaoming";
    type = get_loadArticle_type();
    loadArticle(type,0,10);

}
$(document).ready(function(){
    var a,b,c;
    a = $(window).height();    //浏览器窗口高度
    // var group = $("div#article_list_body div.last").offset().top;
    $(window).scroll(function(){
        b = $(this).scrollTop();   //页面滚动的高度

        // c = group.offset().top;    //元素距离文档（document）顶部的高度
        console.log(a+'  '+b+'  '+$(document).height()+$("div#article_list_body div.last").offset());
        // console.log(c);
        // if(a+b>c){
        //     console.log('1123456')
        // }else{
        //     console.log('tttttttttttttttttttt')
        // }
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

function get_loadArticle_type() {
  pathname = window.location.pathname;
  if(pathname == "/blog/"){
      return -1;
    }else{
      var re = new RegExp('/blog/category/([0-9]*?)/');
      arr = re.exec(pathname);
      return arr[1]
  }
}

function loadArticle(type,index,num) {
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
            addArticleList(xmlhttp);
		}
	}
	xmlhttp.open("GET", "loadArticle/?num="+num+"&type="+type+"&index="+index, true);
	xmlhttp.send();
}
function appendItems(article_list) {
        for(var i=0;i<article_list.length;i++){
        $("div#article_list_body").append(html.Format(article_list[i]));
    }
}
function addArticleList(response) {
    var article_list = $.parseJSON(response.responseText).dataList;
    console.log(article_list);
    html='<div class="card" style="width: auto;">\
          <ul class="list-group list-group-flush">\
          <li class="list-group-item"><h4><a href="/blog/article/{id}">{title}</a></h4>\
            author:{author}&nbsp;&nbsp;创建时间:{create_time}</li>\
          </ul>\
        </div>\
        <br>';
    insertToArticleList(article_list,html);
    insertToArticleList(article_list,html);
    $("div#article_list").append("<br>");
}
function insertToArticleList(article_list,html) {
    var temp = 0;
    var timer = setInterval(function(){
        var i = temp;
         $("div#article_list_body").append(html.Format(article_list[i]));
         temp++;
         if(article_list.length <= temp){
             clearInterval(timer)
         }
    },80)
}





















