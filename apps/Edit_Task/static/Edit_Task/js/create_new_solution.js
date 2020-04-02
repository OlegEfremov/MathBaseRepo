function create_new_solution(task_id){

    let send_data = {
        'task_id': task_id,
    };
    send_data = JSON.stringify(send_data);

    $.ajax({
        url: "create_new_solution",
        type: "POST",
        data: {'data': send_data},
        success: function(res) {
            show_tasks(taskid)
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}