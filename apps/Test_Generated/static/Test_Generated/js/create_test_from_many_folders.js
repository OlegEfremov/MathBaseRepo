function create_test_from_many_folders(){
    var el = document.getElementById('folders_for_test').childNodes;
    var ar='';

    for (var i=0; i<el.length; i++) {
        if (i === 0){
            ar += el[i].id.replace('folder_dbID_','')
        }
        else {
            ar += ','+el[i].id.replace('folder_dbID_','')
        }
    }

    var array_of_inputs_values = get_array_of_inputs_values().join();

    $.ajax({
        url: 'create_test_from_many_folders',
        type: "POST",
        data: {
            'data': ar,
            'array_of_inputs_values' : array_of_inputs_values,
            'test_name': document.getElementById('test_name').value,
            'test_comment': document.getElementById('test_comment').value,
            'current_test_folder': test_folder_action_data['current_test_folder']
        },
        success: function(res) {
            window.location.href = '../../test_generated/'+res+'/';
        },
        error: function(ts) {
            console.log(ts)
        }
    })
}