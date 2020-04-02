function open_test_answers(test_id, is_open){
    var root_path = get_root_path()
    $.ajax({
        url: root_path+'test_generated/open_test_answers',
        type: "POST",
        data: {
            'test_id': test_id,
            'is_open': is_open
        },
        success: function(res) {},
        error: function(ts) {
            console.log(ts)
        }
    })

}
