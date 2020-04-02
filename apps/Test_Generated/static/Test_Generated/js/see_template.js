function see_template(id){
    console.log('see_template')

    $.ajax({
        url: 'see_template',
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