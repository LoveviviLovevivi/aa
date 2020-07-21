$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault()
        var telephone_input = $("input[name='telephone']");
        var password_input = $("input[name='password']");
        remeber_input = $("inpunt[name='remeber']");

        var telephone = telephone_input.val();
        var password = password_input.val();
        var remeber = remeber_input.checked ? 1 : 0;
        zlajax.post({
            'url': '/signin/',
            'data': {
                'telephone': telephone,
                'password': password,
                'remeber': remeber
            },
            'success': function (data) {
                if(data['code']==200){
                    var return_to = $("#return_to_span").text();
                    if(return_to){
                        window.location = return_to;
                    }else{
                        window.location = '/';
                    }
                }else{
                    zlalert.alertInfo(data['message'])
                }


            }
        });
    });
});