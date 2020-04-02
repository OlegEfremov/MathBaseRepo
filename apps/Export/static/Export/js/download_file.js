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
        'checkbox_values': checkbox_values,
        'file_type': 'tex'
    };
    send_data = JSON.stringify(send_data);
    $.ajax({
        type: 'POST',
        url: 'download_dynamic_text',
        data: {'data':send_data},
        // dataType: 'json',
        xhrFields:{
            responseType: 'blob'
        },
        // success: function(res){
            // window.location = res
            // let contents = res;
            // download_file('my_file.tex', contents)
        // },
        success: function(data){
            var anchor = document.createElement('a');
            var url = window.URL || window.webkitURL;
            anchor.href = url.createObjectURL(data);
            anchor.download = 'problems.pdf';
            document.body.append(anchor);
            anchor.click();
            setTimeout(function(){
                document.body.removeChild(anchor);
                url.revokeObjectURL(anchor.href);
            }, 1)
        },
        error: function(error) {
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
