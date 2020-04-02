function find_test_by_id() {
    var test_id = document.getElementById('find_test_by_id_input').value;
    window.location.href = '../../test_generated/' + test_id + '/';

    // $.ajax({
    //     url: "find_test_by_id",
    //     type: "POST",
    //     data: {'test_id': test_id},
    //     success: function (res) {
    //         window.location.href = '../../test_generated/' + res + '/';
    //         },
    //     error: function (ts) {
    //         console.log(ts)
    //     }
    // });
    // return false;

}