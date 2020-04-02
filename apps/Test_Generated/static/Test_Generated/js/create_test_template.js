function create_test_template() {
    var folders_dbID_list = get_folders_dbID_list();
    var array_of_inputs_values = get_array_of_inputs_values().join();

    $.ajax({
        url: 'create_test_template',
        type: "POST",
        data: {'folders': folders_dbID_list,
            'inputs_values' : array_of_inputs_values,
            'template_name': document.getElementById('template_name').value,
            'template_comment': document.getElementById('template_comment').value
        },
        success: function(res) {
            var name = res.split('@')[0];
            var id = res.split('@')[1];

            document.getElementById('templates').innerHTML += '<button class="btn btn-link" onclick=\'create_test_by_template_modal("'+id+'")\'>Cоздать работу по шаблону '+id+'.'+name+'</button>'+
                '<button class="btn btn-link" onclick="delete_template_from_db('+id+')" id="delete_template_button_'+id+'">'+
                    '<i class="fas fa-eye"></i>'+
                '</button>'+

                '<a href="../../admin/Main/test_template/'+id+'/change/" data-toggle="tooltip" title="Редактировать шаблон работы" target="_blank">'+
                    '<i class="fas fa-edit"></i>'+
                '</a>'+

                '<button class="btn btn-link" onclick="see_template({{ test_template.id }})" id="see_template_button_{{ test_template.id }}">'+
                    '<i class="fas fa-trash-alt"></i>'+
                '</button>'+
                '<br>'


        },
        error: function(ts) {
            console.log(ts)
        }
    })
}

function get_folders_dbID_list(){
    var el = document.getElementById('folders_for_test').childNodes;
    var ar='';

    console.log(el)

    for (var i=0; i<el.length; i++) {
        if (i === 0){
            ar += el[i].id.replace('folder_dbID_','')
        }
        else {
            ar += ','+el[i].id.replace('folder_dbID_','')
        }
    }
    return ar
}
