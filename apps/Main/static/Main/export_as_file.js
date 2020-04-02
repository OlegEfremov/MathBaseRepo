function get_list_of_tasks_id(){
    let tasks = $('.task');

    var list_of_tasks_id=[];
    for (var i=0; i<tasks.length;i++){
        list_of_tasks_id.push(tasks[i].id)
    }
    return list_of_tasks_id
}

function get_list_of_sols_id(){
    let sols = $('.solution');

    var list_of_sols_id=[];
    for (var i=0; i<sols.length;i++){
        list_of_sols_id.push(sols[i].id)
    }
    return list_of_sols_id
}

function get_list_of_another_sols_id(){
    let another_sols = $('.another_solution');

    var list_of_another_sols_id=[];
    for (var i=0; i<another_sols.length;i++){
        list_of_another_sols_id.push(another_sols[i].id)
    }

    return list_of_another_sols_id
}

function get_checkbox_values(){
    let checkboxes = $("input:checkbox"),
        checkbox_values = {};
    for (var i=0; i<checkboxes.length;i++){
        checkbox_values[checkboxes[i].id] = checkboxes[i].checked
    }
    return checkbox_values
}


function export_page_as_file(file_type){
    var data = {
                'list_of_tasks_id': get_list_of_tasks_id(),
                'list_of_sols_id': get_list_of_sols_id(),
                'list_of_another_sols_id': get_list_of_another_sols_id(),
                'checkbox_values': get_checkbox_values(),
                'file_type': file_type
    }

    export_as_file(data)
}

function export_as_file(data){
    data = JSON.stringify(data);
    $.ajax({
        type: 'POST',
        url: 'export_as_file',
        data: {'data': data},
        // dataType: 'json',
        xhrFields:{
            responseType: 'blob'
        },
        success: function(data){
            if (typeof data === 'object') {
                var anchor = document.createElement('a');
                var url = window.URL || window.webkitURL;
                anchor.href = url.createObjectURL(data);
                anchor.download = 'problems.pdf';
                document.body.append(anchor);
                anchor.click();
                setTimeout(function () {
                    document.body.removeChild(anchor);
                    url.revokeObjectURL(anchor.href);
                }, 1)
            }
            else{
                console.log('error while compile pdf')
            }
        },
            error: function(error) {
            console.log('error');
        }
    });
}