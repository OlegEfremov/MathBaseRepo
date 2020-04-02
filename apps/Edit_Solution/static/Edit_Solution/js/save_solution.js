function save_solution(sol_id){

    let send_data = {
        'sol_id': sol_id,
        'new_body' : document.getElementById('id_body').value,
        'new_name': document.getElementById('id_name').value,
    };
    send_data = JSON.stringify(send_data);

    $.ajax({
        url: "save_solution",
        type: "POST",
        data: {'data': send_data},
        success: function(res) {
            show_tasks(solid)
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}