$(function (){
    main();
});

function main() {
    $.ajax({
        "url" : "/userinfo/",
        "type" : "get",
        "data" : "",
        "dataType" : "json",
        //如果成功请求执行以下流程
        "success" : function (json) {
            var a = json[0].loginuser;
            var b = json[0].loginemail;
            //将用户名发送给input
            document.getElementById('userid').value = a;
            document.getElementById('emailid').value = b;
        }
    })
}


function changemail() {
    var emailvalue = document.getElementById("emailid").value;
    $.ajax({
        "url" : "/userinfo/",
        "type" : "post",
        "data" : '{"email":"'+emailvalue+'"}',
        "dataType" : "json",
        //如果成功请求执行以下流程
        "success" : function (json) {
            alert(json.errmsg);

        }
    })
}

