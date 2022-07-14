function changepass() {
    var oldpass = document.getElementById("oldpassword").value;
    var newpass1 = document.getElementById("newpassword").value;
    var newpass2 = document.getElementById("againpassword").value;
    console.log(oldpass,newpass1);
    $.ajax({
        "url" : "/changepass/",
        "type" : "post",
        "data" : '{"oldpass":"'+oldpass+'","newpass1":"'+newpass1+'","newpass2":"'+newpass2+'"}',
        "dataType" : "json",
        //如果成功请求执行以下流程
        "success" : function (json) {
            alert(json.errmsg);
        }
    })
}