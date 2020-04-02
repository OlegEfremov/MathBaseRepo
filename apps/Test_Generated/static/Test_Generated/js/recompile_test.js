function recompile_test(test_id){
    $.ajax({
        url: '../recompile_test',
        type: "POST",
        data: {'test_id': test_id},
        success: function(res) {
            window.location.href = '../../test_generated/'+res+'/';
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}


function random_change_task_in_test(test_id, task_number){

    $.ajax({
        url: '../random_change_task_in_test',
        type: "POST",
        data: {'test_id': test_id, 'task_number': task_number},
        success: function(res) {
            window.location.href = '../../test_generated/'+res+'/';
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}