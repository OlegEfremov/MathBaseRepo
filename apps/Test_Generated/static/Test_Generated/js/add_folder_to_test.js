function add_folder_to_test(){
    let e_div = document.getElementById('folders_for_test');
    var l = e_div.childNodes.length;
    var input_id = 'number_of_task_from_folder_'+ view_folder["dbID"] +'_'+(l+1).toString();

    // save inputs values
    var a=[];
    var all_inputs = $(':input[type="number"]');
    for (var i=0; i<all_inputs.length; i++){
        a.push(all_inputs[i].value)
    }

    // add new folder
    var br = '';
    if (all_inputs.length !== 0){br = '<br>'}

    e_div.innerHTML += '<span id="folder_dbID_'+view_folder["dbID"]+'">'+br+
                            '<i class="fas fa-folder"></i> '+view_folder['Name']+
                            ' - <input type="number" step=1 value="1" min="1" style="width: 3em;" id="'+input_id+'">'+
                            ' - <button class="btn btn-link" onclick="delete_folder_from_test(this)">' +
                                '<i class="fas fa-trash-alt"></i>' +
                            '</button>'+
                        '</span>';

    // set inputs values
    var all_inputs = $(':input[type="number"]')
    for (var i=0; i<all_inputs.length-1; i++){
        all_inputs[i].value = a[i]
    }

}