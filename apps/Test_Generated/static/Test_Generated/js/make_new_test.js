function get_number_of_tasks_in_new_test(){
    var e = document.getElementById('number_of_task_in_new_test');
    return e.value;
}

function make_new_test(){
      $.ajax({
        url: 'make_new_test',
        type: "POST",
        data: {'number_of_tasks_in_new_test': get_number_of_tasks_in_new_test(),
            'view_folder':view_folder['dbID'],
            'test_name': document.getElementById('test_name').value,
            'test_comment': document.getElementById('test_comment').value
        },
        success: function(res) {
            window.location.href = '../../test_generated/'+res;
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}