$(document).ready(function() {
   show_tasks(taskid);
});

function show_tasks(task_id){

    let send_data = {
        'task_id' : task_id
    };
    send_data = JSON.stringify(send_data);

    $.ajax({
        url: "show_tasks",
        type: "GET",
        data: {'data': send_data},
        success: function(res) {
            MathJax.Hub.Startup.onload();
            res = compile_img_in_show_tasks(res);
            document.getElementById('table_of_tasks').innerHTML = '';
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}
