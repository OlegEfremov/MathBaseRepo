function export_tasknumbers_csv(){
        $.ajax({
        url: 'export_tasknumbers_csv',
        type: "POST",
        xhrFields:{responseType: 'blob'},
        data: {'dbID': create_data['node_dbID'], 'dbType': create_data['node_dbType']},
        success: function(data){
            var anchor = document.createElement('a');
            var url = window.URL || window.webkitURL;
            anchor.href = url.createObjectURL(data);
            anchor.download = 'tasknumbers.csv';
            document.body.append(anchor);
            anchor.click();
            setTimeout(function(){
                document.body.removeChild(anchor);
                url.revokeObjectURL(anchor.href);
            }, 1)
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}

function export_tasks_csv(){
    console.log('23')
    $.ajax({
        url: 'export_tasks_csv',
        type: "POST",
        xhrFields:{responseType: 'blob'},
        data: {'dbID': create_data['node_dbID'], 'dbType': create_data['node_dbType']},
        success: function(data){
            var anchor = document.createElement('a');
            var url = window.URL || window.webkitURL;
            anchor.href = url.createObjectURL(data);
            anchor.download = 'tasks.csv';
            document.body.append(anchor);
            anchor.click();
            setTimeout(function(){
                document.body.removeChild(anchor);
                url.revokeObjectURL(anchor.href);
            }, 1)
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}