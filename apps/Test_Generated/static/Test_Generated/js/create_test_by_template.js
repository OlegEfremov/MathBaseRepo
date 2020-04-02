function create_test_by_template_modal(tmplt_id){
    template_id = tmplt_id;
    $("#create_test_by_template_modal").modal("show")
}

function create_test_by_template(){
    console.log(target_test_folder_id);
    $.ajax({
        url: 'create_test_by_template',
        type: "POST",
        data: {
            'template_id': template_id,
            'test_name': document.getElementById('test_by_template_name').value,
            'test_comment': document.getElementById('test_by_template_comment').value,
            'current_test_folder': target_test_folder_id
        },
        success: function(res) {
            window.location.href = '../../test_generated/'+res+'/';
            console.log(res)
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}