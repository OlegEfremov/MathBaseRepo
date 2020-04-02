function save_task(task_id){

    let send_data = {
        'task_id': task_id,
        'new_body' : document.getElementById('id_body').value,
        'new_ans': document.getElementById('id_ans').value,
    };
    send_data = JSON.stringify(send_data);

    $.ajax({
        url: "save_task",
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