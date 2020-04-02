$(document).ready(function() {
   $(document).on("change", ":input[type=number]", function () {
        order_numbers[this.id.replace('order_number_','')] = this.value;
    });
});

function reorder_tasks(dbID, page, url){

    let send_data = {
        'solution_folder_dbID' : dbID,
        'order_numbers': order_numbers
    };
    send_data = JSON.stringify(send_data);

    $.ajax({
        url: 'reoder_tasks',
        type: "POST",
        data: {'data': send_data},
        success: function(res) {
            show_tasks(dbID, page, url);
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}

function set_order_numbers(){
    let e = document.getElementById('tasks_order').innerHTML;
    if (e !== '') {
        let tasks_order = JSON.parse(e);

        for (const item of ($(':input[type=number]'))) {
            item.value = tasks_order[item.id.replace('order_number_', '')]
        }
    }
}
