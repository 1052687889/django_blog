LOAD_ARTICLE_NUM=10;
LOAD_INDEX=0;
LOAD_ARTICLE_END=false;
TYPE='type';
TAG='tag';
DATE='date';
link_type = get_link_type();

window.onload=function (){
    console.log(link_type);

    loadArticle()
}

$(window).scroll(function(){
 var scrollTop = $(this).scrollTop();    //滚动条距离顶部的高度
 var scrollHeight = $(document).height();   //当前页面的总高度
 var clientHeight = $(this).height();    //当前可视的页面高度
 if(scrollTop + clientHeight >= scrollHeight){   //距离顶部+当前高度 >=文档总高度 即代表滑动到底部
     console.log("滚动条到达底部");
     if(LOAD_ARTICLE_END==false && LOAD_INDEX != 0){
         loadArticle();
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

function get_link_type() {
    try{
        pathname = window.location.pathname;
        if(pathname == "/blog/"){
            return TYPE;
        }
        var re = new RegExp('/blog/category/([0-9]*?)/');
        arr = re.exec(pathname);
        if(arr[1])
            return TYPE;
    }catch(e){}

    try{
        var re = new RegExp('/blog/tag/([0-9]*?)/');
        arr = re.exec(pathname);
         if(arr[1])
            return TAG
    }catch(e){}

    try{
        var re = new RegExp('/blog/date/([0-9]*?)/([0-9]*?)/');
        arr = re.exec(pathname);
        console.log(arr);
         if(arr[1])
            return DATE
    }catch(e){}
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
function get_loadArticle_tag() {
  pathname = window.location.pathname;
  try{
      var re = new RegExp('/blog/tag/([0-9]*?)/');
      arr = re.exec(pathname);
      return arr[1]
  }catch (e) {}
}
function get_loadArticle_year_month() {
  pathname = window.location.pathname;
  try{
      var re = new RegExp('/blog/date/([0-9]*?)/([0-9]*?)/');
      arr = re.exec(pathname);
      return {'year':arr[1],'month':arr[2]}
  }catch (e) {}
}
function parseParams(data) {
    try {
        var tempArr = [];
        for (var i in data) {
            var key = encodeURIComponent(i);
            var value = encodeURIComponent(data[i]);
            tempArr.push(key + '=' + value);
        }
        var urlParamsStr = tempArr.join('&');
        return urlParamsStr;
    } catch (err) {
        return '';
    }
}
function get_param() {
    var param;
    if(link_type==TYPE){
        param={'link_type':link_type,
                'type':get_loadArticle_type(),
                'index':LOAD_INDEX,
                'num':LOAD_ARTICLE_NUM};

    }else if(link_type==TAG){
        param={ 'link_type':link_type,
                'tag':get_loadArticle_tag(),
                'index':LOAD_INDEX,
                'num':LOAD_ARTICLE_NUM};
    }else if(link_type==DATE){
        d = get_loadArticle_year_month();
        param={ 'link_type':link_type,
                'year':d['year'],
                'month':d['month'],
                'index':LOAD_INDEX,
                'num':LOAD_ARTICLE_NUM};
    }
    return param
}
function loadArticle() {
    var param = get_param();
    console.log("loadArticle:"+param);
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
	url = parseParams(param);
	xmlhttp.open("GET", "loadArticle/?"+url, true);
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
        html='<div class="card shadow-lg" style="width: auto;hight:100;">\
          <ul class="list-group list-group-flush">\
          <li class="list-group-item">\
          <div class="row">\
                <div class="col-2">\
                    <div class="article_img">\
                        <a href="/blog/article/{id}" class="badge">\
                            <img src="{image}" style="width: 100%;height: auto;" alt="">\
                        </a>\
                    </div>\
                </div>\
                <div class="col-10">\
                <a href="/blog/article/{id}" class="badge"><h4>{title}</h4> </a>                    \
                   <h6>\
                       <div class="row">\
                           <div class="col-3">作者:&nbsp;{author}</div>\
                           <div class="col-5">时间:&nbsp;{create_time}</div>\
                           <div class="col-4">阅读数:&nbsp;{read_num}</div>\
                       </div>\
                   </h6>\
                   <h6>\
                   <div class="row">\
                        <div class="col-3">类型:&nbsp;{type}</div>\
                        <div class="col-9">标签:&nbsp;{tag}</div>\
                   </div>\
                    </h6>\
                    <div style="width: 100%;height: auto;" >摘要:&nbsp;&nbsp;&nbsp;{postCon}&hellip;</div>\
                    </div>\
            </div>\
                      </li>\
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
    },80)
}





















