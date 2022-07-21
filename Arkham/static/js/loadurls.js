function load() {
    var a = document.getElementById('remark').value;
    const b = a.split("\n");
    var json = {};
    for (var i=0;i<a.length;i++){
        json[i]=b[i];
    }
    c = JSON.stringify(json);
    console.log(b);
    console.log(c);
    send(c)
}

function send(urls) {
    $.ajax({
        "url" : "/addurls/",
        "type" : "post",
        "data" : urls,
        "dataType" : "json",
        //如果成功请求执行以下流程
        "success" : function (json) {
            alert(json.errmsg+'\n'+'成功添加:'+'\n'+json.addurls+'\n'+'错误子域名:'+'\n'+json.errorurls+'\n'+'重复子域名:'+'\n'+json.checkurls);
        }
    })

}