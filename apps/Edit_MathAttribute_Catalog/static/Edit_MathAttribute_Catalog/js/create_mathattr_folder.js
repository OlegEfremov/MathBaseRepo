function create_mathattr_folder(){

    let send_data = {
        'parent_dbID': document.getElementById('parent_folder').value
    };

    console.log(send_data)
    $.ajax({
        type: 'POST',
        url: 'create_mathattr_folder',
        data: send_data,
        dataType: 'json',
        success: function(data){
            $('#mathattr_tree').jstree(true).refresh();
            node_to_select_dbID = data['dbID']
        },
        error : function(error) {console.log(error)}
    });

}