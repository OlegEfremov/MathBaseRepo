function change_folder_acces_status(is_access_open){
    $.ajax({
        type: 'POST',
        url: 'change_folder_access_status',
        data: {'folder_id': action_data['view_folder'], 'access_status': is_access_open},
        dataType: 'json',
        success: function(data){
        console.log('success')
        },
        error : function(error) {console.log(error)}
    });

    set_test_link(is_access_open)
}


function set_test_link(is_access_open){
    if (is_access_open) {
        document.getElementById('link_for_test').innerHTML = 'Ссылка на тест: '+window.location.hostname+'/solution_catalog/test_' + action_data['view_folder']
    }
    else {
        document.getElementById('link_for_test').innerHTML = ''
    }
}

function set_access_checkbox(){
    if (document.getElementById('folder_access_status') === null){return}

    var status = document.getElementById('folder_access_status').innerText;
    var checkbox = document.getElementById('access_checkbox');
    if (status === 'True'){
        checkbox.checked = true;
        set_test_link(true)
    }
    else {
        checkbox.checked = false;
        set_test_link(false)
    }
}
