LOAD_ARTICLE_NUM=10;
LOAD_INDEX=0;
LOAD_ARTICLE_END=false;

window.onload=function (){
    loadArticle(get_loadArticle_type(),LOAD_INDEX,LOAD_ARTICLE_NUM);
}

$(window).scroll(function(){
 var scrollTop = $(this).scrollTop();    //滚动条距离顶部的高度
 var scrollHeight = $(document).height();   //当前页面的总高度
 var clientHeight = $(this).height();    //当前可视的页面高度
 if(scrollTop + clientHeight >= scrollHeight){   //距离顶部+当前高度 >=文档总高度 即代表滑动到底部
     console.log("滚动条到达底部");
     if(LOAD_ARTICLE_END==false && LOAD_INDEX != 0){
         loadArticle(get_loadArticle_type(),LOAD_INDEX,LOAD_ARTICLE_NUM);
     }
 }else if(scrollTop<=0){
	 console.log("滚动条到达顶部")
 }
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
    console.log("loadArticle:"+type+' '+index+' '+num);
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

function addArticleList(response) {
    var article_list = $.parseJSON(response.responseText).dataList;
    console.log(article_list);
    if(article_list.length < LOAD_ARTICLE_NUM){
        LOAD_ARTICLE_END=true;
    }
    if(article_list.length){
        LOAD_INDEX+=article_list.length;
        html='<div class="card" style="width: auto;">\
          <ul class="list-group list-group-flush">\
          <li class="list-group-item"><h4><a href="/blog/article/{id}">{title}</a></h4>\
            author:{author}&nbsp;&nbsp;创建时间:{create_time}type:{type}<br>postCon:{postCon}&hellip;</li>\
          </ul>\
        </div>\
        <br>';
    insertToArticleList(article_list,html);
    $("div#article_list").append("<br>");
    }

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
    },50)
}





















