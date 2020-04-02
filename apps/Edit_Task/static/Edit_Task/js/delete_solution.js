function delete_solution(sol_id){

    let send_data = {
        'sol_id': sol_id,
    };
    send_data = JSON.stringify(send_data);

    $.ajax({
        url: "delete_solution",
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