function remove_task_from_cart(obj){
    let task_id = $(obj).closest('tr').attr('id');
    checkbox_values['checkbox_task_'+task_id] = false;

    $.ajax({
            url: 'get_list_of_sols_id_in_task',
            type: "POST",
            data: {'task_id': task_id},
            success: function(res) {
                var list_of_sols_id = res.split(',');
                console.log(list_of_sols_id);
                list_of_sols_id.forEach(function (sol_id, index) {
                    checkbox_values['checkbox_sol_' + sol_id] = false
                })
                document.getElementById('task'+task_id).remove();
                write_checkbox_values();
                $(obj).closest('tr').remove();
                renumber_table_rows();
            },
            error: function(ts) {
                console.log(ts)
            }
        });

    // all_tasks_all_sols_json[task_id].forEach(function (sol_id, index){
    //     checkbox_values['checkbox_sol_'+sol_id] = false
    // });
}

function renumber_table_rows() {
    for (var i=0; i<$('tr').length/2; i++){
        document.getElementById('order_number_'+$('tr')[i].id).innerHTML = '№'+(i+1).toString()
        document.getElementById('ans_order_number_task'+$('tr')[i].id).innerHTML = '№'+(i+1).toString()
    }
}