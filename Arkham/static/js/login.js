function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    console.log(username+','+password);
    $.ajax({
        "url" : "/login/",
        "type" : "post",
        "data" : '{"username":"'+username+'","password":"'+password+'"}',
        "dataType" : "json",
        //如果成功请求执行以下流程
        "success" : function (json) {
            if(json.code===500){
                alert(json.errmsg);
            }else {
                // alert(json.errmsg);
                window.location.href='/';
            }
        }
    })
}