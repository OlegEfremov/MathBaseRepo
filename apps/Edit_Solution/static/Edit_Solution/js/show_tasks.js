$(document).ready(function() {
   show_tasks(solid);
});

function show_tasks(sol_id){

    let send_data = {
        'sol_id' : sol_id
    };
    send_data = JSON.stringify(send_data);

    $.ajax({
        url: "show_tasks",
        type: "GET",
        data: {'data': send_data},
        success: function(res) {
            res = compile_img_in_show_tasks(res)
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}
