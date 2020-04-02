function up_down(node) {
        var tempScrollTop = $(document).scrollTop();
        var row = $(node).parents('tr:first');
        if ($(node).is('.up')) {
            if (row.index() !== 0){
                //renumber rows
                document.getElementById('order_number_'+row.attr('id')).innerHTML = '№' + row.index().toString();
                document.getElementById('order_number_'+row.prev('tr').attr('id')).innerHTML = '№'+(row.prev('tr').index()+2).toString();
                row.insertBefore(row.prev());

                var ans_row = $('#task'+row.attr('id'))
                document.getElementById('ans_order_number_'+ans_row.attr('id')).innerHTML = '№' + ans_row.index().toString();
                document.getElementById('ans_order_number_'+ans_row.prev('tr').attr('id')).innerHTML = '№'+(ans_row.prev('tr').index()+2).toString();
                ans_row.insertBefore(ans_row.prev());
            }
        } else {
            if (row.next('tr').length !== 0) {
                //renumber rows
                document.getElementById('order_number_' + row.attr('id')).innerHTML = '№' + (row.index() + 2).toString();
                document.getElementById('order_number_' + row.next('tr').attr('id')).innerHTML = '№' + (row.next('tr').index()).toString();
                row.insertAfter(row.next());

                var ans_row = $('#task'+row.attr('id'));
                document.getElementById('ans_order_number_' + ans_row.attr('id')).innerHTML = '№' + (ans_row.index() + 2).toString();
                document.getElementById('ans_order_number_' + ans_row.next('tr').attr('id')).innerHTML = '№' + (ans_row.next('tr').index()).toString();
                ans_row.insertAfter(ans_row.next());

            }
        }
        $(document).scrollTop(tempScrollTop);
        // return false
};

function export_folder(sol_folder_dbID){
    let send_data = {'sol_folder_dbID': sol_folder_dbID};
    // send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'GET',
        url: 'export_folder',
        data: send_data,
        // dataType: 'json',
        success: function(res){
            MathJax.Hub.Startup.onload();
            document.getElementById('table_of_tasks').innerHTML = '';
            document.getElementById('table_of_tasks').innerHTML = res;
            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);

        },
        error : function(error) {
            console.log('error');
            console.log(error)
        }
    });

}


    function show_hide_toggle(y, display_type = 'block') {
        for (var i=0; i<y.length; i++)
            {
                var x = y[i];
                if (x.style.display === "none") {
                    x.style.display = display_type;
                } else {
                    x.style.display = "none";
                }
            }
    }

    function download(){
        let tasks = $('.task'),
            sols = $('.solution'),
            another_sols = $('.another_solution');

        var list_of_tasks_id=[];
        for (var i=0; i<tasks.length;i++){
            list_of_tasks_id.push(tasks[i].id)
        }

        var list_of_sols_id=[];
        for (var i=0; i<sols.length;i++){
            list_of_sols_id.push(sols[i].id)
        }

        var list_of_another_sols_id=[];
        for (var i=0; i<another_sols.length;i++){
            list_of_another_sols_id.push(another_sols[i].id)
        }

        let checkboxes = $("input:checkbox"),
            checkbox_values = {};
        for (var i=0; i<checkboxes.length;i++){
            checkbox_values[checkboxes[i].id] = checkboxes[i].checked
        }

        let send_data = {
            'list_of_tasks_id': list_of_tasks_id,
            'list_of_sols_id': list_of_sols_id,
            'list_of_another_sols_id': list_of_another_sols_id,
            'checkbox_values': checkbox_values
        };
        send_data = JSON.stringify(send_data);
        $.ajax({
            type: 'GET',
            url: 'download_dynamic_text',
            data: {'data':send_data},
            // dataType: 'json',
            success: function(res){
                let contents = res;
                download_file('my_file.tex', contents)
            },
            error : function(error) {
                console.log('error');
            }
        });
    }


    function download_file(name, contents, mime_type) {
        mime_type = mime_type || "text/plain";

        var blob = new Blob([contents], {type: mime_type});

        var dlink = document.createElement('a');
        dlink.download = name;
        dlink.href = window.URL.createObjectURL(blob);
        dlink.onclick = function(e) {
            // revokeObjectURL needs a delay to work properly
            var that = this;
            setTimeout(function() {
                window.URL.revokeObjectURL(that.href);
            }, 1500);
        };
        dlink.click();
        dlink.remove();
    }


function show_tasks_cart(){
    let send_data = {'checkbox_values': checkbox_values};
    // send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'GET',
        url: 'show_tasks_cart',
        data: send_data,
        // dataType: 'json',
        success: function(res){

        },
        error : function(error) {
            console.log('error');
        }
    });

}

function remove_task_from_cart(obj){
    let task_id = $(obj).closest('tr').attr('id');
    checkbox_values['checkbox_task_'+task_id] = false;
    all_tasks_all_sols_json[task_id].forEach(function (sol_id, index){
        checkbox_values['checkbox_sol_'+sol_id] = false
    });
    sessionStorage.setItem('checkbox_values', JSON.stringify(checkbox_values));

    $(obj).closest('tr').remove()
}