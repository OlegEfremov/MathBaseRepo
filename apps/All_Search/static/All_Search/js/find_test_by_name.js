function find_test_by_name() {
    var test_name = document.getElementById('find_test_by_name_input').value;

    $.ajax({
        url: "find_test_by_name",
        type: "POST",
        data: {'test_name': test_name},
        success: function (res) {
            document.getElementById('table_of_tasks').innerHTML = '';
            document.getElementById('table_of_tasks').innerHTML = res;

            },
        error: function (ts) {
            console.log(ts)
        }
    });
    return false;

}