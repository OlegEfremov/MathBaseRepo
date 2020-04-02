function delete_template_from_db(id){
    console.log('delete_template_from_db')

        $.ajax({
        url: 'delete_template_from_db',
        type: "POST",
        data: {'template_id': template_id,
            'test_name': document.getElementById('test_name').value,
            'test_comment': document.getElementById('test_comment').value
        },
        success: function(res) {
            window.location.href = '../../test_generated/'+res;
            console.log(res)
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}