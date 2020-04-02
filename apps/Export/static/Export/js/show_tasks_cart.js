function show_tasks_cart(){
    let send_data = {'checkbox_values': checkbox_values};
    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: '../../export/show_tasks_cart',
        data: {'data': send_data},
        // dataType: 'json',
        success: function(res){
            res = compile_img_in_show_tasks(res)
            MathJax.Hub.Startup.onload();
            document.getElementById('tasks_cart').innerHTML = '';
            document.getElementById('tasks_cart').innerHTML = res;
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        },
        error : function(error) {
            console.log('error');
        }
    });

}
