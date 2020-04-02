function export_folder_to_tex(folder_id){
    var settings = {};

    let checkboxes = $("input:checkbox"),
        checkbox_values = {};
    for (var i=0; i<checkboxes.length;i++){
        settings[checkboxes[i].id] = checkboxes[i].checked
    }

    $.ajax({
        url: '../../export_folder_to_tex',
        type: "POST",
        data: {
            'folder_id': folder_id,
            'settings': JSON.stringify(settings)
        },
        xhrFields:{
            responseType: 'blob'
        },
        success: function(data){
            if (typeof data === 'object') {
                var anchor = document.createElement('a');
                var url = window.URL || window.webkitURL;
                anchor.href = url.createObjectURL(data);
                anchor.download = 'problems.zip';
                document.body.append(anchor);
                anchor.click();
                setTimeout(function () {
                    document.body.removeChild(anchor);
                    url.revokeObjectURL(anchor.href);
                }, 1)
            }
            else{
                console.log('error while make tex')
            }
        },
        error: function(ts) {
            console.log(ts)
        }
    });
}

function export_folder_to_pdf(folder_id){
    var settings = {};

    let checkboxes = $("input:checkbox"),
        checkbox_values = {};
    for (var i=0; i<checkboxes.length;i++){
        settings[checkboxes[i].id] = checkboxes[i].checked
    }

    $.ajax({
        url: '../../export_folder_to_pdf',
        type: "POST",
        data: {
            'folder_id': folder_id,
            'settings': JSON.stringify(settings)
        },
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
        error: function(ts) {
            console.log(ts)
        }
    });
}