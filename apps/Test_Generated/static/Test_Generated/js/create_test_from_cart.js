var target_folder_for_new_test_id = ''

function create_test_from_cart_modal() {
    $('#create_test_by_star_folder_modal').modal('show')
}

function create_test_from_cart() {

    var rows = document.getElementById('task_table').rows;

    var tasks = '';
    for (var i=0; i<rows.length; i++) {
        if (i === 0){
            tasks += rows[i].id
        }
        else{
            tasks += ','+rows[i].id
        }
    }

    $.ajax({
        type: 'POST',
        url: '../../test_generated/create_test_from_cart',
        data: {
            'data': tasks,
            'current_test_folder': test_folder_action_data['current_test_folder'],
            'test_name': document.getElementById('test_by_star_folder_name').value,
            'test_comment': document.getElementById('test_by_star_folder_comment').value,
        },
        dataType: 'json',
        success: function (res) {
            window.location.href = '../../test_generated/' + res + '/';
        },
        error: function (error) {
            console.log('error');
        }
    });
}
