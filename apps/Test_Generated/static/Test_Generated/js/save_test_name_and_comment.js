$(document).ready(function() {
    document.getElementById('test_name_input').value = document.getElementById('test_name').innerHTML;
    document.getElementById('test_comment_textarea').value = document.getElementById('test_comment').innerText;
});

function save_test_name_and_comment(test_id){
    var test_name = document.getElementById('test_name_input').value;
    var test_comment = document.getElementById('test_comment_textarea').value;

    $.ajax({
        type: 'POST',
        url: '../save_test_name_and_comment',
        data: {'test_name': test_name,
            'test_comment': test_comment,
            'test_id': test_id
        },
        dataType: 'json',
        success: function (res) {
            console.log(res)
        },
        error: function (error) {
            console.log(error);
        }
    });
    document.getElementById('test_name').innerHTML = test_name;
    document.getElementById('test_comment').innerText = test_comment
}